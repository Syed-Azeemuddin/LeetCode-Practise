#return list of even numbers then odd numbers

def listGen(a_list):
    left = 0
    right = len(a_list) - 1

    while left < right:
        while (a_list[left] %2 == 0 and left < right):
            left += 1
        while (a_list[right] %2 == 1 and left < right):
            right -= 1
        if left < right:
            a_list[left], a_list[right] = a_list[right], a_list[left]
            left += 1
            right -= 1
    return a_list
            


print(listGen([1,2,3,4,5,6,7,8,9,10]))