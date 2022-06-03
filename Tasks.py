# 1.	Найти НОК двух чисел

def search_for_the_greatest_common_divisor(num1, num2):
    num1, num2 = max(num1, num2), min(num1, num2)
    remainder = 1
    while (remainder != 0):
        remainder = num1 % num2
        num1, num2 = num2, remainder
    return num1


def search_for_the_lowest_common_multiple(num1, num2):
    return int((num1 * num2) / (search_for_the_greatest_common_divisor(num1, num2)))


number1 = 10
number2 = 15

print(f'НОК двух чисел {number1} и {number2} = {search_for_the_lowest_common_multiple(number1, number2)}')


#_______________________________________________________________________________________________________

# 2.	Вычислить число PI c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

# Try the Nilakantha series. 
# π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14) ⋯
from decimal import Decimal

accuracy = 0.001

pi_current = Decimal(3)
i = 2
count_steps = 1
pi_next = pi_current + Decimal(4 / (i * (i + 1) * (i + 2)))
plus_or_minus = Decimal(1)
accuracy_current = abs(pi_current - pi_next)

while accuracy_current >= accuracy:
    count_steps += 1
    i += 2
    pi_current = pi_next
    plus_or_minus = -plus_or_minus
    pi_next = pi_current + (plus_or_minus * 4) / Decimal((i) * (i + 1) * (i + 2)) 
    accuracy_current = abs(pi_current - pi_next)

print(f'По методу Нилаканта получена PI с точностью {accuracy}  = {pi_next} за {count_steps} итераций')

#____________________________________________________________________________________________

# 3.	Составить список простых множителей натурального числа N

def search_for_prime_multipliers(n):
    divider = 2
    multipliers_list = []

    while (divider <= n):
        while (n % divider == 0):
            multipliers_list.append(divider)
            n //= divider
        divider += 1
    return multipliers_list


N = 3572
print(f'Список простых множителей числа {N} = {search_for_prime_multipliers(N)}')

#__________________________________________________________________________________________________
# 4.	Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

numbers_list = [1, 2, 3, 5, 1, 5, 3, 10]
unique_numbers_list = set(numbers_list)

print(f'Уникальные элементы в списке {numbers_list} - {unique_numbers_list}')

#___________________________________________________________________________

# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 

import random

def create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator):
    with open(file_name, 'w') as data:
        for i in range(amount_of_numbers):
            sep = separator if i != amount_of_numbers - 1 else ""
            data.write(str(random.randint(min_value, max_value)) + sep)

def number_list_from_file(file_name, separator):
    with open(file_name, 'r') as data:
        list_numbers = list(map(int, data.read().split(separator)))
    return list_numbers

def delete_odd_numbers_from_list(list_numbers):
    return  [number for number in list_numbers if number % 2 == 0]

        
def write_odd_numbers_from_list(file_name, list_numbers, separator):
    with open(file_name, 'w') as data:
        data.write(separator.join(map(str, list_numbers)))
            
file_name = 'file.txt'
file_name_odd_numbers = 'odd_file.txt'
amount_of_numbers = 10
min_value = -7
max_value = 7
separator = " "
create_int_numbers_file(file_name, amount_of_numbers, min_value, max_value, separator)
list_numbers = number_list_from_file(file_name, separator)
list_numbers = delete_odd_numbers_from_list(list_numbers)
write_odd_numbers_from_list(file_name_odd_numbers, list_numbers, separator)
