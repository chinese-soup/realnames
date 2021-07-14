#!/usr/bin/env python3

import re

split_re = re.compile(r"\s{2,}")
id64_base = 76561197960265728

def get_steam_id64(steamID):
    id_str = str(steamID)
    id_split = id_str.split(":")  # Split string into 'Universe', Account type, and Account number

    account_type = int(id_split[1])  # Check for account type
    account_id = int(id_split[2])  # Account number, needs to be doubled when added to id64

    id64 = id64_base + (account_id * 2) + account_type

    return str(id64)

if __name__ == "__main__":
    with open("realnames.txt", "r") as f:
        lines = f.readlines()

    new_player_lines = []

    for line in lines:
        if line.startswith("//") or line.startswith("\n"): # Skip comments and empty lines
            continue

        split_line = split_re.split(line)
        old_steamid = split_line[0]
        name = split_line[1][:-4].strip()
        nationality = split_line[1][-4:].replace(".", "")
        new_steamid = get_steam_id64(old_steamid)
        new_player_lines.append(f"{old_steamid},{new_steamid},{name},{nationality}")

    # meh
    with open("realnames64.csv", "w") as f:
        f.write("steamid,steamid64,name,nationality\n")
        for new_line in new_player_lines:
            f.write(new_line)

    print("Done.")
