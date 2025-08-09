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

example
# Get a random compliment
curl -X GET http://127.0.0.1:5003/compliment

# Get the full list of compliments
curl -X GET http://127.0.0.1:5003/compliments

# Add a new compliment
curl -X POST http://127.0.0.1:5003/compliment \
  -H "Content-Type: application/json" \
  -d '{"text":"Alla, your persistence is inspiring!"}'

# Error: empty text field (400)
curl -X POST http://127.0.0.1:5003/compliment \
  -H "Content-Type: application/json" \
  -d '{"text":""}'

# Error: duplicate compliment (409)
curl -X POST http://127.0.0.1:5003/compliment \
  -H "Content-Type: application/json" \
  -d '{"text":"Alla, your persistence is inspiring!"}'

