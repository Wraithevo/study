calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    str_info = len(string), string.upper(), string.lower()
    count_calls()
    return str_info


def is_contains(string, list_to_search):
    count_calls()
    for i in range(0, len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    in_list = string.lower() in list_to_search
    return in_list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
