calander = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12,
}

test = False
while test == False:
    date = input("What is the date?")
    if date[0].isalpha() == True:
        date = date.split(",")
        year = int((date[1]).strip())
        month_day = date[0].split(" ")
        day = int(month_day[1])
        month = month_day[0]
        month = calander[month]

    elif date[0].isalnum() == True:
        date = date.split("/")
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
    test = (day < 31) * (month < 12)

print(f"{year}-{month:02}-{day:02}")