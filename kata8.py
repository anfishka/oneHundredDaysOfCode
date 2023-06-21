def find_average(numbers):
    i = 0
    if len(numbers) == 0:
        return 0
    for j in numbers:
        i = i + j
    res = i / len(numbers)
    print(res)
    return res

 # test.assert_equals(find_average([1, 2, 3]), 2)

find_average([1, 2, 3])
find_average([1, 2, 3, 1, 8])
find_average([1, 2, 3, 5,9,12])



#new task

def number_to_string(num):
    return str(num)

#4th
def add_length(str_):
    modified_arr = []
    words = str_.split()
    for word in words:
        modified_arr.append(word + " " + str(len(word)))
    print(modified_arr)
    return modified_arr


add_length(["aaa", "bbb"])

def multiply_and_increase(value):
    if isinstance(value, str):
        return "Error"
    else:
        return value * 50 + 6

#6th BINARY TO DECIMAL WITH RECURSION
#1st variant
def bin_to_decimal(bin):
        if len(bin) == 0:
            return 0
        else:
            significant_bit = int(bin[-1])
            remain_bits = bin[:-1]
            dec = bin_to_decimal(remain_bits)
            return dec * 2 + significant_bit

def res(bin):
    result = bin_to_decimal(bin)
    return result

#2nd variant
def bin_to_decimal(bin):
    return int(bin, 2)


#7th task - How good are you really?
def better_than_average(class_points, your_points):
    average_class = 0
    
    if class_points != 0:
        for i in class_points:
            average_class += i
        if average_class / len(class_points) >= your_points:
            return False
        else:
            return True
    else:
         return  

