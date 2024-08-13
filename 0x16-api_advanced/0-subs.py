#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers.
    """
    apiUrl = f"https://reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"}

    try:
        response = requests.get(apiUrl, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except requests.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")
        return 0
    except ValueError as e:
        print(f"Error decoding JSON response: {e}")
        return 0

