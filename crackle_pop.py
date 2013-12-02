#! /usr/bin/env python

# Uses Python 3.3
def crackle_pop_on_3_and_5(max_numb):
    """Returns None.  
        Prints Crackle when the number is divisible by 3, 
        Pop when divisible by 5 and 
        CracklePop when it's divisbile by both.  
        Otherwise prints the number upto max_numb
    """
    for numb in range(1,max_numb + 1):
        rem_3 = numb%3
        rem_5 = numb%5
        if rem_3 == 0 and rem_5 == 0:
            print('CracklePop')
        elif rem_3 == 0:
            print('Crackle')
        elif rem_5 == 0:
            print('Pop')
        else:
            print(numb)
    return None

if __name__ == '__main__':
    crackle_pop_on_3_and_5(100)