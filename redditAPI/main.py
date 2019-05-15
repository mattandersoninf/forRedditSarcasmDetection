import config
import praw
import os
import csv

# make reddit object to access the API and enter the credentials as per the config file

reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     username = config.username,
                     password = config.password,
                     user_agent = config.user_agent)

"""
# an example dataset has compiled comments from the following subreddits
# AskReddit, politics, worldnews, leagueoflegends, pcmasterrace, news, funny, pics, todayileanred, GlobalOffensive, AlexJones, The_Donald, 
# JoeRogan, vegan, Overwatch, apexlegends, CallOfDuty, ukpolitics, oddlysatisfying, conspiracy, AskAnAmerican, DotA2, wow, 
# firstworldanarchists, youtubehaiku, Whatcouldgowrong, LivestreamFail, FIFA, cringe, uncensorednews, worldpolitics, JusticeServed,
# showerthoughts, leagueoflegends, BlackPeopleTwitter, space, DestinyTheGame, TopMindsOfReddit, FloridaMan, ImGoingToHellForThis,
# anime_irl, cringe, BigBrother
"""

subreddits = ['AskReddit']
#,'politics','BlackPeopleTwitter','space','TopMindsOfReddit','vegan','Overwatch','wow','The_Donald']

subreddit = reddit.subreddit('AskReddit')

# get the 10 most popular reddit comments in the defined subreddit 
hot_python = subreddit.hot(limit=3)

# for now, the goal of the script is to be able to extract the parameters mentioned in the 


# comment.body is for getting the text from each comment, it seems that it the api digs into the replies 10 levels deep
# do research into the controversiality parameter of comments

# convert utc parameter possibly

for submission in hot_python:
    comments = submission.comments.list()
    i = str(0)
    for comment in comments:
        try:
            print('\n'+i+'. Comment Body: '+str(comment.body))
            print('\n'+i+'. Comment Author: '+str(comment.author))
            print('\n'+i+'. Comment Post Time: '+str(comment.created_utc))
            print('\n'+i+'. Comment Subreddit: '+str(comment.subreddit))
            i = str(int(i)+1)
            if int(i) > 10:
                break
        except praw.exceptions.PRAWExceotion:
            pass

"""
# this with statement opens up the untrained-data.csv file in the data folder
# whatever
with open('../data/untrained-data.csv', mode ='a') as udcsv:
    if 
    for sr in subreddits:
        subreddit = reddit.subreddit(sr)

        # get the 10 most popular reddit comments in the defined subreddit 
        hot_python = subreddit.hot(limit=10)

        # for now, the goal of the script is to be able to extract the parameters mentioned in the 

        for submission in hot_python:
            udcsv.write
"""