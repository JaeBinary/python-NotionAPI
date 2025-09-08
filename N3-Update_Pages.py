import requests
from datetime import datetime, timezone

NOTION_TOKEN = "ntn_rH7725048958OuqPA8JyHnBa39nxix9XFX7P0v8RSY80TA"
DB_ID = "26802e0b7d3f8084bb29e9f61fd411bd"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    print(res.status_code)
    return res

page_id = "26802e0b-7d3f-812b-893e-defb1c740ea3"

title = "Updated Title"
update_data = {"Title": {"rich_text": [{"text": {"content": title}}]}}

update_page(page_id, update_data)
