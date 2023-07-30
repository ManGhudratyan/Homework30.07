def findGreatestDiv(a, b):
    mset = set();
   
    for i in range(1, max(a, b) + 1):
        if (a % i == 0 and b % i == 0):
            mset.add(i);
    max_number = max(mset);
    return max_number
    
print("The greatest common divisor:", findGreatestDiv(15, 75));
