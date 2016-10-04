#! /usr/bin/env python

import os
import time
import base64
from keys import token, name, email

# get today's date
time_now = (time.strftime("%m-%d-%Y-%I-%M-%S"))
time_string = (time.strftime("%m/%d/%Y"))

# variables to update the string
file_name = "daily_updates.txt"
committer_string = "\"committer\": {\"name\": \"" + name + "\", \"email\": \"" + email + "\"}"
content = "Today's date is " + time_string + "."
content_encoded = base64.b64encode(content)
message = "Commit for " + time_string
# path = "Updates/" + time_now + ".txt"
path = file_name
branch = "master"
link = "https://api.github.com/repos/kfcampbell/GithubBotRepo/contents/" + path

# update the file with today's date.
with open(file_name, "a") as daily_file:
    daily_file.write(content + "\n")

# actual string to start with and add to
command = "curl -i -X PUT -H \'Authorization: token "
command += token
# add the path
command += "\' " + "-d \'{\"path\": \"" + path + "\", "
# add the message
command += "\"message\": \"" + message + "\", "
# add the committer info
command += committer_string + ", "
# add the content
command += "\"content\": \"" + content_encoded + "\", "
# add the branch
command += "\"branch\": \"" + branch + "\"}\' "
# add the url
command += link

print command

# now we run the thing.
os.system(command)
