'''
1.math

int op int -> int
int op float -> float
float op float -> float

+, -, *, /(float)
    (1) ** 指數/次方
        print(3**5)
        print(2**6)
    (2) % 餘數 20 / 3 = 6(商)...2(餘數)
        print(20%3)
    (3) // 商數
        print(20//3)

2.關係
something op something -> bool
    >, <, >=, <=
    補充 = assign
    (1) == 相等
    (2) != 不相等
    (3) in 在裡面
    1 in [1,2,3]
    a in 'abc'
    print(2 < 1)
    print(4 in [1,2,3])

3.Logic
    (1) not 反閘
        周杰倫：哎呦不錯喔
        不(not)錯(False) -> True
        錯  -> False

        不(not)行(True) -> False
        行 -> True
        print(not False)
        print(not True)
    (2) or 或閘
        期中考
        math or english -> 3000
        T          F        T
        F          T        T
        T          T        T
        F          F        F(真值表 Truth Table)
        a, b = False, False
        print(a or b)
    (3) and 且閘
        放學
        HW and 打掃 -> :)
        T       F       F
        F       T       F
        T       T       T
        F       F       F
        a, b = False, False
        print(a and b)
    (4) xor (excursive or) 斥或閘
        買飲料
        珍奶 xor 烏龍 -> :)
        T       F       T
        F       T       T
        T       T       F
        F       F       F
        [1]and or not
        (a or b) and not(a and b)
        [2]binary ^
    a, b = bool(3),bool(5)
    print((a or b) and not(a and b))
    print(a^b)

4.bitwise
    1.not ~
    2.or |
    3.and &
    4.xor ^
    5.左移 <<
    6.右移 >>
    print(bin(~0b001))
    print(3|5)
    print(3&5)
    print(3^5)
    print(3>>1)
    print(5<<1)

a = -13
b = 5
print(a, b)
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

5.str&list
'''
print('abc'+'efg')
print([1,2,3]+[4,5,6])
print('abc'*3)
print([1,2,3]*3)