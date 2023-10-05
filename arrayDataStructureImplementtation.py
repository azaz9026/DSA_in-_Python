## Random Access ---------------------------------------------------------------------

arr = [1,2,3,4,5,6,7,8,9,10]

print(arr[4])          ## Ans 5



## Insert an element 5 at index 2 -------------------------------------------------------
## arr.insert(index , element)

arr.insert(2 , 5)
print(arr)            ## Ans [1, 2, 5, 3, 4, 5, 6, 7, 8, 9, 10] 



## Remove an element 8 from the array ---------------------------------------------------
## arr.remove(element)

arr.remove(8)
print(arr)             ## Ans [1, 2, 5, 3, 4, 5, 6, 7, 9, 10]



## Count an element 5 in an array -------------------------------------------------------
## arr.count(element)

print(arr.count(5))    ## Ans Count of element 5 is 2



## Delete an index 2 element 5 in an array ------------------------------------------------------
## arr.pop()

arr.pop(2)
print(arr)             ## Ans [1, 2, 3, 4, 5, 6, 7, 9, 10]



## Sort of  Array -------------------------------------------------------------------------------
## arr.sort(arr)

arr1 = [1,2,3,4,5,6,7,9,4,10]
arr1.sort()
print(arr1)            ## Ans [1, 2, 3, 4, 4, 5, 6, 7, 9, 10]



## To Extract the index of any given element ----------------------------------------------------
## arr.index(element)


(arr.index(1))

    ## Ans element 1 index number is 0



## To extent the orginal array ------------------------------------------------------------------
## arr.extend([element])

arr.extend([10,20,30,40,50])
print(arr)              ## Ans [1, 2, 3, 4, 5, 6, 7, 9, 10, 10, 20, 30, 40, 50]




## To Reveres the whole array -------------------------------------------------------------------

arr.reverse()
arr1.reverse()
print(arr)
print(arr1)
