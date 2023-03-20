import pandas

filepath = "C:/Programare/PythonProjects/Python Course Udemy/CSV/CSV1/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

data = pandas.read_csv(filepath)

colors = data.value_counts(subset = "Primary Fur Color").reset_index(name = "Count")

colors = pandas.DataFrame(colors)
colors.rename(columns = {"Primary Fur Color": "Fur Color"}, inplace = True)
colors.to_csv("CSV/CSV1/squirrel_count.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = str(len(data[data["Primary Fur Color"] == "Cinnamon"]))
black_squirrels_count = str(len(data[data["Primary Fur Color"] == "Black"]))

new_data = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_data = pandas.DataFrame(new_data)
new_data.to_csv("CSV/CSV1/squirrel_count2.csv")