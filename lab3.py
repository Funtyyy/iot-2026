def unpaired(numbers):
    for num in numbers:
        if -num not in numbers:
            return num


print(unpaired([1, -1, 2, -2, 3]))       
print(unpaired([-3, 1, 2, 3, -1, -4, -2]))  
print(unpaired([1, -1, 2, -2, 3, 3]))    
    
    