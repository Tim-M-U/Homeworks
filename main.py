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

def numIslands(grid):
    if not grid:
        return 0
    rows = len(grid)
    col = len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(col):
            if grid[r][c] == "1":
                islands += 1
                dfs(r,c)
    return islands

def main():
    print(numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


if __name__ == '__main__':
    main()
