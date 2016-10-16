#! /usr/bin/env python

import time
from keys import token, username, name, email, branch
from github3 import login

class github_bot():
    
    # init method
    def __init__(self):
        # login to github and get the correct repository
        self.access = login(username=username, token=token)
        self.repository = self.access.repository(username, 'GithubBotRepo')
        self.filename = 'daily_updates.txt'       

        # get today's date
        self.time_now = (time.strftime("%m-%d-%Y-%I-%M-%S"))
        self.time_string = (time.strftime("%m/%d/%Y"))

        # construct the contents of our commit and commit message.
        self.content = "Today's date is " + self.time_string + "."
        self.commit_message = "Commit for " + self.time_string

        self.file_contents = self.repository.file_contents(self.filename).decoded
        self.file_contents += "\n" + self.content

        # so the files in the repos are stored as tuples, with <name, file object/contents> in them.
        # get the directory contents
        self.dir_contents = self.repository.directory_contents('/')
        
    def run(self):
        # get the correct file. is there a better way to do this than iterating through?
        self.file_to_update = None
        for item in self.dir_contents:
            if(item[0] == self.filename):
                self.file_to_update = item

        # make sure we found the right file before we update it.
        if(self.file_to_update != None):
            # actually update the file.
            self.file_to_update[1].update(self.commit_message, self.file_contents, branch)

# now we need to instantiate this class.
bot = github_bot()
bot.run()
