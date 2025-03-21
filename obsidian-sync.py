import requests
import json

with open("Obsidian-Sync/params.json") as f:
    params = json.load(f)

NOTION_API_KEY = params["NOTION_API_KEY"]
NOTION_DATABASE_ID = params["NOTION_DATABASE_ID"]
OBSIDIAN_VAULT_PATH = params["OBSIDIAN_VAULT_PATH"]


def notion_auth():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
    }
    response = requests.request("POST", url, headers=headers)
    print(response.text)


def sync():
    # Function to sync data between Notion and Obsidian
    print("Syncing...")
    notion_auth()
    print("Synced!")


if __name__ == "__main__":
    sync()
