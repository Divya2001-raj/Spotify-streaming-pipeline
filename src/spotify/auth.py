# Spotify authentication logic will be implemented in Phase 2.1.

import os  # Used to read environment variables

import base64  # Used to encode Client ID and Secret

import requests  # Used to send HTTP requests

from pathlib import Path  # Used to locate the project root

from dotenv import load_dotenv  # Used to load the .env file


load_dotenv(Path(__file__).resolve().parents[2] / ".env")  # Load environment variables from the project root


CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")  # Read Spotify Client ID

CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")  # Read Spotify Client Secret


def get_access_token():  # Function to generate an access token

    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"  # Combine Client ID and Secret

    auth_bytes = auth_string.encode("utf-8")  # Convert to bytes

    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")  # Encode in Base64

    headers = {  # HTTP headers
        "Authorization": f"Basic {auth_base64}"  # Spotify expects Base64 credentials
    }

    data = {  # Request body
        "grant_type": "client_credentials"  # OAuth Client Credentials Flow
    }

    response = requests.post(  # Send POST request
        "https://accounts.spotify.com/api/token",
        headers=headers,
        data=data
    )
    """print("CLIENT_ID:", CLIENT_ID)

    print("CLIENT_SECRET:", CLIENT_SECRET)

    print("Status Code:", response.status_code)

    print("Response:", response.text)"""
    
    response.raise_for_status()  # Raise an exception for HTTP errors

    return response.json()["access_token"]  # Return only the access token