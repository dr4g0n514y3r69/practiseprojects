n = int(input("Choose a whole number greater than 2: "))
odd1 = int(((n ** 2) / 2) - 0.5)
odd2 = int(((n ** 2) / 2) + 0.5)
even1 = int(((n / 2) ** 2) - 1)
even2 = int(((n / 2) ** 2) + 1)
py_list = []


def triple_finder(num):
    if num < 3:
        print("Whole number must be greater than 2. Please try again.")
    else:
        if num % 2 == 0:
            py_list.extend([num, even1, even2])
        else:
            py_list.extend([num, odd1, odd2])
        py_list.sort()    
        first_side, second_side, third_side = str(py_list[0]), str(py_list[1]), str(py_list[2])
        print(f"One side is {first_side}. The other side is {second_side}. The hypotenuse is {third_side}.")
    

triple_finder(n)