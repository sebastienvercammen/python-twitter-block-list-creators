def error_handler(error):
    """Log a TweepError exception."""
    if error.api_code:
        if error.api_code == 32:
            print("invalid API authentication tokens")
        elif error.api_code == 34:
            print("requested object (user, Tweet, etc) not found")
        elif error.api_code == 64:
            print("your account is suspended and is not permitted")
        elif error.api_code == 130:
            print("Twitter is currently in over capacity")
        elif error.api_code == 131:
            print("internal Twitter error occurred")
        elif error.api_code == 135:
            print("could not authenticate your API tokens")
        elif error.api_code == 136:
            print("you have been blocked to perform this action")
        elif error.api_code == 179:
            print("you are not authorized to see this Tweet")
        else:
            print("error while using the REST API: %s", tweep_error)
    else:
        print("error with Twitter: %s", tweep_error)
