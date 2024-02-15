n = float(input())

x = 5
#t = 1e-6
powered = x ** x
div = 5

while round(powered, 6) != round(n, 6):
        div = div/2
        if powered < n:
                x += div
        else:
                x -= div
        powered = x ** x
       
print(round(x, 6))



#n = input()
#n = 7
#l, u = 1.0, max(float(n), 2.0)
#t = 1e-6

#while u-l > t:
    #mid = (l + u) / 2

   # if mid ** mid < float(n):
      #  l = mid
    #else:
      #  u = mid

#print(round(mid, 6))

