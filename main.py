def arr():
    nums = input(enter numbers -> )
    nums = [int(i) for i in arr]
    nums_sum = 0
    for i in nums:
        nums_sum += i
    mean = nums_sum / Len(nums)
    return f'Sum = {nums_sum}, Arithmetical mean = {mean}'
arr()