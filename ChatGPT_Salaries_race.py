# -*- coding: utf-8 -*-

# importing matplotlib
import matplotlib.pyplot as plt
plt.rc('axes', titlesize=20)     
plt.rc('axes', labelsize=16)    
plt.rc('xtick', labelsize=16)   
plt.rc('ytick', labelsize=16)  
 
# making a simple plot
x =[1, 2, 3, 4]
y =[152273, 104688, 112308, 153611]
 
# creating error
y_error = [16556,14004,17836,19993]
 
# plotting graph
#plt.plot(x, y)

plt.errorbar(x, y,
             yerr = y_error,
             fmt ='o')
plt.ylabel('ChatGPT Assigned Salary')
plt.xlabel('Demographic')
labels = ['White','Black','Latinx','Asian']

plt.xticks(x, labels, rotation=45)
plt.savefig('output.png')

