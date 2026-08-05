import requests  # Used to make HTTP requests

from spotify.auth import get_access_token  # Import authentication function

from ingestion.save_raw import save_raw_json  # Import JSON saving function


def search_artist(artist_name):  # Search for an artist

    token = get_access_token()  # Generate access token

    url = "https://api.spotify.com/v1/search"  # Spotify Search API

    headers = {
        "Authorization": f"Bearer {token}"  # Pass access token
    }

    params = {
        "q": artist_name,  # Artist name
        "type": "artist",  # Search only artists
        "limit": 1  # Return only one result
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    print("Status Code:", response.status_code)  # Print status code

    response.raise_for_status()  # Raise error if request fails

    data = response.json()  # Convert JSON response into a Python dictionary

    save_raw_json(  # Save the raw response
        data=data,
        entity="artists",
        file_name=artist_name.replace(" ", "_")
    )

    return data  # Return the API response