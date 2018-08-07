# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 10:32:46 2018

@author: othapliy
"""

import praw

import pdb
import os
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")
nPosts = 25;
        
if not os.path.isfile("posts_responded_to.txt"):
    posts_responded_to = []
else:
    with open("posts_responded_to.txt", "r") as f:
        posts_responded_to = f.read()
        posts_responded_to = posts_responded_to.split("\n")
        posts_responded_to = list(filter(None, posts_responded_to))
        
        
for submission in subreddit.hot(limit = nPosts):
    if submission.id not in posts_responded_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Please be gentle. Incoming first bot repsonse!!")
            print("Bot responding to: ",submission.id)
            posts_responded_to.append(submission.id)

with open("posts_responded_to.txt", "w") as f:
    for postID in posts_responded_to:
        f.write(postID + "\n")
    
            