def check_if_prime(num):
    for x in range(2,num):
        if num%x==0:
            print(num, 'equals', x,'*', num//x)
            break

    else:
     print(num, 'is a prime number')

for n in range(2,10):
    check_if_prime(n)
    
