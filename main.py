def findLength(nums):
    if not nums:
        return 0
    current_len = 1
    max_len = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            current_len += 1
        else:
            current_len = 1

        max_len = max(current_len, max_len)

    return max_len

def numberOfLines(widths, s):
    lines = 1
    curr_w = 0
    for symbol in s:
        symbol_width = widths[ord(symbol) - ord('a')]
        if curr_w + symbol_width > 100:
            lines += 1
            curr_w = symbol_width
        else:
            curr_w += symbol_width
    return [lines, curr_w]


def main():
    print(findLength([1,2,3,4,2,3]))


if __name__ == '__main__':
    main()
