def CheckPrime(num):

    for i in range(num):
        
        if num <= 1:
            return False
    
        if num % 2 == 0:
            return False
    
    return True