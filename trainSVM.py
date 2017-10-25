import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

f=open("output.txt", "r")
ftest = open("outputTest3.txt", "r") 
label = open("ear_coordinate.txt","r")
testX = open("TestLabel_X.txt","w")
testY = open("TestLabel_Y.txt","w")

lines = f.readlines()

#training feature vectors
leftEarY =  []
rightEarY = []
leftEarX =  []
rightEarX = []

#test feature vectors
leftEarYTest =  []
rightEarYTest = []
leftEarXTest =  []
rightEarXTest = []

#training labels
x_label = []
y_label = []

flag = 0

#for the training video
for line in lines:
    if flag==0:
	flag=1
	continue
    else:
        leX = []
        reX = []
	leY = []
	reY = []
        z = line.replace(',',' ').split()
        z = [float(i) for i in z]

        for i in range (3,6):
            leX.append(z[i])
        
        for i in range (0,3):
            reX.append(z[i])
 
	for i in range (9,12):
            leY.append(z[i])
        
        for i in range (6,9):
            reY.append(z[i])
       
        leftEarX.append(leX)
        rightEarX.append(reX)
	leftEarY.append(leY)
        rightEarY.append(reY)

#for the test video
flag = 0
lines = ftest.readlines()
for x in lines:
    if flag==1:
        leX = []
        reX = []
	leY = []
	reY = []
        z = x.replace(',',' ').split()
        z = [float(i) for i in z]

        for i in range (3,6):
            leX.append(z[i])
        
        for i in range (0,3):
            reX.append(z[i])
 
	for i in range (9,12):
            leY.append(z[i])
        
        for i in range (6,9):
            reY.append(z[i])
       
        leftEarXTest.append(leX)
        rightEarXTest.append(reX)
	leftEarYTest.append(leY)
        rightEarYTest.append(reY)
    else:
        flag=1

#for training label vectors
lines = label.readlines()
flag = 0
for  line in lines:
    if flag == 0:
	flag=1
	continue
    x_label.append(line.split()[0])
    y_label.append(line.split()[1])

#svr training x model
classifier_x = SVR(kernel = 'linear', C=0.001)
classifier_x.fit(leftEarX, x_label)

#svr training y model
classifier_y = SVR(kernel = 'linear', C=0.001)
classifier_y.fit(leftEarY, y_label)

#prediciting test labels
x_lin = classifier_x.predict(leftEarXTest)
y_lin = classifier_y.predict(leftEarYTest)

for i in x_lin:   
    testX.write(str(i))
    testX.write('\n')

for i in y_lin:   
    testY.write(str(i))
    testY.write('\n')

#plotting svm curve
lw = 1
plt.scatter(y_label, x_label, color='darkorange', label='data')
#plt.plot(x_label, x_lin, color='c', lw=lw, label='Linear model')
#plt.plot(y_label, y_lin, color='m', lw=lw, label='Linear model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

