'''
@Author: Nikita Rai
@Date: 2021-08-05 07:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-06 06:10:00
@Title : Employee Wage Computation 
'''

import random
print("Welcome in Employee Wage Computation")
ISPARTTIME = 1
ISFULLTIME = 2
EMP_RATE_PER_DAY = 20 
randomCheck = random.randint(1,3)
if ( ISPARTTIME == randomCheck ) :
   EMPHRS = 4
   print("Employee Hours =" , EMPHRS ) 
elif (ISFULLTIME == randomCheck) :
   EMPHRS = 8
   print("Employee Hours =" , EMPHRS ) 
else:
   EMPHRS = 0
   print("Employee is absent")
salary = (EMP_RATE_PER_DAY * EMPHRS)

print ("part time or full time salary of employee " ,salary)
