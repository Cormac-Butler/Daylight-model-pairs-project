from datetime import datetime
import numpy as np
from astral import LocationInfo
import pytz
from astral.sun import sunrise, sunset
from datetime import date, timedelta
import matplotlib.pyplot as plt

def daylightLength(day, latitude):

    theta = np.radians(latitude)

    delta = np.radians(23.44)*np.sin((2*np.pi*(day - 78.37569444444445))/365.25)

    angle = np.arccos(max(min(-np.tan(theta) * np.tan(delta), 1), -1))

    dayLength = 24 * angle / np.pi
    
    return dayLength

def daysSinceSelectedDatetime(date):

    startOfYear = "01-01-2025"

    selectedDate = datetime.strptime(startOfYear, "%d-%m-%Y")
    
    currentDate = datetime.strptime(date, "%d-%m-%Y")
    
    timeDifference = (currentDate - selectedDate).total_seconds()
    
    daysDifference = timeDifference / 86400
    
    return daysDifference

def convert(hours):

    totalMinutes = round(hours * 60)

    h, m = divmod(totalMinutes, 60)

    return f"{h} hours and {m} minutes"

def trueValue():

    city = LocationInfo("Belfast", "Northern Ireland", "Europe/London", 54.5973, -5.9301)
    timezone = pytz.timezone(city.timezone)

    startDate = date(2025, 1, 1)
    endDate = date(2025, 12, 31)
    delta = timedelta(days=1)

    data = []
    dayNumber = 1
    while startDate <= endDate:
        sr = sunrise(city.observer, date=startDate, tzinfo=timezone)
        ss = sunset(city.observer, date=startDate, tzinfo=timezone)
        daylight_duration = (ss - sr).seconds / 3600
        data.append(daylight_duration)
        startDate += delta
        dayNumber += 1

    return data

if __name__ == "__main__":

    targetDate = "20-03-2024"

    latitude = 54.5973           # Belfast is 54.5973°


    day = daysSinceSelectedDatetime(targetDate)
    day_length = daylightLength(day, latitude)

    print(f"On the {targetDate} at {latitude}°N:\n")
    print(f"Day Length: {convert(day_length)}\n")