# cisco-webapp-api

This repo contains the API implementation of the web app. It uses the PRAW client in order to get the top articles for a given subreddit, trims unneeded fields, then returns the result in JSON.

## Frameworks Used

- Flask
- PRAW

## Instructions

Go to https://www.reddit.com/prefs/apps and get a new client ID and client secret. Then run

```
export CWA_ID=your_client_id
export CWA_SECRET=your_client_secret
export FLASK_APP=app.py

pip install -r requirements.txt
flask run
```

Python 3.6+ is required.

## Demonstration

https://cisco-webapp-api.herokuapp.com/top/askreddit
