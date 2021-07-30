# realnames
This repository for realnames is used for the HLTV.download website to match players from demos with their realnames, it's supposed to be run everytime the upstream realnames get a change.

How to use:
1. Pull the upstream `realnames.txt`
2. Run `convert_to_64.py` to generate a CSV file with an additional column (steamID in steamID64 format).
3. Run `dump_to_db.py` to delete all the previous realnames and dump all of them again in a single transaction to a SQLite3 database.

Preferably do this in cron or something.

## Original README follows:

# realnames
Realnames are used in Adrenaline Gamer for displaying player's real identity and their nationality whilst they are connected to the server.

## Installation & Usage
Simply drop realnames.txt to the AG folder, then enter `loadauthid` in console to display realnames for everyone in the server. To disable it, use `unloadauthid`.

## Credits and thanks to
* The original creator(s) - unknown
* Hardstyle - maintaining and updating realnames 2014-2017
* Godsbane - for slag
* Rammy
* (:
