first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_results = [len(x) for x in first_strings if len(x) > 5]
second_results = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
third_results = [{x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}]

print(first_results)
print(second_results)
print(third_results)