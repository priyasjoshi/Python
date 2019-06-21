def factcal(n):
    fact = 1
    while n>0:
        fact *=n
        n= n-1
        if (n<=1):
            break
    else: #Display the message if n is not positive integer.
        print('Input a correct number...')
        return
    return fact
def factdata(n):
    result = []
    while n>0:
        result.append(n)
        n = n-1
        if (n==0):
          break
    else:
        print('Input a correct number......')
        return
    return result