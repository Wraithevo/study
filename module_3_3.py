def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [False, 37.52, 'list']
values_dict = {'a': True, 'b': 'dict', 'c': 3.3}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [39.47, 'second list']
print_params(values_list_2, 42)
