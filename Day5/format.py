'''
a = 3
name = 'alan'
age = 18

print('hi my name is', name, 'and I am', age, 'my number is', a)
print(20/6)

name = ['kevin', 'andy', 'Luka']
age = [100, 7, 25]
print(name[0], name[1], name[2])
print(age[0], age[1], age[2])
format 1.變數跟字串混合輸出 2.取到小數後第幾位 3.對齊

(1)% %s(str) %d(int) %f(float)
(2).format
(3)f-string
name = ['alan', 'aaron', 'jessica']
age = [18, 8, 100]
print("Hi my name is %-7s and I am %3d years old" % (name[0], age[0]))
print("Hi my name is {:7s} and I am {:3d} years old".format(name[1], age[1]))
print(f"Hi my name is {name[2]:7s} and I am {age[2]:3d} years old")

print("1:{1} 2:{2} 3:{0}".format('alan', 'aaron', 'jessica'))

bmi = weight(kg)/height(m)^2
h, w = 180, 70
bmi = w / ((h / 100) ** 2)
print(f"height={h}, weight={w}, bmi={bmi:.1f}")
'''


