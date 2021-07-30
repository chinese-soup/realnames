#!/usr/bin/env python3
import csv, sqlite3

try:
    con = sqlite3.connect("../sql/hltvdownload.sqlite3")
    #con.set_trace_callback(print)

except Exception as e:
    print("Database connection error.")

print("Deleting old values.")
cur = con.cursor()

cur.execute("""DELETE FROM realnames;""") # don't commit this until we're done here

with open("realnames64.csv", "r") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:

        steamid = row["steamid"]
        steamid64 = row["steamid64"]
        playername = row["name"]
        nationality = row["nationality"]
        try:
            cur.execute(f"""INSERT INTO realnames VALUES (?, ?, ?, ?)""", (steamid64,
                    steamid,
                    playername,
                    nationality))
        except sqlite3.IntegrityError as e:
            try: # cursed
                print(f"Appending {playername} to exisitng record, with steamid64 = {steamid64}")
                a = cur.execute(f"""UPDATE realnames SET playername = playername || ' aka ' || ? WHERE steam_id64 = ?""", (playername, steamid64))
            except Exception as e:
                print(f"Skipping {playername} because of {e}")
        except Exception as e:
            print(f"Other exception: {e}")

print("Done.")
con.commit()
con.close()