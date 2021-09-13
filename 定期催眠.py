import time

x=1
while x>0:
    print('你開的是必修課，可以如煉獄試煉，不可讓學生必休克')
    print('你教的是大學生，可以如成人對待，不可讓學生當小孩')

    his=eval(input('世文成績(0~100):'))
    if(his<60):
        print('學生休克')
        time.sleep(2)
        continue

    y= eval(input('心智年齡(0~100):'))
    if(y<12):
        print('學生小孩')
        time.sleep(5)
        continue
