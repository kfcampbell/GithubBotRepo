#! /usr/bin/env python

import time
import random
from keys import token, username, name, email, branch
from github3 import login
from Helpers import get_commit_message


class GithubBot:

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
        self.commit_message = get_commit_message()  # "Commit for " + self.time_string

        self.file_contents = self.repository.file_contents(self.filename, branch).decoded
        self.file_contents += "\n" + self.content

        # so the files in the repos are stored as tuples, with <name, file object/contents> in them.
        # get the directory contents
        self.dir_contents = self.repository.directory_contents('/')
        
    def run(self, commit_message, file_contents):
        # get the correct file. is there a better way to do this than iterating through?
        self.file_to_update = None
        for item in self.dir_contents:
            if item[0] == self.filename:
                self.file_to_update = item
                break

        # make sure we found the right file before we update it.
        if self.file_to_update is not None:
            # actually update the file.
            self.file_to_update[1].update(commit_message, file_contents, branch)
            
    # this is where we determine how many times we're going to commit today
    def determine_commits(self):
        # need to get a random number. say, between 1 and 8 commits, weighted towards the bottom?
        number_of_commits = 0
        rand = random.randint(1, 100) # get a random integer between 1 and 100.
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
        print "Commits to make: " + str(number_of_commits)
        
        # make the first commit.
        self.run(self.commit_message, self.file_contents)
        
        # make any further commits.
        for commit in range(1, number_of_commits):
            # construct the contents of our commit and commit message.
            self.content = "Commit number " + str(commit + 1) + " for " + self.time_string + "."
            self.commit_message = get_commit_message()  # "Another commit for " + self.time_string + "."
            self.file_contents = self.repository.file_contents(self.filename).decoded
            self.file_contents += "\n" + self.content 
            
            # print "content: " + self.content
            # print "commit message: " + self.commit_message
            # print self.file_contents
            self.run(self.commit_message, self.file_contents)


# now we need to instantiate this class.
try:
    bot = GithubBot()
    bot.determine_commits()
except Exception, e:
    print "error with the bot: " + e.message
