def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f

def ave(b,a):
    s=0
    c=0
    for i in range(b,a+1):
        s+=i
        c+=1
    return (s/c)

def prime(a):
    c=0
    for i in range(2,a):
        if a%i==0:
            c+=1
    if c==0:
        print("Prime")
    else:
        print("Not prime")
        
def even(a):
    if a%2==0:
        return True
    else:
        return False