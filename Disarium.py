# Checking the disarium number
def is_disarium(num):
    str_num = str(num)
    total = 0
    for i in range(len(str_num)):
        digit = int(str_num[i])
        total += digit ** (i + 1)
    return total == num
# first n disarium numbers
def first_n_disarium(n):
    count = 0
    num = 0
    while count < n:
        if is_disarium(num):
            print(num, end=' ')
            count += 1
        num += 1
    print()
# printing disarium between 2 numbers.  
def disarium_in_range(start, end):
    for num in range(start, end + 1):
        if is_disarium(num):
            print(num, end=' ')
    print()
print("First 10 Disarium numbers:")
first_n_disarium(10)

print("\nDisarium numbers between 100 and 200:")
disarium_in_range(100, 200)
