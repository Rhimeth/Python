import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
data = np.genfromtxt('grades.txt', delimiter = ' ')
print(data)

f = open("grades.txt", "r")
f = open("gradeplot.py")
file.read()
grades = np.loadttxt("grades.txt", ",")
A = B = C = D = F = 0
    
Sum = 0
Number = 0

l_Sum = ();

grades = f.readline()
for letters in f:
        if grades >= 90:
            A += 1

        elif grades > 80 and grades < 90:
            B +=1

        elif grades > 70 and grades < 80:
            C +=1

        elif grades > 60 and grades < 70:
            D +=1

        elif grades > 60:
            F +=1

for line in data:
    print(line)
for line in range(len(data[0])):
    Sum = 0
    Number = 0
    for row in range(len(data)):
            Sum = Sum + data[line][row]
            Number +=1
print(l_Sum)
plt1.plot(data)
plot2.plot(l_Sum)
plt1.show()
plt2.show()

