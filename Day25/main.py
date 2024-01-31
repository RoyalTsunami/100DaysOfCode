# import csv

# with open(file="Day25\weather-data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = row[1]
#             temperatures.append(int(temp))
#     print(temperatures)

import pandas

data = pandas.read_csv("Day25\weather-data.csv")
print(data["temp"])
