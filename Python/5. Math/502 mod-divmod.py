#https://www.hackerrank.com/challenges/python-mod-divmod/problem

x,y = (int(input()) for i in range(2))
a,b = divmod(x,y)
print(a,b, (a,b), sep="\n")
