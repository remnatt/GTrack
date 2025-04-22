# GTrack.py
import argparse
import requests
import os
import logging
from datetime import datetime
from github import Github

# ---------------------- Logging Setup ---------------------- #
logging.basicConfig(filename='GTrack.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# ---------------------- Argument Parsing ---------------------- #
def parse_args():
    parser = argparse.ArgumentParser(description="GitHub Repo Base Committer & Logger")
    
    parser.add_argument('--api', action='store_true')
    parser.add_argument('--botAs', type=str, default='GTracker')
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
    
    return parser.parse_args()

# ---------------------- License Mapping ---------------------- #
LICENSE_MAP = {
    1: 'MIT License',
    2: 'Apache License 2.0',
    3: 'Apache License 2.0',
    4: 'The Unlicense',
    5: 'GNU General Public License v3.0'
}

LICENSE_TEMPLATES = {
    1: 'MIT license content...',
    2: 'Apache 2.0 license content...',
    4: 'Unlicense content...',
    5: 'GNU license 3.0 content...'
}

# ---------------------- GitHub Manager ---------------------- #
class GitHubRepoManager:
    def __init__(self, token, repo_name, username):
        self.g = Github(token)
        self.user = self.g.get_user()
        self.repo = self._get_or_create_repo(repo_name)
        self.username = username

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
    logging.info(f"{action} | {filename} | {message}")

def format_readme(bold):
    text = "# Project Title\n\nThis is a base README."
    return f"**{text}**" if bold else text

def get_license(lic_id):
    return LICENSE_TEMPLATES.get(lic_id, "License not found")

# ---------------------- Main Logic ---------------------- #
def main():
    args = parse_args()

    token = os.getenv('GH_TOKEN')
    repo_name = "auto-created-repo"  # This could be passed in as a CLI arg too
    manager = GitHubRepoManager(token, repo_name, args.botAs)

    commit_msg = args.customcommitmessage or "Initial commit"
    
    if args.readme == 'true':
        manager.commit_file("README.md", format_readme(args.bold), commit_msg, args.vmode)

    if args.licsensetype:
        license_content = get_license(args.licsensetype)
        manager.commit_file("LICENSE", license_content, commit_msg, args.vmode)

    if args.gitignore == 'true':
        manager.commit_file(".gitignore", "# Add your ignores here", commit_msg, args.vmode)

    if args.extrafile:
        filename = f"{args.extrafile}.{args.extrafiletype}"
        manager.commit_file(filename, args.content, commit_msg, args.vmode)

if __name__ == "__main__":
    main()
