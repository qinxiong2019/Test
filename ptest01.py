# arr=[2,5,1,3,7,1,10,35,12]
# for i in range (0,len(arr)-1):
        # for j in range(i+1,len(arr)):
            # if arr[i]>arr[j]:
                # arr[i],arr[j]=arr[j],arr[i]

# print arr          



######selectsort

# arr=[2,5,1,3,7,1,10,35,12]
# print arr
# for i in range(0,len(arr)-1):
    # index = i
    # for j in range(i+1,len(arr)):
        # if arr[index]>arr[j]:
            # index=j
    # if i != index:
        # arr[i],arr[index]=arr[index],arr[i]
        # print arr[i],"<->",arr[index]

# print arr        
            
            
            
######quick sort

print "test update"

arr=[2,5,1,3,7,1,10,35,12]
print arr

for i in range(len(arr)):
        preIndex = i-1
        #print "preIndex:",preIndex
        current = arr[i]
        print "current:",current
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            #print "arr[preIndex+1],arr[preIndex]",arr[preIndex+1],arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
        #print "arr[preIndex+1]",arr[preIndex+1]
        print "arr:",arr
        
            
        
print arr

            