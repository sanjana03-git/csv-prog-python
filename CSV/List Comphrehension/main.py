numbers = [1, 2, 3, 4, 5]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Sanjana"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num*2 for num in range(1, 5)]
print(range_list)

names = ["Sanjana", "Ananya", "Rohan", "Priya"]
first_letter = [name[0] for name in names]
short_names = [name for name in names if len(name) <= 5]
print(first_letter)
print(short_names)

even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)

squared_numbers = [num**2 for num in range(1, 6)]
print(squared_numbers)


overlap = [num for num in range(1, 10) if num % 2 == 0 and num % 3 == 0]
print(overlap)


#syntx of list comprehension
# new_list = [expression for item in iterable if condition]