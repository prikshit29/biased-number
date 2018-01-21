import time

seed=time.time()
m=pow(2,32)
a=1664525
c=1013904223
num=[1,2,3,4,5,6,7,8,9,10] # sample list of 10 numbers
set=['L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','L','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H']  # sam set for each low or high category number

def rand():
    global seed
    seed=(a*seed+c)%m
    return int(seed)
def myrand():
    return rand()%rand()
def myrand(low,high):
    r = (rand() % (high - low)) + low
    return int(r)

def findrandnum(raa,rab,m):
    b=set[myrand(0,100)]
    if(b=='L'):
        print(myrand(raa,m))
    elif(b=='H'):
        print(myrand(m,rab))

#findrandnum()
print("enter the ranges for list i.e. for 1 to 100 , first enter 1 then enter 100")
ra=int(input("enter the lower range for list"))
rb=int(input("enter the upper range for list"))

mean=int((ra+rb)/2)
findrandnum(ra,rb,mean)
