# You can remove 'pass' if you written code in the function
# Exercise 1

def find_closest(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid  # found
        elif data[mid] < target:
            low = mid + 1  # target is in the right half
        else:
            high = mid - 1  # target is in the left half
    return data[mid]

# Exercise 2
def integer_sqrt(n):
    # Write your code here
    pass

