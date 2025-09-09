import requests
from datetime import datetime, timezone

NOTION_TOKEN = "ntn_Fa7725048959YKXe513xFsNuyA4atXrYPlbwOhAEpLpcAz"
DB_ID = "26802e0b7d3f8084bb29e9f61fd411bd"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DB_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    print(res.status_code)
    return res

url = "Test URL 2"
title = "Test Title 2"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "URL": {"title": [{"text": {"content": url}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "Published": {"date": {"start": published_date, "end": None}}
}

create_page(data)
