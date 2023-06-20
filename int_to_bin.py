"""
If you need binary from an integer this is you script.
additional, will obtain the gaps... a gaps is a numbers of 0 units closed inside 1 number
"""

def solution(N):
    quantity_of_gabs =0
    size_of_gabs = 0
    binary = bin(N)[2:]
    list_of_ceros = binary.split("1")
    for idx, i in enumerate(list_of_ceros):
        if len(list_of_ceros) -1 == idx:
            continue
        if "0" in i:
            if size_of_gabs < len(i):
                size_of_gabs = len(i)
            quantity_of_gabs +=1

    
    if quantity_of_gabs == 0:
        size_of_gabs = 0


    print(N)
    print(binary)
    print(quantity_of_gabs)
    print(size_of_gabs)
    print("·························")

    
solution(1041)
    
solution(32)
    
solution(9)
    
solution(529)
    
solution(200)

solution(12345)

solution(1041)

