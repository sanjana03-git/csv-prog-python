# import csv

# with open("CSV/weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data:
#         print(row)
#         temperature.append(int(row[1]))

# print(temperature)

import pandas   
data = pandas.read_csv("CSV/weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# avg = sum(temp_list) / len(temp_list)
# print(avg)

# print(data["temp"].max())
# print(data["temp"].min())
# print(data["temp"].mean())

# Get data in columns
# print(data["condition"])
# print(data.condition)
# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("CSV/new_data.csv", index=False//)

import pandas
data = pandas.read_csv("CSV/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
data = pandas.DataFrame(data_dict)
data.to_csv("CSV/squirrel_count.csv", index=False)