from spotify.artists import search_artist  # Import artist search function


def main():

    artist = search_artist("Arijit Singh")  # Search Spotify

    print(artist)  # Display the response


if __name__ == "__main__":

    main()