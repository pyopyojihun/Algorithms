import sys

N=int(sys.stdin.readline())
s=[]

for i in range(N):
    inp=sys.stdin.readline().rstrip()

    if ' ' in inp:
        inp,n=inp.split()
        n=int(n)

    if inp=='push':
        s.append(n)

    elif inp=='pop':
        if len(s)==0:
            print(-1)

        else:
            print(s.pop())

    elif inp=='size':
        print(len(s))

    elif inp=='empty':
        if len(s)==0:
            print(1)

        else:
            print(0)

    elif inp=='top':
        if len(s)==0:
            print(-1)
        else:
            print(s[len(s)-1])
