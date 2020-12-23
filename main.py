from Traffic import *
from ConstructeurCSV import *

dropLine("data.csv", "constructedData.csv")
dropColumn("constructedData.csv", "constructedData.csv")
addYear("constructedData.csv", "constructedData.csv")
addHour("constructedData.csv", "constructedData.csv")
addWeekDay("constructedData.csv", "constructedData.csv")

weeklyTraffic("constructedData.csv")
yearTraffic("constructedData.csv")
