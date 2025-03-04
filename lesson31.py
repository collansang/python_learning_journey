#default arguments = default values for certain parameters
                   # default is used when argument is omitted
                   #makes your functions more flexible and reduces the number arguments
                   #1. positional, 2. default, 3. keyword 4, arbitrary

def net_price(org_price, discount= 0.05, tax= 0.1): #numbers infront of them will be used as default you dont pass in
                                                    # the value when you call the function
    return org_price * (1-discount) * (1 +tax)
print(net_price(500))# i this case default values in tax and discount will be used


import time
def count(end, start=0):
    for x in range(start, end+ 1):
        print(x)
        time.sleep(1)#will be the one responsible for interval time wait to count a second
    print('DONE!!!!')

count(15)