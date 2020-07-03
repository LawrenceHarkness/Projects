mark = eval(input('please enter the mark you acquired'))
if (mark <=100 and mark >=95):
    print('you got an A+')
elif (mark >= 80 and (mark <95)):
    print ('you got an A')
elif (mark >= 70 and (mark <80)):
    print ('you got an B')
elif (mark >= 60 and (mark <70)):
    print ('you got an C')
elif (mark >= 50 and (mark <60)):
    print ('you got an D')
elif (mark >= 40 and (mark <50)):
    print ('you got an E')
elif (mark >= 0 and (mark <40)):
    print ('you got an F')
else:
    print ('you have entered an invalid mark')