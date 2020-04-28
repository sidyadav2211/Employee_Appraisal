# Program that check you got appraisal or not
#project 1 to 10
project_complete=int(input('Enter number of project you Completed :'))
# manager rating upto 1 to 5
manager_rating=float(input('Plase give your rating sir :')) 

if project_complete>=5 and manager_rating>=3:
    employee=True
else:
    employee=False
if employee:
    print('You got Appraisal ')
else:
    print('Better next time ')