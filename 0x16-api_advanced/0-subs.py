#!user/bin/python3

"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
#Return the total number of subscribers on a given subreddit.
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200 and response.text.strip():
        try:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']
            else:
                print("Unexpected response format.")
                return 0
        except ValueError:
            print("Failed to parse JSON from the response.")
            return 0
    else:
        print("Failed to retrieve data. Status code: {}".format(response.status_code))
        return 0
