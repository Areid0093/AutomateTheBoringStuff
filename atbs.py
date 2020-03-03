## Collatz Sequence
def collatz(number):
    if number%2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return (3 * number + 1)
        


answer = int(input('Please enter an integer greater than 0: '))

while answer != 1:
    answer = collatz(answer)


## Insert/Join comma_code
user_list = ['apples', 'bananas', 'tofu', 'cats']
    
def comma_code(user_list):
    return '{}, and {}'.format(', '.join(user_list[:-1], user_list[-1]))

## Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print('\n'.join(map(''.join, zip(*grid))))

##
