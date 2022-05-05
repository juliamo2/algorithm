# 三角形找最小值

triangle = [[3],
            [5, 8],
            [6, 2, 4],
            [2, 8, 6, 4],
            [4, 2, 6, 3, 5]]


# 状态转移方程
# dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

def minimumTotal(triangle):
    # 获取triangle的长度，也就是‘三角形’的高

    n = len(triangle)

    # 初始化dp为‘三角形’最后那一行

    dp = triangle[-1]

    # 从下(倒数第二层)到上

    for i in range(n - 2, -1, -1):

        # 更改dp前j个的值

        for j in range(i + 1):
            dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

    # 返回dp第一个值

    return print(dp[0])


minimumTotal(triangle)
