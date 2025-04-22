# GTrack.py
import argparse
import os
import requests
from github import Github
import logger_wrapper

# ---------------------- Argument Parsing ---------------------- #
def parse_args():
    parser = argparse.ArgumentParser(description="GitHub Repo Base Committer & Logger")
    parser.add_argument('--api', action='store_true')
    parser.add_argument('--botAs', type=str, default='GTracker')
    parser.add_argument('--botPfp', type=str, default=None)
    parser.add_argument('--incommit', action='store_true')
    parser.add_argument('--readme', type=str, choices=['true', 'false'], default='true')
    parser.add_argument('--bold', action='store_true')
    parser.add_argument('--licsensetype', type=int, choices=range(1, 6))
    parser.add_argument('--gitignore', type=str, choices=['true', 'false'], default='false')
    parser.add_argument('--extrafile', type=str)
    parser.add_argument('--extrafiletype', type=str)
    parser.add_argument('--content', type=str)
    parser.add_argument('--customcommitmessage', type=str)
    parser.add_argument('--vmode', action='store_true')
    parser.add_argument('--addtimestamp', type=str, choices=['true', 'false'], default='false')
    parser.add_argument('--SecurityFile', type=str, choices=['true', 'false'], default='false')
    return parser.parse_args()

# ---------------------- GitHub Manager ---------------------- #
class GitHubRepoManager:
    def __init__(self, token, repo_name, username, bot_pfp=None):
        self.g = Github(token)
        self.user = self.g.get_user()
        self.repo = self._get_or_create_repo(repo_name)
        self.username = username
        self.bot_pfp = bot_pfp

    def _get_or_create_repo(self, name):
        try:
            return self.user.get_repo(name)
        except:
            return self.user.create_repo(name, auto_init=False)

    def commit_file(self, path, content, commit_msg, vmode):
        try:
            contents = self.repo.get_contents(path)
            if vmode:
                self.repo.update_file(contents.path, commit_msg, content, contents.sha)
                log_action("UPDATED", path, commit_msg)
            else:
                log_action("SKIPPED (Exists)", path, commit_msg)
        except:
            self.repo.create_file(path, commit_msg, content)
            log_action("CREATED", path, commit_msg)

# ---------------------- Helper Functions ---------------------- #
def log_action(action, filename, message):
    args = parse_args()
    add_timestamp = args.addtimestamp == 'true'
    logger_wrapper.clog("GTrack.log", action, filename, message, add_timestamp)

def format_readme(bold):
    text = "# Project Title\n\nThis is a base README."
    return f"**{text}**" if bold else text

def get_license(lic_id):
    license_map = {
        1: 'mit',
        2: 'apache-2.0',
        3: 'apache-2.0',
        4: 'unlicense',
        5: 'gpl-3.0'
    }
    license_key = license_map.get(lic_id)
    if license_key:
        return fetch_license_text(license_key)
    else:
        raise ValueError("Invalid license type")

def fetch_license_text(license_key):
    url = f"https://api.github.com/licenses/{license_key}"
    headers = {"Accept": "application/vnd.github.raw+json"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return f"License fetch failed ({response.status_code})"

def create_security_file(content=None):
    return content if content else "> [!IMPORTANT]\n> \n> **This is NOT a malicious tool. Do not use it in any wrong way.**"

# ---------------------- Main Logic ---------------------- #
def main():
    args = parse_args()
    token = os.getenv('GH_TOKEN')
    if not token:
        print("Error: GH_TOKEN environment variable is not set.")
        return

    repo_name = "auto-created-repo"
    manager = GitHubRepoManager(token, repo_name, args.botAs, args.botPfp)
    commit_msg = args.customcommitmessage or "Initial commit"

    if args.readme == 'true':
        manager.commit_file("README.md", format_readme(args.bold), commit_msg, args.vmode)

    if args.licsensetype:
        license_content = get_license(args.licsensetype)
        manager.commit_file("LICENSE", license_content, commit_msg, args.vmode)

    if args.gitignore == 'true':
        manager.commit_file(".gitignore", "# Add your ignores here", commit_msg, args.vmode)

    if args.SecurityFile == 'true':
        security_text = create_security_file(args.content if args.extrafile == 'SECURITY.md' else None)
        manager.commit_file("SECURITY.md", security_text, commit_msg, args.vmode)

    if args.extrafile and args.extrafiletype and args.content:
        filename = f"{args.extrafile}.{args.extrafiletype}"
        manager.commit_file(filename, args.content, commit_msg, args.vmode)

if __name__ == "__main__":
    main()
