## Insert/Join comma_code
user_list = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(user_list):
    return '{}, and {}'.format(', '.join(user_list[:-1], user_list[-1]))