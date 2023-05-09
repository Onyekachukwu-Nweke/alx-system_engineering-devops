#!/usr/bin/python3
"""
A function that shows the top ten posts
"""
import requests as req


def top_ten(subreddit):
    """
    Returns the top ten posts for a
    given subreddit
    """
    if subreddit is None and type(subreddit) is not str:
        return 0
    base = 'https://www.reddit.com'
    header = {'User-Agent': 'n_onyekachukwu'}
    params = {'limit': 10}
    res = req.get('{}/r/{}/hot.json'.format(base, subreddit), params=params,
                  headers=header, allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
