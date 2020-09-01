import cv2#pip install opencv-python
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("Resized_"+image,re)