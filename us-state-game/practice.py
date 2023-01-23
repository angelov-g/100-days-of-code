# with open("weather_data.csv") as weather_data:
#     data_list = weather_data.readlines()
#
# print(data_list)
#
# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()

temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# average = data["temp"].mean()
max_temp = data["temp"].max()
# print(max_temp)


# Data in columns
# print(data["condition"])
# print(data.condition)

# Data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp*1.8) + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")