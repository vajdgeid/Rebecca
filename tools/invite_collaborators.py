#!/usr/bin/env python3
import csv
import json
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

OWNER = "vajdgeid"
REPO = "Rebecca"
CSV_PATH = os.path.join(os.getcwd(), "github_accounts.csv")


def read_accounts(path):
    accounts = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = (row.get('username') or '').strip()
            email = (row.get('email') or '').strip().strip('"')
            token = (row.get('token') or '').strip()
            if username:
                accounts.append({
                    'username': username,
                    'email': email,
                    'token': token,
                })
    return accounts


def find_owner_token(accounts):
    for a in accounts:
        if a['username'] == OWNER and a['token']:
            return a['token']
    # fallback to env
    env_tok = os.getenv('GITHUB_TOKEN')
    if env_tok:
        return env_tok
    raise RuntimeError('Owner token not found in CSV or env GITHUB_TOKEN')


def invite_collaborator(token: str, collaborator: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/collaborators/{collaborator}"
    data = json.dumps({"permission": "push"}).encode('utf-8')
    req = Request(url=url, data=data, method='PUT')
    req.add_header('Authorization', f'token {token}')
    req.add_header('Accept', 'application/vnd.github+json')
    try:
        with urlopen(req, timeout=20) as resp:
            status = resp.status
            body = resp.read().decode('utf-8', errors='ignore')
            return status, body
    except HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='ignore')
    except URLError as e:
        return -1, str(e)


def main():
    accounts = read_accounts(CSV_PATH)
    owner_token = find_owner_token(accounts)
    invited = []
    for a in accounts:
        if a['username'] and a['username'] != OWNER:
            status, body = invite_collaborator(owner_token, a['username'])
            invited.append((a['username'], status))
            print(f"invite {a['username']}: {status}")
    print(json.dumps({"invited": invited}))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)
