# import random
# names = ["Sanjana", "Rohit", "Anjali", "Vikram", "Priya"]
# student_scores = {name: random.randint(0, 100) for name in names}
# print(student_scores)

# passed_students = {name: score for name, score in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_count = {word: len(word) for word in sentence.split()}
# print(word_count)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: (temp_c * 9/5) + 32 for day, temp_c in weather_c.items()}
# print(weather_f)

#syntax of dictionary comprehension
# new_dict = {key: value for item in iterable if condition}

#syntx of dictionary comprehension with pandas dataframe
# new_dict = {key: value for (index, row) in df.iterrows() if condition}

student_dict = {
    "student": ["Sanjana", "Rohit", "Anjali", "Vikram", "Priya"],
    "score": [85, 92, 78, 88, 95]
}

import pandas 

student_df = pandas.DataFrame(student_dict)
# print(student_df)
for (index, row) in student_df.iterrows():
    print(row)
    print(row.student)
    print(row.score)

passed_students = {row.student: row.score for (index, row) in student_df.iterrows() if row.score >= 80}
print(passed_students)