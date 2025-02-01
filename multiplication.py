import pyinputplus as pyip
import random,time
numberofquestions=10
correct_answers=0
for questionnumber in range(numberofquestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    prompt='#%s:\t%s x %s ='%(questionnumber,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$' %(num1*num2)],blockRegexes=[('.*','Incorect!')],timeout=20,limit=3)
    except pyip.TimeoutException:
        print('out of time!')
    except pyip.RetryLimitException:
        print('out of tries')
    else:
        print('correct!')
        correct_answers+=1
    time.sleep(1)
    print('Score: %s /%s' %(correct_answers,numberofquestions))
          
