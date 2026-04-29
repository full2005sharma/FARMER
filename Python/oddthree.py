def count_odd_three_digit_nums(nums):
    c = 0
    for num in nums:
        if num is None:
            continue

        if len(str(abs(num))) == 3 and num % 2 != 0:
            c += 1
    return c
print(count_odd_three_digit_nums([123,-211,None,22]))