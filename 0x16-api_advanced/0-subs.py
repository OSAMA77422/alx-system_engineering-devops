#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid, returns 0.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers.
    """
    apiUrl = f"https://reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom User-Agent for Reddit API query"
    }

    try:
        response = requests.get(apiUrl, headers=headers, allow_redirects=False)
        
        # Check for redirect status code
        if response.status_code == 302:
            return 0
        
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    
    except requests.RequestException:
        # Handle any request exceptions (network issues, invalid requests)
        return 0

    except ValueError:
        # Handle JSON decoding issues
        return 0

