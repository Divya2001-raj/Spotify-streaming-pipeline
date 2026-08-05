import requests  # Used to make HTTP requests

from spotify.auth import get_access_token  # Generates Spotify access token

from ingestion.save_raw import save_raw_json  # Saves raw JSON response


def get_artist_details(artist_id):  # Fetch details for a specific artist

    token = get_access_token()  # Generate access token

    url = f"https://api.spotify.com/v1/artists/{artist_id}"  # Artist Details endpoint

    headers = {
        "Authorization": f"Bearer {token}"  # Pass access token
    }

    response = requests.get(  # Send GET request
        url,
        headers=headers
    )
    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Response:")
    print(response.text)

    response.raise_for_status()

    data = response.json()
    print("Status Code:", response.status_code)  # Print status code

    #response.raise_for_status()  # Raise error if request fails

    #data = response.json()  # Convert JSON response into Python dictionary

    save_raw_json(  # Save raw response
        data=data,
        entity="artist_details",
        file_name=data["name"].replace(" ", "_")
    )

    return data  # Return response