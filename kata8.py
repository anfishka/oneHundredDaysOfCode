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
