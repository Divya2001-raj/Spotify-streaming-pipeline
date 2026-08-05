from spotify.artists import search_artist
from spotify.artist_details import get_artist_details


def main():

    artist = search_artist("Arijit Singh")

    artist_id = artist["artists"]["items"][0]["id"]

    details = get_artist_details(artist_id)

    print("Artist Name:", details["name"])
    print("Artist ID:", details["id"])
    print("Spotify URL:", details["external_urls"]["spotify"])
    print("Artist URI:", details["uri"])


if __name__ == "__main__":
    main()