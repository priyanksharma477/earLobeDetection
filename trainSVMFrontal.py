import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

f=open("output.txt", "r")
ftest = open("outputTest6.txt", "r")
label = open("ear_coordinate_frontal.txt","r")
testXleft = open("TestLabel_XL.txt","w")
testYleft = open("TestLabel_YL.txt","w")
testXright = open("TestLabel_XR.txt","w")
testYright = open("TestLabel_YR.txt","w")

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
x_label_left = []
y_label_left = []
x_label_right = []
y_label_right = []

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
    x_label_left.append(line.split()[0])
    y_label_left.append(line.split()[1])
    x_label_right.append(line.split()[2])
    y_label_right.append(line.split()[3])

#svr training xleft model
classifier_xl = SVR(kernel = 'linear', C=0.001)
classifier_xl.fit(leftEarX, x_label_left)

#svr training yleft model
classifier_yl = SVR(kernel = 'linear', C=0.001)
classifier_yl.fit(leftEarY, y_label_left)

#svr training xright model
classifier_xr = SVR(kernel = 'linear', C=0.001)
classifier_xr.fit(rightEarX, x_label_right)

#svr training yright model
classifier_yr = SVR(kernel = 'linear', C=0.001)
classifier_yr.fit(rightEarY, y_label_right)

#predicting test labels
x_lin_left = classifier_xl.predict(leftEarXTest)
y_lin_left = classifier_yl.predict(leftEarYTest)
x_lin_right = classifier_xr.predict(rightEarXTest)
y_lin_right = classifier_yr.predict(rightEarYTest)

for i in x_lin_left:   
    testXleft.write(str(i))
    testXleft.write('\n')

for i in y_lin_left:   
    testYleft.write(str(i))
    testYleft.write('\n')

for i in x_lin_right:   
    testXright.write(str(i))
    testXright.write('\n')

for i in y_lin_right:   
    testYright.write(str(i))
    testYright.write('\n')

#plotting svm curve
lw = 1
#plt.scatter(y_label, x_label, color='darkorange', label='data')
#plt.plot(x_label, x_lin, color='c', lw=lw, label='Linear model')
#plt.plot(y_label, y_lin, color='m', lw=lw, label='Linear model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

