def stars_horizontal(x):
    answer = ''
    for i in range(x):
        answer += '*'
    answer=answer.center(5)
    return answer

def stars_vertical(x):
    for i in range(x):
     print('*')


print(stars_horizontal(5))
print(stars_vertical(5))

