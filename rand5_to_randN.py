from random import random

# Condition:
def rand5():
    # return one number in [1, 2, 3, 4, 5] in equal possibility
    return int(random() * 5 + 1)

# --------------------------------------------- #

# Implementation:
def rand7():
    # Given rand5, return one of 1 to 7 in equal possibility
    while(True):
        rand25 = 5 * (rand5()-1) + (rand5()-1)
        if rand25 < 21:
            return rand25 % 7 + 1

def power_rand(i):
    # return a function that generates random
    # power_rand(1) return 0 to 4 on average (5 numbers)
    # power_rand(2) return 0 to 24 on average (25 numbers)
    # power_rand(3) return 0 to 624 on average (625 numbers)
    # ...
    if i == 1:
        return rand5()-1
    else:
        i -= 1
        return (5**i)*(power_rand(i)) + (power_rand(i))

def randN(n):
    # input n
    # Given rand5(), return one of 1 to n in equal possibility
    if n < 1:
        print("illegal n \n")
        return -1

    max_range = 5
    times = 1
    while(max_range < n):
        times += 1
        max_range **= 2

    effective_range = max_range // n * n

    while(True):
        x = power_rand(times)
        if x < effective_range:
            return x % n + 1 


# Test cases:
# We assume it's OK if accuracy rate > 98%
if __name__ == "__main__":
    # test case for rand7:
    count_1s = 0
    count_4s = 0
    count_7s = 0
    for i in range(70000):
        rand_num = rand7()
        if rand_num == 1:
            count_1s += 1
        elif rand_num == 4:
            count_4s += 1
        elif rand_num == 7:
            count_7s += 1
    print count_1s, count_4s, count_7s
    assert(abs(count_1s - 10000) < 200)
    assert(abs(count_4s - 10000) < 200)
    assert(abs(count_7s - 10000) < 200)

    # --------------------------------------------- #

    # test case for randN:
    n = 10   # change 'n' for new cases
    count_1s = 0
    count_Ns = 0
    count_half_Ns = 0
    for i in range(10000*n):
        rand_num = randN(n)
        if rand_num == 1:
            count_1s += 1
        elif rand_num == n // 2:
            count_half_Ns += 1
        elif rand_num == n:
            count_Ns += 1
        
    print count_1s, count_half_Ns, count_Ns
    assert(abs(count_1s - 10000) < 200)
    assert(abs(count_half_Ns - 10000) < 200)
    assert(abs(count_Ns - 10000) < 200)


    # test case for randN:
    n = 29   # change 'n' for new cases
    count_1s = 0
    count_Ns = 0
    count_half_Ns = 0
    for i in range(10000*n):
        rand_num = randN(n)
        if rand_num == 1:
            count_1s += 1
        elif rand_num == n // 2:
            count_half_Ns += 1
        elif rand_num == n:
            count_Ns += 1
        
    print count_1s, count_half_Ns, count_Ns
    assert(abs(count_1s - 10000) < 200)
    assert(abs(count_half_Ns - 10000) < 200)
    assert(abs(count_Ns - 10000) < 200)


    '''
    Emmm, the complexity for randN is not high since the recursive function won't be deep.
    But the performance of UT is a little bit poor for Python. /facepalm
    If you want to see the count result for n larger than 625, even 625^2, please decrease the loop amount for UT. /facepalm
    '''