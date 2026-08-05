# Spotify artist search functionality will be implemented in Phase 2.2.

import requests  # Used to make HTTP requests to Spotify API

from spotify.auth import get_access_token  # Import the function that generates the access token


def search_artist(artist_name):  # Function to search an artist by name

    token = get_access_token()  # Generate a valid access token

    url = "https://api.spotify.com/v1/search"  # Spotify Search API endpoint

    headers = {  # HTTP request headers
        "Authorization": f"Bearer {token}"  # Pass the access token
    }

    params = {  # Query parameters
        "q": artist_name,  # Artist name entered by the user
        "type": "artist",  # Search only artists
        "limit": 1  # Return only one matching artist
    }

    response = requests.get(  # Send GET request
        url,
        headers=headers,
        params=params
    )

    print("Status Code:", response.status_code)  # Print status code for debugging

    response.raise_for_status()  # Raise an exception if request fails

    return response.json()  # Convert JSON response to Python dictionary