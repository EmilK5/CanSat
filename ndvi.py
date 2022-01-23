import cv2
import numpy as np


def increase_contrast(image):
  max_image = np.percentile(image, 95)	
  min_image = np.percentile(image, 5)
	
	max_bgr = 255.0
	min_bgr = 0.0

  image_ic = image – min_image
  image_ic = image_ic * ((min_bgr – max_bgr) / (min_image – max_image))
  
  image_ic = image_ic + min_image

	return image_ic
  
#Reading in a photo
image = cv2.imread("image.jpg")
image_array = np.array(image, dtype=float)
image_contrasted = increase_contrast(image_array)

#Calculating NDVI
b, g, r = cv2.split(image_contrasted)
denominator = (r.astype(float) + b.astype(float))
denominator[denominator==0] = 0.01

numerator = (r.astype(float) - b.astype(float))
ndvi = numerator / denominator

ndvi_ic = increase_contrast(ndvi)

cv2.imwrite("image-ndvi-greyscale.png", ndvi_ic)
image_ndvi = cv2.imread("image-ndvi-greyscale.png")

#Putting on a color mask
img_ndvi = cv2.applyColorMap(image_ndvi, get_colormap('RdYlGn')).astype(np.int)
cv2.imwrite("image-ndvi.jpg", img_ndvi)

#Showing an image with key
mage_ndvi = cv2.imread("image-ndvi.jpg")
image_ndvi_array = np.array(image_ndvi, dtype=float)

cv2.imwrite("image-ndvi.jpg", image_ndvi_array)
img = Image.open("image-ndvi.jpg")

im_show = plt.imshow(img)
plt.colorbar(ticks=[])
plt.title("NDVI")
plt.show()

