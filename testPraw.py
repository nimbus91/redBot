# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:53:02 2018

@author: othapliy
"""

import praw
import os
import re

reddit = praw.Reddit(client_id='YuIXUmw-u4yBrQ',
                     client_secret = 'mVGUMS8AW5KCdkvlYbECKoBDQwE',
                     user_agent = 'AngloBot',
                     username = '-Cunning-Stunt-',
                     password = '45Minutes!')
subreddit = reddit.subreddit("pythonforengineers")
nPosts = 5;

if not os.path.isfile("shitposting.txt"):
    posts_responded_to = []
else:
    with open("shitposting.txt", "r") as f:
        posts_responded_to = f.read()
        posts_responded_to = posts_responded_to.split("\n")
        posts_responded_to = list(filter(None, posts_responded_to))

for submission in subreddit.hot(limit = nPosts):
    if submission.id not in posts_responded_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Please be gentle. Incoming first bot repsonse!!")
            print("Bot responding to: ",submission.id)
            posts_responded_to.append(submission.id)

with open("shitposting.txt", "w") as f:
    for postID in posts_responded_to:
        f.write(postID + "\n")