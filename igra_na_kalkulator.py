a = 0
b = int(input())
e = input()
c = int(input())
d = int(input())
if e == "/":
    a = b / c == d
elif e == "+":
    a = b + c == d
elif e == "-":
    a = b - c == d
elif e == "*":
    a = b * c == d
if a:
    print("Yes")
else:
    print("No")
