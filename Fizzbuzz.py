def main():
    end = 100 #Defined a variable to hold the maximum number that we want to fizzbuzz

    #A for loop to iterate over every number until we hit the targeted variable above
    for num in range(end):
        #Some logic pertaining if the number is divisible by 3, 5, or none
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
            continue
        elif num % 5 == 0:
            print("Buzz")
            continue
        elif num % 3 == 0:
            print("Fizz")
            continue
        #If neither of these cases are hit, just print the number
        print(num)
main()
