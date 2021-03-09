def main():
    l = 100
    for i in range(l):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        elif i % 3 == 0:
            print("Fizz")
            continue
        print(i)
main()
