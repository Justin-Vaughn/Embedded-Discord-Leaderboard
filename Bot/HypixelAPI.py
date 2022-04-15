import requests
from functools import lru_cache

apiKey = "API_KEY"


print("Requesting API...")
guildRAW = requests.get(f"https://api.hypixel.net/guild?key={apiKey}&id=5f304eb78ea8c97248581d7f").json()  # Calls hypixel guild API
print("API Loaded.")
weeklyGXP_RAW = guildRAW["guild"]["members"]
topLB = 10  #len(weeklyGXP_RAW)


@lru_cache(maxsize=2)
def guildGXP(day="today"):
    count = 0
    guildMembersGXP = []
    for memberCount in range(len(weeklyGXP_RAW)):
        userGXP = {}
        weeklyGXP = weeklyGXP_RAW[memberCount]["expHistory"]
        userUUID = guildRAW["guild"]["members"][memberCount]["uuid"]
        userName = requests.get(f"https://api.ashcon.app/mojang/v2/user/{userUUID}").json()["username"] #Gets user UUID

        for todayGXP in weeklyGXP.values():
            if count == 1:
                userGXP["today"] = todayGXP
            elif count == 2:
                userGXP["yesterday"] = todayGXP

                break  # Breaks function after getting nessecary info (only needs today and yesterday)
            count = count + 1

        count = 0
        userGXP = {"username": userName, "gxp": userGXP}
        guildMembersGXP.append(userGXP)

    return sorted(guildMembersGXP, key=lambda x: x['gxp'].get(day, 0), reverse=True)


def todayPos(member):
    guildData = guildGXP()
    for x in range(len(weeklyGXP_RAW)):
        ign = guildData[x]["username"]
        gD = guildData[x]["gxp"]["today"]
        #print(f"{x}. (T) ign: {ign}, gxp: {gD}")
        if ign == member:
            #print(f"(T)IGN: {member}, Pos ({x+1})")
            return x+1

@lru_cache(maxsize=130)
def yesterdayPos(member):
    guildData = guildGXP("yesterday")
    for x in range(len(weeklyGXP_RAW)):
        ign = guildData[x]["username"]
        gD = guildData[x]["gxp"]["yesterday"]
        #print(f"{x}. (Y) ign: {ign}, gxp: {gD}")
        if ign == member:
            #print(f"(Y)IGN: {member}, Pos ({x+1})")
            return x

@lru_cache(maxsize=130)
def higherLower(x, member):
    today = x
    yesterday = yesterdayPos(member)
    guildData = guildGXP()
    pos = abs(today-yesterday)
    #print(f"({member}) Today: {today} - Yesterday: {yesterday}, Moved {pos}")
    if guildData[x]["gxp"]["today"] == 0 and guildData[x]["gxp"]["yesterday"] == 0:
        return "<:gray_arrow_forward:711009453704740906>"
    elif today < yesterday:
        return f"<:green_arrow_up:710198079701123113> [{pos}]"
    elif today > yesterday:
        return f"<:red_arrow_down:710198080703561920> [{pos}]"
    elif today == yesterday:
        return "<:gray_arrow_forward:711009453704740906>"

def formatedList():
    string = ""
    guildData = guildGXP()
    for x in range(topLB):
        member = guildData[x]["username"]
        todayGXP = guildData[x]["gxp"]["today"]
        if x == 0:
            string = string + f":first_place: {member} - **{todayGXP:,}** Guild Experience | {higherLower(x, member)}\n"
        elif x == 1:
            string = string + f":second_place: {member} - **{todayGXP:,}** Guild Experience | {higherLower(x, member)}\n"
        elif x == 2:
            string = string + f":third_place: {member} - **{todayGXP:,}** Guild Experience | {higherLower(x, member)}\n"
        else:
            string = string+f"{x + 1}. {member} - **{todayGXP:,}** Guild Experience | {higherLower(x, member)}\n"
    return string



def totalGXP(day="none"):
    guildData = guildGXP()
    todayGXP = 0
    yesterdayGXP = 0
    for x in range(len(weeklyGXP_RAW)):
        todayGXP = todayGXP+guildData[x]["gxp"]["today"]
        yesterdayGXP = yesterdayGXP+guildData[x]["gxp"]["yesterday"]
    if day == "today":
        return f"{todayGXP:,}"
    elif day == "yesterday":
        return f"\n{yesterdayGXP:,}"
    if todayGXP > yesterdayGXP:
        return f"**{todayGXP:,}**\n({round(todayGXP/yesterdayGXP*100, 2)}% <:green_arrow_up:710198079701123113>)"
    elif todayGXP < yesterdayGXP:
        return f"**{todayGXP:,}**\n({round(todayGXP/yesterdayGXP*100, 2)}% <:red_arrow_down:710198080703561920>)"
    else:
        return f"\n{todayGXP:,}\n <:gray_arrow_forward:711009453704740906>"

#print(totalGXP("today"))
#print(totalGXP("yesterday"))
#print(totalGXP())
formatedList()
totalGXP()
