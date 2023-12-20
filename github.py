import os
import requests
import base64


class GitHubUploader:

    def __init__(self, token=None, owner=None, repo=None):
        self.token = token
        self.owner = owner
        self.repo = repo

    def get_url(self, owner, repo, file_path):
        path = os.path.relpath(file_path, os.getcwd())
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

        return url

    def get_headers(self, token):
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28"
        }

        return headers

    def get_sha_if_exists(self, file_path, ref):
        url = self.get_url(self.owner, self.repo, file_path)
        headers = self.get_headers(self.token)
        params = {
            "ref": ref
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()["sha"]
        elif response.status_code == 404:
            return None
        else:
            error = "Failed to get " + file_path + ". Status code: " \
                + response.status_code + ", Message: " + response.text
            raise Exception(error)

    def base64_encode(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()
        content_base64 = base64.b64encode(content).decode()

        return content_base64

    def create_file(self, file_path, content, branch):
        url = self.get_url(self.owner, self.repo, file_path)
        headers = self.get_headers(self.token)
        data = {
            "message": f"upload {file_path} via API",
            "committer": {
                "name": "yamanashi-icalendar-updater",
                "email": "yamanashi-icalendar-updater@yuukis.github.io"
            },
            "content": content,
            "branch": branch
        }

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 201:
            print(f"Successfully uploaded {file_path} on branch {branch}")
        else:
            print(f"Failed to upload {file_path}. "
                  + f"Status code: {response.status_code}, "
                  + f"Message: {response.text}")

    def update_file(self, file_path, content, sha, branch):
        url = self.get_url(self.owner, self.repo, file_path)
        headers = self.get_headers(self.token)
        data = {
            "message": f"upload {file_path} via API",
            "committer": {
                "name": "yamanashi-icalendar-updater",
                "email": "yamanashi-icalendar-updater@yuukis.github.io"
            },
            "content": content,
            "sha": sha,
            "branch": branch
        }
        data["sha"] = sha

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"Successfully uploaded {file_path} on branch {branch}")
        else:
            print(f"Failed to upload {file_path}. "
                  + f"Status code: {response.status_code}, "
                  + f"Message: {response.text}")

    def upload(self, file_path, ref="main", branch="main"):
        if not self.token:
            raise ValueError("GitHub token is not set.")
        if not self.owner:
            raise ValueError("GitHub repository owner is not set.")
        if not self.repo:
            raise ValueError("GitHub repository name is not set.")

        sha = self.get_sha_if_exists(file_path, ref)
        content = self.base64_encode(file_path)

        if sha is None:
            self.create_file(file_path, content, branch)
        else:
            self.update_file(file_path, content, sha, branch)
