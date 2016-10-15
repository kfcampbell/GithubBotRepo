# Github Bot Project

I know they got rid of streaks, but this is a bot I made to play with Github's API to post a new file every day.

## Usage
Clone the repo, then make a cron job to run the GithubUpdate.py script each day.

## Things It Would Be Nice To Add

* a better way to construct a JSON request than just string manipulation (done. used github3.py)
* simply update a single file rather than add a new file each time (done)
* randomly commit more than once on some occasions and not at all on others
* add logging

## Dependencies
* github3.py (pip install --pre github3.py)
