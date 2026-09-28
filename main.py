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

def main():
    print(findLength([1,2,3,4,2,3]))


if __name__ == '__main__':
    main()
