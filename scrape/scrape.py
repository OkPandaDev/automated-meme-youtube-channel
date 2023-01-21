import os

subreddit = input("subreddit: ")
amount = input("amount of videos: ")

os.system(f"gallery-dl --range 1-{amount} https://www.reddit.com/r/{subreddit}/")