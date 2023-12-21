import cv2

# load the images

# ruta de la imagen
image_path = "./images/Carne-de-Wagyu-copy.png"

# creación de la imagen para trabajar en open cv
image_wagyu_gray = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
image_wagyu_alpha = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
# show the created images

cv2.imshow("imagen grises",image_wagyu_gray)# recive dos parametros un titulo y la iamgen creada en opencv
cv2.imshow("imagen canal alpha",image_wagyu_alpha)
cv2.waitKey(0)
cv2.destroyAllWindows()