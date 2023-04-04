q = 0x1
w = 0x2
e = 0x3
r = 0x4
t = 0x5
y = 0x6
u = 0x7
o = 0x8
p = []
a = open("instructions.bin",'rb').read()
s = a[0]
d = input("Enter the flag: ")
if len(d) != s:
    print("Incorrect")
    exit()
d = d[:s]
f = []
for g in d:
    f.append(ord(g))
i = 1
h = 0
while i < len(a):
    j = a[i]
    if j == q:
        p.append(a[i+1])
        i += 2
    elif (j == w) and (h < s):
        p.append(f[h])
        h += 1
        i += 1
    elif j == e:
        l = p.pop()
        print(l)
        i += 1
    elif j == r:
        z = p.pop()
        x = p.pop()
        p.append(z + x)
        i += 1
    elif j == t:
        z = p.pop()
        x = p.pop()
        p.append(z - x)
        i += 1
    elif j == y:
        z = p.pop()
        x = p.pop()
        p.append(z * x)
        i += 1
    elif j == u:
        z = p.pop()
        x = p.pop()
        p.append(z ^ x)
        i += 1
    elif j == o:
        k = p.pop()
        if k !=0:
            print("Incorrect!")
            exit()
        i += 1
    else:
        print("Invalid instruction")
        exit()
print("Correct!!")