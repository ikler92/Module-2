import random
n = random.randint(3, 20)

def counter(random_number):
    password_number = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password_number += str(i) + str(j)
                print(i, ' ', j)
    return password_number

print('Число в первом поле', n)
print('Пароль для второго поля', counter(n))

