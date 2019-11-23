# Block Twitter List Creators

People are finding themselves on thousands of hate- and abuse-promoting lists. In order to provide a first step against destructive behavior, this python script will block all the creators of these lists. Every blocked Twitter user gets logged to the terminal (together with the list's name).

When you block a list creator, you are automatically removed from the list. This is regular Twitter behavior.

**Note:** This script currently doesn't evaluate the origin of the list in any way. It will indiscriminately block everyone. You can still manually unblock people you've had positive experiences with by finding their Twitter usernames in the terminal logs.

## Usage

1. Install [Python3](https://www.python.org/downloads/).
2. If you don't have pip (python package manager), [install it](https://pip.pypa.io/en/stable/installing/) as well.
3. Open a terminal in the project's directory and run `pip install -r requirements.txt`.
4. Copy [.env.example](.env.example) to `.env` and enter your [Twitter app keys](https://developer.twitter.com/en/apps).
5. Start the script with `python start.py`.

## Notes

* This is an extremely simple script, made in half an hour to [give a little help](https://twitter.com/moorehn/status/1089185034727313408). All contributions are welcome via complete, and documented, pull request.
