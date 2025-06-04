import os
import requests

class APIClient:
    def __init__(self):
        # This should be in environment variables!
        self.github_token = "ghp_1234567890abcdefghijklmnopqrstuvwx123456"
        self.jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
        
    def call_api(self):
        headers = {
            "Authorization": f"Bearer {self.github_token}",
            "X-JWT-Token": self.jwt_token
        }
        return requests.get("https://api.github.com/user", headers=headers)

if __name__ == "__main__":
    client = APIClient()
    print("App started successfully")