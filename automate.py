import os

sol = '/Users/aaditya.prabu_int/Desktop/Files/IDFC-FB-Assignment-1/Day 1/Part 2/Solution.py'

content = ''
with open(sol) as file:
    content = file.read()

for day in range(4,26):
    day_path = './Day'+str(day)
    os.mkdir(day_path)
    for part in range(1,3):
        part_path = day_path + '/Part' +str(part)
        os.mkdir(part_path)
        with open(part_path+ '/Solution.py','w') as file:
            file.write(content)
        with open(part_path+ '/input.txt','w') as file:
            file.write(' ')
        with open(part_path+ '/output.txt','w') as file:
            file.write(' ')
         
