# print("this is a debug message")

def solution(N):
    alpha__dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    response = ''
    # Implement your solution here
    if N <= 1:
        return 'a'
    string = 'a' * N

    for idx, i in enumerate(alpha__dic):

        count_len = len(alpha__dic)
        if idx == count_len -1:
            return string
        string_to_search = i * 2
        string_for_replace = alpha__dic[idx +1]
        # print(string_to_search)
        # print(string_for_replace)

        string = string.replace(string_to_search, string_for_replace)
    return string
            
        

print(solution(11))
print(solution(1))
print(solution(67108876))