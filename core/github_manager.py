"""
GitHub integration for config storage and GitHub Pages deployment
"""
import os
import logging
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
        
        # Ensure configs directory exists by creating .gitkeep if needed
        try:
            self.repo.get_contents("configs/.gitkeep")
        except:
            # Create configs directory with .gitkeep
            self.repo.create_file(
                path="configs/.gitkeep",
                message="Create configs directory",
                content="# This directory stores VLESS configurations\n",
                branch="main"
            )
        
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
        
        # Update GitHub Pages index
        self._update_pages_index()
        
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
    
    def _update_pages_index(self) -> None:
        """
        Automatically update the GitHub Pages index file with all available configs
        """
        try:
            # Get all config files
            contents = self.repo.get_contents("configs")
            configs = []
            
            if isinstance(contents, list):
                for item in contents:
                    if item.name.endswith(".txt") and item.name != ".gitkeep":
                        # Extract username from filename
                        parts = item.name.rsplit("_", 2)  # Split from right: username_YYYYMMDD_HHMMSS.txt
                        if len(parts) >= 3:
                            username = "_".join(parts[:-2])  # Handle usernames with underscores
                        else:
                            username = item.name.replace(".txt", "")
                        
                        configs.append({
                            "username": username,
                            "filename": item.name,
                            "created_at": item.last_modified or "Unknown",
                            "download_url": f"{self.get_pages_url()}configs/{item.name}"
                        })
                
                # Sort by creation time (newest first)
                configs.sort(key=lambda x: x["filename"], reverse=True)
                
                # Generate and upload index.html
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
        except Exception as e:
            logger = logging.getLogger(__name__)
            logger.warning(f"Could not update pages index: {e}")
    
    def update_pages_index(self, configs: List[dict]) -> None:
        """
        Update the GitHub Pages index file with available configs (manual override)
        
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
            download_url = config.get('download_url', f"configs/{config['filename']}")
            config_rows += f"""
            <tr>
                <td>{config['username']}</td>
                <td>{config['created_at']}</td>
                <td><a href="{download_url}" target="_blank">Download</a></td>
            </tr>
            """
        
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>VLESS Configs</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
        h1 {{ color: #333; }}
        table {{ border-collapse: collapse; width: 100%; max-width: 800px; margin: 20px auto; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
        th {{ background-color: #4CAF50; color: white; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
        tr:hover {{ background-color: #f1f1f1; }}
        a {{ color: #4CAF50; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .info {{ background: #e7f3ff; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔑 VLESS Configuration Files</h1>
        <div class="info">
            <p><strong>Note:</strong> These configuration files are for personal use only. Do not share them publicly.</p>
        </div>
        <table>
            <tr>
                <th>Username</th>
                <th>Created</th>
                <th>Download</th>
            </tr>
            {config_rows}
        </table>
    </div>
</body>
</html>
"""
