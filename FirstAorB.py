
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Implement your solution here
    last_index_a = 0
    last_index_b = 100

    count_a = S.count('a')
    count_b = S.count('b')

    if count_a + count_b < 1:
        return False
    if len(S) < 1 or len(S) > 3*10**5:
        return False

    for idx, i in enumerate(S):
        if i == 'a':
            last_index_a = idx
        if i == 'b':
            last_index_b = idx

    # print(last_index_a, last_index_b)
    if last_index_a > last_index_b:
        return False

    return True
print(solution('aabbb'))
print(solution('ba'))
print(solution('aaa'))
print(solution('b'))
print(solution('abba'))
