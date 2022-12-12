from math import sqrt

for number in range(185311, 185331):
    dividers_list = []
    for divider in range(1, int(sqrt(number)) + 1):
        if number % divider == 0:
            dividers_list.append(divider)
    if len(dividers_list) == 4:
        print(number, dividers_list)
