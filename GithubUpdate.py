#! /usr/bin/env python

import os
import time
import base64
from keys import token, username, name, email
from github3 import login

# login to github and get the correct repository
access = login(username=username, token=token)
repository = access.repository(username, 'GithubBotRepo')
filename = 'daily_updates.txt'

# get today's date
time_now = (time.strftime("%m-%d-%Y-%I-%M-%S"))
time_string = (time.strftime("%m/%d/%Y"))

# construct the contents of our commit and commit message.
content = "Today's date is " + time_string + "."
commit_message = "Commit for " + time_string

file_contents = repository.file_contents(filename).decoded
file_contents += "\n" + content

# so the files in the repos are stored as tuples, with <name, file object/contents> in them.
# get the directory contents
dir_contents = repository.directory_contents('/')

# get the correct file. is there a better way to do this than iterating through?
file_to_update = None
for item in dir_contents:
    if(item[0] == filename):
        file_to_update = item

# make sure we found the right file before we update it.
if(file_to_update != None):
    # actually update the file.
    file_to_update[1].update(commit_message, file_contents)