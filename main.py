def numbers_of_letters(n):
    def convert_num_to_let(num):
        n1_9 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        w_list = []
        for digit in str(num):
            w_list.append(n1_9[int(digit)])
        return ''.join(w_list)

    res = []

    while True:
        word = convert_num_to_let(n)
        res.append(word)
        if len(word) == n:
            print(res)
            return res
        n = len(word)




# test.assert_equals(numbers_of_letters(1), ["one", "three", "five", "four"])
# 2
# test.assert_equals(numbers_of_letters(12), ["onetwo", "six", "three", "five", "four"])
# 3
# test.assert_equals(numbers_of_letters(37), ["threeseven", "onezero", "seven", "five", "four"])
# 4
# test.assert_equals(numbers_of_letters(311), ['threeoneone', 'oneone', 'six', 'three', 'five', 'four'])
# 5
# test.assert_equals(numbers_of_letters(999), ["nineninenine", "onetwo", "six", "three", "five", "four"]

numbers_of_letters(1)
numbers_of_letters(12)
numbers_of_letters(37)
numbers_of_letters(311)
numbers_of_letters(999)