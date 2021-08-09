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
MAX_HRS_IN_MONTH = 100
TOTAL_EMP_HR = 0
TOTAL_WORKING_DAYS = 0
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
while ( TOTAL_EMP_HR<100 and TOTAL_WORKING_DAYS < NUM_OF_WORKING_DAYS ) :
          TOTAL_WORKING_DAYS+=1
          empCheck = random.randint(1, 3)
          empHrs = int(wage(empCheck))
          TOTAL_EMP_HR = empHrs + TOTAL_EMP_HR
          print("Total Working Hours of Employee " ,TOTAL_EMP_HR )
totalSalary = ( TOTAL_EMP_HR * EMP_RATE_PER_HR)
print("Total salary of workings hours and days " ,totalSalary)