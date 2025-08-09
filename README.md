# requirements.txt
# Compliment API (Flask)

Simple API that returns random compliments and lets you add new ones.

## Quick start
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python flaskgit.py

Endpoints
GET /compliment — random compliment

GET /compliments — all compliments

POST /compliment — add a compliment ({"text": "..."} ≤ 140 chars)
