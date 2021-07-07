def toString(data: str):
    # function to convert list to string
    string_value = ''

    for value in data:
        string_value += value
    return string_value


def format_number(value: str):
    list_seperated_values = []
    seperated_to_string = ''

    if len(value) > 3:
        list_value = list(value)

        while len(list_value) > 3:
            list_seperated_values.insert(0, list_value[-3:])
            del list_value[-3:]

        print(F"First value: {list_value}\nSecond value: {list_seperated_values}")

        for lst in list_seperated_values:
            seperated_to_string += F"{toString(lst)},"

        print(F"Seperated value: {seperated_to_string}")

        formatted_value = F"{toString(list_value)},{seperated_to_string.rstrip(',')}"
        print(F"Formatted: {formatted_value}")
    
    else:
        print(value)

format_number('1232344')
# toString(['1','2','3','4','5'])