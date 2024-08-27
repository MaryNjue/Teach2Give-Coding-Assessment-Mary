def filterEvenNumbersFromWord(word):
    digits = [int(char) for char in word if char.isdigit()]
    even_numbers = [num for num in digits if num % 2 == 0]
    return even_numbers
user_input = input("Please enter a word containing digits: ")
filtered_evens = filterEvenNumbersFromWord(user_input)
print(f"The even numbers extracted from the input are: {filtered_evens}")

