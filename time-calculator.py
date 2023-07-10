def add_time(start, duration, day=""):
    # get start info
    startSplit = start.split(" ")
    startHour = int(startSplit[0].split(":")[0])
    startMins = int(startSplit[0].split(":")[1])
    theM = startSplit[1]
    if theM == "PM":
        startHour = startHour + 12

    # get duration info
    durationSplit = duration.split(":")
    durationHour = int(durationSplit[0])
    durationMins = int(durationSplit[1])

    

    finalHour = startHour + durationHour
    finalMins = startMins + durationMins
    finalTheM = "AM"

    if finalMins > 59:
        finalMins = finalMins - 60
        finalHour = finalHour + 1

    # in case days passed
    passDay = 0
    while finalHour > 23:
        finalHour = finalHour - 24
        passDay = passDay + 1

    if finalHour > 12:
        finalHour = finalHour - 12
        finalTheM = "PM"

    if finalHour == 12:
        finalTheM = "PM"

    if finalHour == 0:
        finalTheM = "AM"
        finalHour = 12

    if finalMins < 10:
        finalMins = f"0{finalMins}"
    
    daysMassege = ""
    if passDay == 1: 
        daysMassege = " (next day)"
    
    if passDay > 1:
        daysMassege = f" ({passDay} days later)"
    

# get day info
    numToDay = {
        "Sunday": 1, 
        "Monday": 2, 
        "Tuesday": 3,
        "Wednesday": 4, 
        "Thursday": 5,
        "Friday": 6,
        "Saturday": 7, 
        }
    startDay = day.capitalize()
    capDay = ""
    startDayNum = 0
    if startDay in numToDay:
        startDayNum = numToDay[startDay]
   
    
    startDayNum = startDayNum + passDay

    while startDayNum > 7:
        startDayNum = startDayNum - 7

    if day == "":
        capDay = ""
    else: 
        capDay = ", " + (list(numToDay.keys())[list(numToDay.values()).index(startDayNum)])

    return f"{finalHour}:{finalMins} {finalTheM}{capDay}{daysMassege}"


print(add_time("6:30 PM", "205:12", "thursday"))
