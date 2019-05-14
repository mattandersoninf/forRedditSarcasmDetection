import config

import praw

# make reddit object to access the API and enter the credentials as per the config file

reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

# an example dataset has compiled comments from the following subreddits
# AskReddit, politics, worldnews, leagueoflegends, pcmasterrace, news, funny, pics, todayileanred, GlobalOffensive, AlexJones, The_Donald, 
# JoeRogan, vegan, Overwatch, apexlegends, CallOfDuty, ukpolitics, oddlysatisfying, conspiracy, AskAnAmerican, DotA2, wow, 
# firstworldanarchists, youtubehaiku, Whatcouldgowrong, LivestreamFail, FIFA, cringe, uncensorednews, worldpolitics, JusticeServed,
# showerthoughts, leagueoflegends, BlackPeopleTwitter, space, DestinyTheGame, TopMindsOfReddit, FloridaMan, ImGoingToHellForThis,
# anime_irl, cringe, BigBrother

subreddit = reddit.subreddit('funny')

hot_python = subreddit.hot(limit=1)

for submission in hot_python:
    print(submission)
