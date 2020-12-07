import cv2
import numpy as np
def preprocessing_image(image):

  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  image_blur = cv2.medianBlur(image_gray, 3)
  ret, thresh = cv2.threshold(image_blur, 120, 255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
  image_bw = cv2.bitwise_not(thresh)

  #Padding
  h, w = image_gray.shape
  pad_size = int(abs(h-w)/2)
  pad_extra = abs(h-w)%2
  image_padding = np.array([])
  if h > w:
    image_padding = cv2.copyMakeBorder(image_bw, 0,0, pad_size + pad_extra, pad_size, cv2.BORDER_CONSTANT, value = [0,0,0])
    image_padding = cv2.copyMakeBorder(image_padding, 2,2,2,2, cv2.BORDER_CONSTANT, value = [0,0,0])
  elif w > h :
    image_padding = cv2.copyMakeBorder(image_bw,pad_size + pad_extra, pad_size,0,0, cv2.BORDER_CONSTANT, value = [0,0,0])
    image_padding = cv2.copyMakeBorder(image_padding, 2,2,2,2, cv2.BORDER_CONSTANT, value = [0,0,0])
  else :
    image_padding = image_bw
  
  #Resize 28x28
  image_resized = cv2.resize(image_padding, (28,28))

  #Dilate
  kernel_dilate = np.array((3,3), np.uint8)
  image_dilate = cv2.dilate(image_resized, kernel_dilate)

  
  #plt.show()

  #Expand dims
  image_result = np.expand_dims(image_dilate, 0)
  return image_result
