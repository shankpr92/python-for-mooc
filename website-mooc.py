import matplotlib.pyplot as plt
#from openpyxl import load_workbook
import pandas as pd
from pandas import ExcelWriter
import collections
sheett=pd.read_excel("C:/Users/prana/Desktop/SNA/Project.xlsx")
#import xlsxwriter




timestamp = sheett['Timestamp']
Id = sheett['Id']
mooc = sheett['Which MOOC website do you prefer for online certification/learning?']

lmooc=list(mooc)


print(Id,lmooc[-1])
lmooc[-1].split(",")

k=1
for i in lmooc:
    l2 = []
    l2=i.split(",")
    #j=0
    #for j in l2:
    j=0
    while j < len(l2):
        print("--------",k,"========>",l2[j])
        #print(i.split(","))
        j=j+1
    k=k+1
    
    ##########################################################################
  
# part 2    

l3 = []
l4 = []

k=1

for i in lmooc:
    l2 = []
    l2=i.split(",")
    #j=0
    #for j in l2:
    j=0
    while j < len(l2):
        print("--------",k,"========>",l2[j])
        l3.append(k)
        l4.append(l2[j])
        #print(i.split(","))
        j=j+1
    k=k+1

'''
df = pd.DataFrame(l3)
df.to_excel("C:/Users/prana/Desktop/SNA/output.xlsx", header=False, index=False)


dff = pd.DataFrame(l4)
dff.to_excel("C:/Users/prana/Desktop/SNA/output.xlsx", header=False, index=False)
'''


df = pd.DataFrame({'Id':l3,
                   'Mooc':l4})
 
writer = ExcelWriter("C:/Users/prana/Desktop/SNA/output.xlsx")
df.to_excel(writer,'sheet1',index=False)
writer.save()







print(len(l3))

print(l4)





































### Ignore this

'''

plt.plot(listexperience,listsalary)


salaries_and_tenures	=	[(83000,8.7),(88000,8.1),(48000,0.7),(76000,6),(69000,6.5),(76000,7.5),(60000,2.5),(83000,	10), (48000,	1.9),	(63000,	4.2)]

salary_by_tenure	=	collections.defaultdict(list)

for salary,tenure in salaries_and_tenures:				
    salary_by_tenure[tenure].append(salary)



evennumbers = [x for x in range(10) if x%2==0]
print(evennumbers)





print(salary_by_tenure)

'''
