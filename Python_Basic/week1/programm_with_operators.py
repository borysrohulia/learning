import random

# variant 1

# control_num = 17
# def game():
#     input_num = input('введите число: ')
#     if input_num.isdigit() != True:
#         print('Пока')
#     elif int(input_num) == control_num:
#         print('совершенно верно! Вы угадали')
#     elif int(input_num) < control_num:
#         print('число больше')
#         game()
#     else:
#         print('число меньше')
#         game()

# game()

# variant 2

number = random.randint(0, 101)

while True:
    answer = input('Введите число: ')
    if not answer or answer == 'exit': 
        break

    if not answer.isdigit():
        print('введите правильное число!')
        continue
    if int(answer) > number:
        print('число меньше')
    elif int(answer) < number:
        print('число больше')
    else:
        print('Вы угадали!')
        break
