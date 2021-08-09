'''
@Author: Nikita Rai
@Date: 2021-08-05 07:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-06 06:10:00
@Title : Employee Wage Computation 
'''

import random
print("Welcome in Employee Wage Computation")
ISPRESENT = 1
randomCheck = random.randint(0, 1)
if ( ISPRESENT == randomCheck ) :
   print("Employee is present" ) 
   EMP_RATE_PER_DAY = 20 
   EMPHRS = 8 
   salary = int(EMP_RATE_PER_DAY * EMPHRS) 
   print ('Daily employee wage', salary)
else:
   print("Employee is absent")
   SALARY = 0