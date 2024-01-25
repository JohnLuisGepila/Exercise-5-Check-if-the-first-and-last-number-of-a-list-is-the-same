def is_first_and_last_same(numbers):
    print("Give a set of numbers:", numbers)

    first_number = numbers[0]
    last_number = numbers [-1]

    if first_number == last_number:
        return True
    else:
        return False
    
first_set = [50,40,30,20,10]   
print("result is", is_first_and_last_same(first_set ))
second_set = [10,20,30,40,10]
print("result is", is_first_and_last_same(second_set))