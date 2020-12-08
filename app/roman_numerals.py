def parse(s):
    # if s == 'I':
    #     return 1
    # elif s == 'II':
    #     return 2
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    for i in range(len(s)):
        curr_char = s[i]

        if i == len(s) - 1:
            total += nums[curr_char]
            return total

        next_char = s[i + 1]
        if curr_char not in nums:
            return 'invalid entry'
        if nums[curr_char] >= nums[next_char]:
            total += nums[curr_char]
        else:
            total -= nums[curr_char]
        print(curr_char, ':', next_char, ':', total)

    return total
