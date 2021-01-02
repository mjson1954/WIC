def Power(Base, Exponent):
    if Base==0: return 1
    result=1
    for i in range(Exponent):
        result*=Base
    return result
#위에는 O(n)

def Power(Base, Exponent):
    if Exponent==0 or Base==0:
        return 1
    if Exponent%2==0:
        NewBase=Power(Base, Exponent/2)
        return NewBase*NewBase
    else:
        NewBase=Power(Base, (Exponent-1)/2)
        return (NewBase*NewBase)*Base
    
#이건 O(log2n)
