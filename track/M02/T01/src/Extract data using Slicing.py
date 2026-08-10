word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = [first, second, third]
record = (first, second, third)

# Slice the string, list and tuple
sliced_word = word[1:-1]
sliced_list = numbers[:2]
reversed_tuple = record[::-1]

print("Middle:", sliced_word)
print("First Two:", sliced_list)
print("Reversed Tuple:", reversed_tuple)