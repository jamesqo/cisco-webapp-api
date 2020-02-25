import os

from flask import Flask, render_template, request
import praw

app = Flask(__name__)
reddit = praw.Reddit(client_id=os.environ['CWA_ID'],
                     client_secret=os.environ['CWA_SECRET'],
                     user_agent='flask:cisco-webapp-api:v1.0.0')

def pluck(obj, fields):
    return {field: getattr(obj, field) for field in fields}

def trim_submission(submission):
    result = pluck(submission, [
        'author',
        'is_self',
        'num_comments',
        'permalink',
        'score',
        'selftext',
        'title',
        'url'
    ])
    result['author'] = result['author'].id
    return result

def error(message, status):
    return {'error': message}, status

@app.route('/top/<subreddit>')
def top(subreddit):
    scope = request.args.get('scope', 'all', type=str)
    limit = request.args.get('limit', 10, type=int)
    if subreddit is None:
        return error('Please specify a subreddit.', 400)
    if scope not in ('all', 'day', 'week', 'hour', 'month', 'year'):
        return error('Invalid scope.', 400)
    if limit < 0:
        return error("limit can't be negative.", 400)

    submissions = reddit.subreddit(subreddit).top(time_filter=scope, limit=limit) # TODO: Get all of them (lazily load)
    submissions = list(map(trim_submission, submissions))
    return {
        'data': submissions
    }
