"""teaching schedule"""
N = int(input())
A = int(input())
time = 0
time += A * N
if not time :
    print('No teaching')
elif time < 60 :
    print(f'{time} minute')
else:
    hour = time // 60
    minutes = time % 60
    if not hour:
        print(f'{minutes} minute')
    elif not minutes :
        print(f'{hour} hours')
    else:
        print(f'{hour} hours {minutes} minute')
