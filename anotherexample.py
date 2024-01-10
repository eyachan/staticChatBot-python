from string import ascii_lowercase
double_alphabet_values = list (ascii_lowercase)
new_list =[]
for i in double_alphabet_values:
    i = str(i+i)
    new_list.append(i)
double_alphabet  = dict(zip(double_alphabet_values, new_list))
print(double_alphabet)