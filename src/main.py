from spotify.artists import search_artist


def main():

    artist = search_artist("Arijit Singh")

    print(artist["artists"]["items"][0]["name"])
    print(artist["artists"]["items"][0]["id"])
    print(artist["artists"]["items"][0]["external_urls"]["spotify"])


if __name__ == "__main__":

    main()