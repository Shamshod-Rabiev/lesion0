my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = []
s = 0
while s < len(my_list):
    if my_list[s] > 0:
        a.append(my_list[s])
    elif my_list[s] < 0:
        break
    s = s + 1
print(a)