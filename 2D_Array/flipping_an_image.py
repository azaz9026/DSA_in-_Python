## Flipping an image ---------------------------------------------------------------------------------------------------------------------------


def flippingImage(image):
    reverse(image)
    return image


def reverse(image):
    n = len(image)
    for i in range( 0 , n ):
        s = 0 
        e = n - 1

        while s <= e:
            temp = image[i][s]
            image[i][s] = image[i][e]
            image[i][e] = temp
            s +=1
            e -=1
        
        for j in range( 0 , n ):
            image [i] [j] = 1 if image [i] [j] == 0 else 0

image = [[1,1,0],[1,0,1],[0,0,0]]
result = flippingImage(image)
print(result)



## Ans => [[1, 0, 0], [0, 1, 0], [1, 1, 1]]