import cv2

# load the images

# ruta de la imagen
image_path = "./images/Carne-de-Wagyu.jpg"

# creación de la imagen para trabajar en open cv
image_wagyu = cv2.imread(image_path)


# saves copy as png

# ruta con el nombre final que tendra la imagen en formato png
image_copy_path = "./images/Carne-de-Wagyu-copy.png" 

# creacion de la copia este metodo recive dos parametros: la ruta y nombre que recibira la imagen donde se guardará y el otro parametro la imagen creada por opencv
cv2.imwrite(image_copy_path,image_wagyu)

# load the copy
image_wagyu_png = cv2.imread(image_copy_path)

# show the created images

cv2.imshow("original in jpg",image_wagyu)# recive dos parametros un titulo y la iamgen creada en opencv
cv2.imshow("copy ",image_wagyu_png)
cv2.waitKey(0)
cv2.destroyAllWindows()