def arithmetic_arranger(problems, con = False):
  #This checks the number of input problems
  if len(problems) > 5 :
    print('Error: Too many problems.')
    exit()

  #Initialization of lists, strings
  foper = list()
  soper = list()
  opera = list()
  res = list()
  fline = str()
  sline = str()
  tline = str()
  aline = str()


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

  #The arithmetic operations
  counter = 0
  while counter < len(problems):
    try:
      a = int(foper[counter])
      b = int(soper[counter])
    except:
      print('Error: Numbers must only contain digits.')
      exit()
    if opera[counter] == '+':
      res.append(str(a + b))
    elif opera[counter] == '-':
      res.append(str(a - b))
    
    #Finding the width of longest operand
    long = max(len(foper[counter]), len(soper[counter]))

    #Creation of first line
    fline = fline + foper[counter].rjust(long + 2) + '    '

    #Creation of second line
    sline = sline + opera[counter] + ' ' + soper[counter].rjust(long + 1) + '    '

    #Creation of third line
    for val in range(long + 2):
      tline = tline + '-'
    tline = tline + '    '

    #Creation of fourth line
    aline = res[counter].rjust(long + 2) + '    '

    counter = counter + 1

  #Final output
  fline = fline.strip()
  sline = sline.strip()
  tline = tline.strip()
  aline = aline.strip()
  if con == False:
    arranged_problems = fline + '\n' + sline + '\n' + tline
  elif con == True:
    arranged_problems = fline + '\n' + sline + '\n' + tline + '\n' + aline
  
  return arranged_problems