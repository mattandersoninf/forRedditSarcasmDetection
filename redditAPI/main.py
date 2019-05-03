import config

import praw

# make reddit object to access the API and enter the credentials as per the config file

reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

subreddit = reddit.subreddit('funny')

hot_python = subreddit.hot(limit=1)

for submission in hot_python:
    print(submission)
