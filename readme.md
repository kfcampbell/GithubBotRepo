# Github Bot Project

They got rid of streaks, but I figured there was still some fun to be had in manipulating the Github API with python.

## Usage
Clone the repo, then make a cron job to run the GithubUpdate.py script each day.

## Things It Would Be Nice To Add

* a better way to construct a JSON request than just string manipulation (done. used github3.py)
* simply update a single file rather than add a new file each time (done)
* randomly commit more than once on some occasions (done)
* add more interesting commit messages
* add logging

## Dependencies
* github3.py (pip install github3.py==1.0.0a4)
