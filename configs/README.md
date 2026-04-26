# VLESS Config Generator - Configuration Guide

## Overview
This project uses a single repository for both config storage and GitHub Pages hosting.
All configurations are stored in the `configs/` directory and automatically served via GitHub Pages.

## Repository Structure

```
your-repo/
├── configs/          # VLESS configuration files (auto-generated)
│   ├── username_20240101_120000.txt
│   └── username_20240102_150000.txt
├── index.html        # Auto-generated index page for GitHub Pages
├── README.md
└── .github/
    └── workflows/
        └── pages.yml # Optional: GitHub Actions for Pages deployment
```

## Setup Instructions

### 1. Create Your Repository

1. Go to GitHub and create a new repository (e.g., `vless-configs`)
2. Make it **Public** (required for GitHub Pages free tier)
3. Initialize with a README if desired

### 2. Enable GitHub Pages

1. Go to your repository Settings
2. Navigate to **Pages** section
3. Under **Source**, select:
   - Deploy from a branch
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**

Your GitHub Pages URL will be:
```
https://your-username.github.io/vless-configs/
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and update:

```bash
# In your main bot repository's .env file
CONFIG_REPO=your-username/vless-configs
PAGES_REPO=your-username/vless-configs
```

**Note:** Both `CONFIG_REPO` and `PAGES_REPO` point to the same repository.

### 4. GitHub Personal Access Token

Ensure your token has these permissions:
- ✅ `repo` (Full control of private repositories)
- ✅ `workflow` (if using GitHub Actions)

To create:
1. GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Select scopes: `repo`, `workflow`
4. Copy and save securely

### 5. Directory Structure

The bot will automatically:
- Create `configs/` directory if it doesn't exist
- Store configs as `configs/{username}_{timestamp}.txt`
- Generate/update `index.html` for GitHub Pages

### 6. File Naming Convention

Configs are named as:
```
configs/{username}_{YYYYMMDD}_{HHMMSS}.txt
```

Example:
```
configs/Weleredz_20240126_143022.txt
```

### 7. GitHub Pages Index

The bot automatically generates an `index.html` file that lists all available configs:

```html
<!DOCTYPE html>
<html>
<head>
    <title>VLESS Configs</title>
</head>
<body>
    <h1>VLESS Configuration Files</h1>
    <table>
        <tr>
            <th>Username</th>
            <th>Created</th>
            <th>Download</th>
        </tr>
        <!-- Auto-populated -->
    </table>
</body>
</html>
```

## Usage Flow

1. User clicks "Get Proxy" in Telegram
2. Bot generates VLESS config
3. Bot uploads to `configs/` directory in your repo
4. Bot updates `index.html` on GitHub Pages
5. Config is accessible via: `https://your-username.github.io/vless-configs/configs/username_timestamp.txt`

## Manual Management

### View Configs
Browse to: `https://your-username.github.io/vless-configs/`

### Download Config
Direct link: `https://your-username.github.io/vless-configs/configs/{filename}.txt`

### Delete Old Configs
1. Go to your repository on GitHub
2. Navigate to `configs/` folder
3. Delete unwanted files
4. The bot will update the index automatically on next generation

## Security Considerations

⚠️ **Important:**
- Repository must be **Public** for free GitHub Pages
- Config files are publicly accessible via GitHub Pages URL
- Only share config URLs with intended users
- Consider implementing additional authentication if needed

## Troubleshooting

### GitHub Pages Not Working

1. Verify repository is Public
2. Check Pages settings in repository Settings
3. Wait 1-2 minutes for deployment
4. Ensure `index.html` exists in root directory

### Config Upload Fails

1. Verify GITHUB_TOKEN has `repo` scope
2. Check CONFIG_REPO format: `owner/repo`
3. Ensure repository exists and you have write access

### 404 Errors

1. Wait for GitHub Pages to deploy (check Actions tab)
2. Verify file path is correct
3. Check browser cache

## Advanced Configuration

### Custom Domain

To use a custom domain:
1. Add CNAME file to repository root
2. Configure DNS records with your domain provider
3. Update VLESS_SNI in bot configuration

### Multiple Users

The bot supports multiple usernames but only responds to @Weleredz by default.
To allow more users, modify `ALLOWED_USERNAME` in `bot/main.py`:

```python
ALLOWED_USERNAMES = ["Weleredz", "user2", "user3"]

def is_allowed_user(self, username: str) -> bool:
    return username in ALLOWED_USERNAMES
```

## API Endpoints

Once configured, configs are accessible at:

- **Index Page:** `https://{owner}.github.io/{repo}/`
- **Config File:** `https://{owner}.github.io/{repo}/configs/{filename}.txt`
- **Raw File:** `https://raw.githubusercontent.com/{owner}/{repo}/main/configs/{filename}.txt`

## Maintenance

### Regular Cleanup
Periodically remove old configs:
```bash
# Example: Remove configs older than 30 days
find configs/ -name "*.txt" -mtime +30 -delete
```

### Monitoring
Check GitHub Actions tab for deployment status and errors.

## Support

For issues or questions, check:
- GitHub Issues in this repository
- Telegram Bot API documentation
- GitHub Pages documentation
