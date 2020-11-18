import requests
import json

apiKey = "API_KEY"

print("Requesting API...")
guildRAW = requests.get(f"https://api.hypixel.net/guild?key={apiKey}&id=5cf5a97977ce84f4a05b066f").json()  # Calls hypixel guild API
print("API Loaded.")
weeklyGXP_RAW = guildRAW["guild"]["members"]

def guildGXP():

    count = 0
    guildMembersGXP = []
    for memberCount in range(len(weeklyGXP_RAW)):
        userGXP = {}
        weeklyGXP = weeklyGXP_RAW[memberCount]["expHistory"]
        userUUID = guildRAW["guild"]["members"][memberCount]["uuid"]
        userName = requests.get(f"https://api.ashcon.app/mojang/v2/user/{userUUID}").json()["username"] #Gets user UUID

        for dailyGXP in weeklyGXP.values():
            if count == 1:
                userGXP["today"] = dailyGXP
            elif count == 2:
                userGXP["yesterday"] = dailyGXP
            count = count + 1

        count = 0
        userGXP = {"username": userName, "gxp": userGXP}
        guildMembersGXP.append(userGXP)

    return sorted(guildMembersGXP, key=lambda x: x['gxp'].get('today', 0), reverse=True)

# lines.sort() is more efficient than lines = lines.sorted()
def printedList():
    guilData = guildGXP()
    for x in range(len(weeklyGXP_RAW)):
        member = guilData[x]["username"]
        dailyGXP = guilData[x]["gxp"]["today"]
        print(f"{x+1}. {member} - {dailyGXP} Guild Experience")

printedList()
