# import csv

# with open(file="Day25\weather-data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temp = row[1]
#             temperatures.append(int(temp))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("Day25\weather-data.csv")
# print(data["temp"])
# print(type(data["temp"]))
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# print(data_dict)
# print(data_list)

# data_list = data["temp"].to_list()
# print(sum(data_list) / len(data_list))

# print(data["temp"].max())


# print(data[data.temp == data.temp.max()])


import pandas

data = pandas.read_csv("Day25\squirrel_data.csv")

fur_color_data = pandas.DataFrame(data["Primary Fur Color"].value_counts())

fur_color_data.to_csv("Day25\squirrel_count.csv")
