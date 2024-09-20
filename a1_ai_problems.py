# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

#first problem

print("hello world")

separator = " - "
string_list = ["apple", "banana", "cherry", "date"]

result = separator.join(string_list)
print(result)


my_list = [1, 2, 3, "apple", "banana", 3.14]
print(my_list)  


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("Welcome to 'Guess the Number'!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")

if __name__ == "__main__":
    guess_the_number()



def sum_list(numbers):
    return sum(numbers)

my_list = [1, 2, 3, 4, 5]
print("Sum:", sum_list(my_list))




