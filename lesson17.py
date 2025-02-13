#for loops = execute a block of code a fixed number of times
             # you can iterate over a range , string, sequence et.

for m in range(1, 11): #counts fromm 1 to 10.
    print(m)

#To reverse you can enclose it with reversed function.
for x in reversed(range(2, 11)):
    print(x)

for w in range(3, 15, 2): #counts by 2s,, if replaced by 3 it counts by threes anf so on
    print(w)


#Suppose we are to count to 20 but we dont need 13 to appear, we can use (break) function
#           to break and stop from continuing or use (continue funtion to skip it and continue eg:

for a in range(1, 21): # skips number 13 and continues.
    if a == 13:
        continue
    else :
        print(a)

for b in range(1,21):# will stop immediately before 13
    if b == 13:
        break
    else:
        print(b)