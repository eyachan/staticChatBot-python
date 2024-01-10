min_len_input = 100
general_user_input = ''
while len(general_user_input) < 100:
    user_input = input('Print a random string containing 0 or 1:')
    user_input = ''.join([letters for letters in user_input if letters in ['0', '1']])
    general_user_input += user_input
    char_left = max(100 - len(general_user_input), 0)
    print(f'Current data length is {len(general_user_input)}, {char_left} symbols left')
print(f'Final data string: {general_user_input}')