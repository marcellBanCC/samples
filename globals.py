value = 0


def incorrect_global_setter():
    value = 10


def correct_global_setter():
    global value
    value = 12


def print_global():
    print(value)


print_global()
incorrect_global_setter()
print_global()
correct_global_setter()
print_global()
