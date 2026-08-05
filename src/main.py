from spotify.auth import get_access_token  # Import the authentication function


def main():

    token = get_access_token()  # Generate an access token

    print(token)  # Print the token


if __name__ == "__main__":

    main()