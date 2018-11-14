import bisect
import random
import datetime

SIZE = 30

now = int(datetime.datetime.now().timestamp())
random.seed(now)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
