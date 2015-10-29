__author__ = 'bijan'
# url = 'http://www.pythonchallenge.com/pc/return/bull.html'
s = '1'
for i in range(30):
    l = len(s)
    new_s =''
    count = 0
    prev_num = '1'
    for j in range(l):
        num = s[j]
        if j == 0:
            count += 1
            prev_num = num
        else:
            if num == prev_num:
                count += 1
            else:
                new_s += str(count)+prev_num
                prev_num = num
                count = 1
        if j == l-1:
            new_s += str(count)+prev_num
            s = new_s
print(len(s))
