#!/usr/bin/python3
"""
A function that shows the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a
    given subreddit
    """
    if subreddit is None and type(subreddit) is not str:
        return 0
    base = 'https://www.reddit.com'
    r = requests.get('{}/r/{}/about.json'.format(base, subreddit),
                     headers={'User-Agent': 'n_onyekachukwu'},
                     allow_redirects=False).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
