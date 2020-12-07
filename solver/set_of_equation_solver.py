from cropper.yolov4 import yolov4

import numpy
from preprocess.deskew import text_skew
from digit_segmentor.ocr_module import ocr
from solver.equation_solver import eq_solver
import cv2
import config
import copy
equation_weight = config.equation_weight
char_weight = config.char_weight
config_path = config.config_path
yolov4_char = cv2.dnn.readNet(char_weight, config_path)
yolov4_eq = cv2.dnn.readNet(equation_weight, config_path)

def eq_4_display(list_eq):
  list_4_display =[]
  for eq in list_eq :
    string = ""
    for i,char in enumerate(eq):
      if char in ["+", "="]:
        string += " " + char + " "
      elif char == "-":
        if i == 0 or string[len(string)-2:len(string)] == "= ":
          string += char
        else :
          string += " " + char + " "
      elif char.isnumeric() :
        if i == 0 :
          string += char
        elif string[-1].isalpha():
          string += "^" + char
        else :
          string += char
      else :
        string += char
    list_4_display.append(string)



  return list_4_display

def soe_solver(image):

    equation_detection = yolov4(image, yolov4_eq, "eq")
    equation_coor = equation_detection.detection(0.5, 0.4)

    if equation_coor is not None:
        # Xoay ảnh input ban đầu
        ## buoc nay da detect+crop+xoay
        deskewed_img = text_skew(image, equation_coor, False)

        # Từ ảnh đã crop + xoay ( cleaned-up ) , lấy ra toạ độ các pt trong ảnh đã xoay
        equation_detection_1 = yolov4(deskewed_img, yolov4_eq, "eq")
        equation_coor_1 = equation_detection_1.detection(0.5, 0.4)




        # crop lần nữa cho ra output focus vào hệ
        eqs_cropped = text_skew(deskewed_img, equation_coor_1, True)


        # Sắp xếp theo chiều từ trên xuống
        equation_coor_1 = sorted(equation_coor_1, key=lambda x: x[1])
        # List equation images
        equation_image = [deskewed_img[y:y + h, x:x + w + 5] for x, y, w, h in equation_coor_1]

        list_text_equation = []
        for num, eq in enumerate(equation_image):
            char_detection = yolov4(eq, yolov4_char, "char")
            char_coor = char_detection.detection(0.5, 0.3)

            # List character images
            char_image = [eq[y:y + h, x:x + w] for x, y, w, h in char_coor]

            text = ocr(char_image)
            list_text_equation.append(text)

        result = eq_solver(list_text_equation)
        res = []
        temp = result
        if(isinstance(result,dict)):
            result = []
            result.append(temp)

        for i in result:
            res_dict = {}
            for idx, key in enumerate(i.keys()):
                res_dict[str(list(i.keys())[idx])] = str(list(i.values())[idx])
            res.append(res_dict)
        parsed_expr = eq_4_display(list_text_equation)
        return (res, parsed_expr, copy.deepcopy(eqs_cropped), deskewed_img,equation_coor_1)
    return None
