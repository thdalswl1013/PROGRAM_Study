# 풀이 1
score=input()

if score=="A+":
    print(4.3)
elif score=="A0":
    print(4.0)
elif score=="A-":
    print(3.7)
elif score=="B+":
    print(3.3)
elif score=="B0":
    print(3.0)
elif score=="B-":
    print(2.7)
elif score=="C+":
    print(2.3)
elif score=="C0":
    print(2.0)
elif score=="C-":
    print(1.7)
elif score=="D+":
    print(1.3)
elif score=="D0":
    print(1.0)
elif score=="D-":
    print(0.7)
elif score=="F":
    print(0.0)


# 풀이 2
"""
dic = {'A+':'4.3', 'A0':'4.0', 'A-':'3.7',
       'B+':'3.3', 'B0':'3.0', 'B-':'2.7',
       'C+':'2.3', 'C0':'2.0', 'C-':'1.7',
       'D+':'1.3', 'D0':'1.0', 'D-':'0.7',
       'F':'0.0'}
grade = input()
print(dic[grade])
"""