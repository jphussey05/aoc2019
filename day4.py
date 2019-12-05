# 6 digits
# within puzzle range
# two adj digits are the same
# digits always increase left to right

def is_adjacent(num):

    for i in range(0, len(num)-1):
        if num[i] == num[i+1]:
            return True

    return False

def is_increasing(num):
    
    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            return False
    
    return True


lower = 109165
upper = 576723
cnt = 0

for num in range(lower, upper + 1):
    if is_adjacent(str(num)) and is_increasing(str(num)):
        cnt += 1

print(cnt)