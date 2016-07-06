# Github Bot Project

I know they got rid of streaks, but this is a bot I made to play with Github's API to post a new file every day.

## Usage
Create a new repo, then run a cron job to run the GithubUpdate.py script each day.

## Things It Would Be Nice To Add

* a better way to construct a JSON request than just string manipulation
* simply update a single file rather than add a new file each time
* a way to construct base64-encoded and hashed content rather than using a hardcoded version
* store each new file in a folder rather than in the main directory
