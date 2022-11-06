        
d = [1,2,5,3,4,10,7]
d_run = d[1:]
last = d[0]


res = 0
for i in d_run:
    if i > last:
        print(i)
        last = i
        res = i
    print('javob = ', res)