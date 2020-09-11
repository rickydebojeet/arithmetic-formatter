# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main

#Initialisation of variables
arithmetic_exp = list()

#Taking input
while True:
  exp = input('Please enter your arithmetic expression: ')
  exp = str(exp)
  arithmetic_exp.append(exp)
  check = input('Do you want to continue? y or n : ')
  if check == 'n':
    break

print('Aranging...')
condition = input('Do you want the result to be shown? y or n : ')

if condition == 'y':
  condition = True
else:
  condition = False

print(arithmetic_arranger([arithmetic_exp, condition]))



# Run unit tests automatically
main(module='test_module', exit=False)