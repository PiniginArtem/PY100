num = 123
count = 0

num_changeable = num
while num_changeable != 1:
    if num_changeable % 2 == 0:
        num_changeable /= 2
    elif num_changeable % 2 == 1:
        num_changeable = (num_changeable * 3 + 1) / 2
    else:
        print('impossible!')
    count += 1

print(count)
