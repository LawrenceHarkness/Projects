import time

from_ = eval(input('what would you like to count from'))
upto = eval(input('what number would you like to count upto?'))

for i in range(from_,upto + 1):

    print('\t {0}'.format(i))
    time.sleep(1)
print('-----------\n all done\n-----------')











