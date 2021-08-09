'''
@Author: Nikita Rai
@Date: 2021-08-05 07:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-06 06:10:00
@Title : Employee Wage Computation 
'''
import random

ISPARTTIME = 1
ISFULLTIME = 2
EMP_RATE_PER_HR = 20
TOTAL_SALARY = 0
NUM_OF_WORKING_DAYS = 20
for day in range(1,NUM_OF_WORKING_DAYS):
   empCheck = random.randint(1, 3)
def wage(empCheck):
   '''
   Description:
     name of the function is wage which is use for switcher to return the desired value
   Parameter:
      empCheck is the parameter which i passed in this random value will be stored
   Return:
       Returning the value according to the attendance
   '''
   switcher = {
      1: 8,
      2: 4,
      3: 0,
    }
   return switcher.get(empCheck,"employee wage")
empHrs = int(wage(empCheck))
salary = (empHrs * EMP_RATE_PER_HR)
totalSalary = (salary * NUM_OF_WORKING_DAYS)
print("salary for a month " ,totalSalary)