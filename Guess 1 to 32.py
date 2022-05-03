n = 5
allowed_range = 2 ** n

start = 1
end = allowed_range
mid = (start + end) // 2

first_question = input("Is your number greater than " + str(mid) + "? (y/n) ")

if first_question == "y":
    start = mid
    mid = (start + end) // 2
else:
    end = mid
    mid = (start + end) // 2

second_question = input("Is your number greater than " + str(mid) + "? (y/n) ")

if second_question == "y":
    start = mid
    mid = (start + end) // 2
else:
    end = mid
    mid = (start + end) // 2

third_question = input("Is your number greater than " + str(mid) + "? (y/n) ")

if third_question == "y":
    start = mid
    mid = (start + end) // 2
else:
    end = mid
    mid = (start + end) // 2

fourth_question = input("Is your number greater than " + str(mid) + "? (y/n) ")

if fourth_question == "y":
    start = mid
    mid = (start + end) // 2
else:
    end = mid
    mid = (start + end) // 2

fifth_question = input("Is your number greater than " + str(mid) + "? (y/n) ")

if fifth_question == "y":
    print("Your number is " + str(mid + 1) + ".")
else:
    print("Your number is " + str(mid) + ".")