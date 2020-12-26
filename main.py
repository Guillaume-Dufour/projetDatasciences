from Traffic import *
from ConstructeurCSV import *

"""
dropLine("data.csv", "constructedData.csv")
dropColumn("constructedData.csv", "constructedData.csv")
addYear("constructedData.csv", "constructedData.csv")
addHour("constructedData.csv", "constructedData.csv")
addWeekDay("constructedData.csv", "constructedData.csv")
addMonth("constructedData.csv", "constructedData.csv")
"""

dataFrame = pandas.read_csv("constructedData.csv", sep=',', low_memory=False)
weeklyTraffic(dataFrame)
yearTraffic(dataFrame)
monthTraffic(dataFrame, 2001)
hourTraffic(dataFrame)
