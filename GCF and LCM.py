def gcf():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    remainder = int(num1) % int(num2)
    while remainder != 0:
        num1 = num2
        num2 = remainder
        remainder = int(num1) % int(num2)
    print(str(int(num2)) + " is the greatest common factor.")


def lcm():
    num1 = input("Please enter the first number: ")
    num2 = input("Please enter the second number: ")
    pre_lcm = int(num1) * int(num2)
    remainder = int(num1) % int(num2)
    while remainder != 0:
        num1 = num2
        num2 = remainder
        remainder = int(num1) % int(num2)
    gcf = num2
    final_lcm = int(pre_lcm) / int(gcf)
    print(str(int(final_lcm)) + " is the least common multiple.")

user_choice = input("Would you like to find the GCF or the LCM? ")

if user_choice.upper() == "GCF":
    gcf()
elif user_choice.upper() == "LCM":
    lcm()
else:
    print("Please try again.")
