import numpy as np
import cv2
def text_skew(image, coor, check) :

  np_coor = np.array(coor)
  x_new = np.min(np_coor[:,0])
  y_new = np.min(np_coor[:,1])
  w_new = np.max(np.array([x + w for x,y,w,h in coor])) - x_new
  h_new = np.max(np_coor[:,1]) + np_coor[np.argmax(np_coor[:,1])][3] - np.min(np_coor[:,1])

 #Crop soe
  soe_cropped = image[y_new : y_new + h_new, x_new : x_new + w_new]
  # If check == true thì chỉ trả về ảnh đc crop
  if check == True :
    return soe_cropped
  #if check == False thì sẽ trả về ảnh gốc đã được xoay
  else :
    gray = cv2.cvtColor(soe_cropped, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    image_black = np.zeros((image.shape[0], image.shape[1]))
    image_black[y_new : y_new + h_new, x_new : x_new + w_new] = thresh
    
    coords = np.column_stack(np.where(image_black > 0))
    angle = cv2.minAreaRect(coords)[-1]
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
      angle = -(90 + angle)
    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
      angle = -angle

    # if abs(angle) < 10 :
    #   return image
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h),
      flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    
    return rotated

