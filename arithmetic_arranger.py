def arithmetic_arranger(problems, sum = False):
#This checks the number of input problems
  if len(problems) > 5 :
    print('Error: Too many problems.')
    exit()

#Initialization of lists
  foper = list()
  soper = list()
  opera = list()

#Spliting the operands in the problems  
  for problem in problems:
    problem.lstrip()
    problem.rstrip()
    sproblem = problem.split(" ")
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      print('Error: Numbers cannot be more than four digits.')
      exit()
    if not (sproblem[1] == '+' or sproblem[1] == '-'):
      print('Error: Operator must be \'+\' or \'-\'.')
      exit() 
    foper.append(sproblem[0])
    opera.append(sproblem[1])
    soper.append(sproblem[2])

  return arranged_problems