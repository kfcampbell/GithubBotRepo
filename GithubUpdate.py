#! /usr/bin/env python

import time
import random
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
            
    # this is where we determine how many times we're going to commit today
    def determine_commits(self):
        print "entered determining commits function."
        
        # need to get a random number. say, between 1 and 8 commits, weighted towards the bottom?
        number_of_commits = 0
        rand = random.randint(1, 100) # get a random integer between 1 and 100.
        print rand
        # experiment with weighting.
        if rand < 3:
            number_of_commits = 8
        elif rand < 8:
            number_of_commits = 7
        elif rand < 14:
            number_of_commits = 6
        elif rand < 20:
            number_of_commits = 5
        elif rand < 29:
            number_of_commits = 4
        elif rand < 35:
            number_of_commits = 3
        elif rand < 55:
            number_of_commits = 2
        else:
            number_of_commits = 1
        print number_of_commits
        
        # now commit this many times.
        for time in range(0,number_of_commits):
            # run needs to be modified to take the commit message and stuff.
            # get today's date
            self.time_now = (time.strftime("%m-%d-%Y-%I-%M-%S"))
            self.time_string = (time.strftime("%m/%d/%Y"))

            # construct the contents of our commit and commit message.
            self.content = "Today's date is " + self.time_string + "."
            self.commit_message = "Commit for " + self.time_string


# now we need to instantiate this class.
bot = github_bot()
bot.determine_commits()