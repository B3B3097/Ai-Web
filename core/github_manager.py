"""
GitHub integration for config storage and GitHub Pages deployment
"""
import os
from github import Github
from typing import Optional, List
from datetime import datetime


class GitHubManager:
    """Manage GitHub repository for config storage"""
    
    def __init__(self, token: str, repo_name: str, pages_repo_name: Optional[str] = None):
        """
        Initialize GitHub manager
        
        Args:
            token: GitHub personal access token
            repo_name: Repository name for config storage (format: owner/repo)
            pages_repo_name: Optional separate repository for GitHub Pages
        """
        self.github = Github(token)
        self.repo_name = repo_name
        self.pages_repo_name = pages_repo_name or repo_name
        self.repo = self.github.get_repo(repo_name)
        self.pages_repo = self.github.get_repo(self.pages_repo_name)
        
    def upload_config(self, username: str, config: str, filename: Optional[str] = None) -> str:
        """
        Upload a VLESS config to the repository
        
        Args:
            username: Username for the config owner
            config: VLESS config string
            filename: Optional custom filename
            
        Returns:
            Path to the uploaded file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"configs/{username}_{timestamp}.txt"
        else:
            filename = f"configs/{filename}"
        
        # Check if file exists
        try:
            contents = self.repo.get_contents(filename)
            # Update existing file
            self.repo.update_file(
                path=contents.path,
                message=f"Update config for {username}",
                content=config,
                sha=contents.sha,
                branch="main"
            )
        except:
            # Create new file
            self.repo.create_file(
                path=filename,
                message=f"Add config for {username}",
                content=config,
                branch="main"
            )
        
        return filename
    
    def get_config(self, username: str) -> Optional[str]:
        """
        Retrieve the latest config for a user
        
        Args:
            username: Username to search for
            
        Returns:
            Config content or None if not found
        """
        try:
            contents = self.repo.get_contents("configs")
            if isinstance(contents, list):
                # Find the most recent config for this user
                user_configs = [c for c in contents if c.name.startswith(username)]
                if user_configs:
                    # Sort by name (which includes timestamp) and get the latest
                    user_configs.sort(key=lambda x: x.name, reverse=True)
                    latest = user_configs[0]
                    return latest.decoded_content.decode()
        except:
            pass
        
        return None
    
    def delete_config(self, filename: str) -> bool:
        """
        Delete a config file
        
        Args:
            filename: Path to the file to delete
            
        Returns:
            True if successful, False otherwise
        """
        try:
            contents = self.repo.get_contents(filename)
            self.repo.delete_file(
                path=contents.path,
                message=f"Delete config {filename}",
                sha=contents.sha,
                branch="main"
            )
            return True
        except:
            return False
    
    def get_pages_url(self) -> str:
        """
        Get the GitHub Pages URL
        
        Returns:
            GitHub Pages base URL
        """
        try:
            pages = self.pages_repo.get_pages()
            return pages.html_url
        except:
            # If pages is not enabled, construct the URL
            owner = self.pages_repo.owner.login
            repo_name = self.pages_repo.name
            return f"https://{owner}.github.io/{repo_name}/"
    
    def update_pages_index(self, configs: List[dict]) -> None:
        """
        Update the GitHub Pages index file with available configs
        
        Args:
            configs: List of config metadata dictionaries
        """
        html_content = self._generate_index_html(configs)
        
        try:
            contents = self.pages_repo.get_contents("index.html")
            self.pages_repo.update_file(
                path=contents.path,
                message="Update configs index",
                content=html_content,
                sha=contents.sha,
                branch="main"
            )
        except:
            self.pages_repo.create_file(
                path="index.html",
                message="Create configs index",
                content=html_content,
                branch="main"
            )
    
    def _generate_index_html(self, configs: List[dict]) -> str:
        """Generate HTML index page"""
        config_rows = ""
        for config in configs:
            config_rows += f"""
            <tr>
                <td>{config['username']}</td>
                <td>{config['created_at']}</td>
                <td><a href="configs/{config['filename']}">Download</a></td>
            </tr>
            """
        
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>VLESS Configs</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>VLESS Configuration Files</h1>
    <table>
        <tr>
            <th>Username</th>
            <th>Created</th>
            <th>Download</th>
        </tr>
        {config_rows}
    </table>
</body>
</html>
"""
