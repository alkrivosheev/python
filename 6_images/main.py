import cv2#pip install opencv-python

img = cv2.imread("galaxy.jpg",0)#as grey
# img = cv2.imread("galaxy.jpg",1)#as color

print( cv2.__version__ )
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# resized_image = cv2.resize(img,(1000,500))#изменение размера
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))#изменение размера с соблюдением пропорции
cv2.imshow("Galaxy",resized_image)
cv2.imwrite("Galxy_resized.jpg",resized_image)
# cv2.waitKey(2000)#2 sec
cv2.waitKey(0)#wait anykey
cv2.destroyAllWindows()