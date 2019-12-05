# 6 digits
# within puzzle range
# two adj digits are the same
# digits always increase left to right
import re


def is_adjacent(num, num_re):
    num_set = set(num)
    # print(num_set)
    for x in num_set:
        # print(f'Checking {x}')
        num_checks = [
            re.compile(x + '{6}'),
            re.compile(x + '{5}'),
            re.compile(x + '{4}'),
            re.compile(x + '{3}'),
            re.compile(x + '{2}')
        ]

        for check in num_checks:
            y = check.search(num)
            if y:
                # print(y[0])
                if len(y[0]) > 2:
                    # print(f'too many {x}')
                    break
                elif len(y[0]) == 2:
                    return True

    return False


def is_increasing(num):
    
    for i in range(0, len(num)-1):
        if num[i] > num[i+1]:
            return False
    
    return True

num_re = re.compile(r'\d{2}|\d{3}|\d{4}|\d{5}|\d{6}')

lower = 109165
upper = 576723
cnt = 0

for num in range(lower, upper + 1):
    if is_adjacent(str(num), num_re) and is_increasing(str(num)):
        cnt += 1

print(cnt)