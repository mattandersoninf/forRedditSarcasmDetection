import config
import praw
import os
import csv
import pandas as pd
from pprint import pprint
import multiprocessing

# make reddit object to access the API and enter the credentials as per the config file

#def getSubredditDataMP(sr):



"""
# an example dataset has compiled comments from the following subreddits
# AskReddit, politics, worldnews, leagueoflegends, pcmasterrace, news, funny, pics, todayileanred, GlobalOffensive, AlexJones, The_Donald, JoeRogan, vegan, Overwatch, apexlegends, CallOfDuty, ukpolitics, oddlysatisfying, conspiracy, AskAnAmerican, DotA2, wow, firstworldanarchists, youtubehaiku, Whatcouldgowrong, LivestreamFail, FIFA, cringe, uncensorednews, worldpolitics, JusticeServed, showerthoughts, leagueoflegends, BlackPeopleTwitter, space, DestinyTheGame, TopMindsOfReddit, FloridaMan, ImGoingToHellForThis, anime_irl, cringe, BigBrother

# remember to add a condition that verifies if the subreddit still exists

# [pics, uncensorednews] don't work, expel for now

# pics for example throws the following exception "prawcore.exceptions.NotFound: received 404 HTTP response", will review later

# response 404 means that the resource does not exist. look further into what could have been removed from reddit

# response 504 reddit is under heavy pressure, or you're trying to throw up a cooment into reddit's database (which this script does not do at all)

"""


subreddits = ['AskReddit', 'politics', 'worldnews', 'leagueoflegends', 
              'pcmasterrace', 'news', 'funny', 'todayileanred', 
              'GlobalOffensive', 'AlexJones', 'The_Donald', 'JoeRogan', 
              'vegan', 'Overwatch', 'apexlegends', 'CallOfDuty', 
              'ukpolitics', 'oddlysatisfying', 'conspiracy', 
              'AskAnAmerican', 'DotA2', 'wow', 'firstworldanarchists',
              'youtubehaiku', 'Whatcouldgowrong', 'LivestreamFail', 
              'FIFA', 'cringe', 
              'worldpolitics', 
              'JusticeServed', 'showerthoughts', 'leagueoflegends', 
              'BlackPeopleTwitter', 'space', 'DestinyTheGame', 
              'TopMindsOfReddit', 'FloridaMan', 'ImGoingToHellForThis', 
              'anime_irl', 'cringe', 'BigBrother']


def getSubredditData():
    reddit = praw.Reddit(client_id = config.client_id,
                        client_secret = config.client_secret,
                        username = config.username,
                        password = config.password,
                        user_agent = config.user_agent)


    tmp_dataframe = pd.DataFrame(columns=['body','author','created_utc','subreddit','id','link_id','parent_id'])
    

    #,'politics','BlackPeopleTwitter','space','TopMindsOfReddit','vegan','Overwatch','wow','The_Donald']
    for sr in subreddits:
        print(sr)
        subreddit = reddit.subreddit(sr)

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
                    tmp_dataframe = tmp_dataframe.append(pd.DataFrame({'body':[str(comment.body)], 
                                                                       'author':[str(comment.author)], 
                                                                       'created_utc':[str(comment.created_utc)], 
                                                                       'subredit':[str(comment.subreddit)], 
                                                                       'id':[str(comment.id)], 
                                                                       'link_id':[str(comment.link_id)], 
                                                                       'parent_id':[str(comment.parent_id)]}),ignore_index=True,sort=True)
                    #tmp_dataframe.append(pd.DataFrame([comment.body, comment.author, comment.created_utc, comment.subreddit, comment.id, comment.link_id, comment.parent_id], columns=['body','author','created_utc','subreddit','id','link_id','parent_id']))
                                  
                    i = str(int(i)+1)
                    if int(i) > 10:
                        break
                except praw.exceptions.PRAWException:
                    pass

    return tmp_dataframe

"""
# this with statement opens up the untrained-data.csv file in the data folder

with open('../data/untrained-data.csv', mode ='w') as udcsv:
    
    for sr in subreddits:
        subreddit = reddit.subreddit(sr)

        # get the 10 most popular reddit comments in the defined subreddit 
        hot_python = subreddit.hot(limit=10)

        # for now, the goal of the script is to be able to extract the parameters mentioned in the 

        for submission in hot_python:
            udcsv.write
"""


if __name__=="__main__":

    pprint(getSubredditData())

    """
    with multiprocessing.Pool() as pool:
        pool.map(getSubredditDataMP, subreddits)
    """
