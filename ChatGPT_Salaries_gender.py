# -*- coding: utf-8 -*-

# importing matplotlib
import matplotlib.pyplot as plt
plt.rc('axes', titlesize=20)     
plt.rc('axes', labelsize=16)    
plt.rc('xtick', labelsize=16)   
plt.rc('ytick', labelsize=16)  
 
# making a simple plot
x =[1, 2]
y =[153077, 115417]
 
# creating error
y_error = [13258,13800]
 
# plotting graph
#plt.plot(x, y)

plt.errorbar(x, y,
             yerr = y_error,
             fmt ='o')
plt.ylabel('ChatGPT Assigned Salary')
plt.xlabel('Demographic')
labels = ['Male','Female']

plt.xlim([0.5,2.5])

plt.xticks(x, labels, rotation=45)
plt.savefig('output.png')

