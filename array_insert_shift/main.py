import math
def insertShiftArray(arr,n):

     location = len(arr)/2
     if location %2 ==0 :
         arr.insert(int(location) , n)
     elif location % 2 != 0:
        location =  location-(location%2)
        location = math.ceil(location)
        location +=1
        arr.insert(location,n)
