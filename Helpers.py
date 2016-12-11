#! /usr/bin/env python

# this class will contain helpers for getting interesting commit messages from whatthecommit.com
import urllib2


def get_commit_message():
    try:
        url = "http://whatthecommit.com/index.txt"
        open_url = urllib2.urlopen(url)
        commit_message = open_url.read().rstrip()
        return commit_message
    except Exception, e:
        return None

get_commit_message()
