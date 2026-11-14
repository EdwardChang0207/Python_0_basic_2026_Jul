a, b, c = input().split()
a, b, c = int(a), int(b),int(c)
D = b**2 - 4*a*c

if D < 0:
    print('No real root')
elif D == 0:
    a1 = int((-b / (2*a)))
    print(f'Two same roots x={a1}')
else:
    a1 = int((-b + D**0.5) / (2*a))
    a2 = int((-b - D**0.5) / (2*a))
    print(f'Two different roots x1={a1} , x2={a2}')

a, b, c=input().spilt
a, b, c=int(a), int(b), int(c)
D = b**2 - 4*a*c

if D <0:
    print("No real root")
elif D==0:
    a1 = int((-b + D**0.5)//(2*a))
    print(f"Two same roots x={a1}")
else :
    a1=int((-b + D**0.5)//(2*a))
    a2=int((-b + D**0.5)//(2*a))
    print(f"Two different roots x1={a1} , x2={a2}")

a, b, c=input().split()
a, b, c=int(a), int(b), int(c)
D = b**2 - 4*a*c

if D <0:
    print("No real root")
elif D==0:
    a1 = int((-b + D**0.5)//(2*a))
    print(f"Two same roots x={a1}")
else:
    a1=int((-b + D**0.5)//(2*a))
    a2=int((-b - D**0.5)//(2*a))
    print(f"Two different roots x1={a1} , x2={a2}")