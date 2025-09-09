import requests
from datetime import datetime, timezone

NOTION_TOKEN = "ntn_Fa7725048959YKXe513xFsNuyA4atXrYPlbwOhAEpLpcAz"
DB_ID = "26802e0b7d3f8084bb29e9f61fd411bd"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def delete_page(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, json=payload, headers=headers)
    print(res.status_code)
    return res

page_id = "26802e0b-7d3f-812b-893e-defb1c740ea3"

delete_page(page_id)
