# def mysterious_function(n):
#     if n <= 1:
#         return 1
#     return n * mysterious_function(n - 1)
# x=mysterious_function(4)
# print(x)


def mysterious_function(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result