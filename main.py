# remember to fork this and push to github

#file objects
# f = open('test.txt', 'r')

# print(f.readlines())

# f.close()


# with open('test.txt', 'r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')

# employee_file = open("employees.txt", "r")

# for employee in employee_file.readlines():
  
#   print(employee)

# employee_file.close()

with open('readme.txt', 'w') as f:
  f.write('readme')

with open('readme.txt', 'w') as f:
  f.write('i dont care')

with open('readme.txt', 'a') as f:
  f.write('i dont care 3xxxx')

#create a file through python code
#get it to accept user input
#to append to the content

with open('mateo', 'w') as f:
  input = input("type your message: ")
  f.write(input)

  