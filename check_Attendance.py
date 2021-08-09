'''
@Author: Nikita Rai
@Date: 2021-08-05 07:10:00
@Last Modified by: Nikita Rai
@Last Modified time: 2021-08-06 06:10:00
@Title : Check Employee is
Present or Absent
- Use ((RANDOM)) for Attendance
Check
'''

import random
print("Welcome in Employee Wage Computation")
ISPRESENT = 1
randomCheck = random.randint(0, 1)
if ( ISPRESENT == randomCheck ) :
	print("Employee is present" )
else:
	print("Employee is absent")
