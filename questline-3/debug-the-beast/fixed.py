def second_largest(arr):
    
    largest = second =float()
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float() else none



n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

output=second_largest(arr)
print("second largest:",output)

