import config
import praw
import os
import csv
import pandas as pd
from pprint import pprint
import multiprocessing
import subreddit_file
import fileinput

subreddits = subreddit_file.subreddits

def getSubredditDataMP(sr):
    
    # make reddit object to access the API and enter the credentials as per the config file
    
    reddit = praw.Reddit(client_id = config.client_id,
                                  client_secret = config.client_secret,
                                  username = config.username,
                                  password = config.password,
                                  user_agent = config.user_agent)
    

    tmp_dataframe = pd.DataFrame(columns=['body','author','created_utc','subreddit','id','link_id','parent_id'])
    

    print(sr)
    subreddit = reddit.subreddit(sr)

    # get the 10 most popular reddit comments in the defined subreddit 
    hot_python = subreddit.hot(limit=3)

    
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
                                
                i = str(int(i)+1)
                if int(i) > 10:
                    break
            except praw.exceptions.PRAWException:
                pass
    """
    mode = ''
    
    if os.path.isfile('../data/untrained-data.csv'): os.path

    mode='w' if os.path.isfile('../redditAPI/data/untrained-data.csv') else 'a'
    """

    tmp_dataframe.to_csv(os.path.join(os.getcwd(),'redditAPI','data','untrained-data.csv'), mode='a', encoding='utf-8', index=False)


if __name__=="__main__":
    
    # print(os.getcwd())
    
    with multiprocessing.Pool() as pool:
        pprint(pool.map(getSubredditDataMP, subreddits))
    
