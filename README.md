# Equations-solver
## 1. Tải weight và darknet
- Tải weight file tại https://drive.google.com/drive/folders/1FeCE8Kl4MZM0DWupdy6taGXra6UzkO2q?fbclid=IwAR0IQwZyAwk6bAwTxWVvfKxO7xOLruW_T1eNkkpYaDzJlPH5s4DIXnHUkcw
- Tải darknet tại https://github.com/AlexeyAB/darknet.git
## 2. Config
- Sau khi tải Darknet, vào thư mục darknet/config tạo bản sao của yolov4-custom.cfg và đặt tên là yolov4_training.cfg
- Trong file yolov4_training.cfg :
  - Sửa classes = 80 thành classes = 1 tại dòng số : 970 1058 1146
  - Sửa filters = 255 thành filters = 18 tại dòng số : 1139 1051 963
- Trong file Makefile trong thư mục darknet :
  - Sửa GPU = 0 thành GPU = 1
  - Sửa OPENCV =0 thành OPENCV = 1
## 3.Chạy chương trình
# 
# Chạy Front-end
- cd vào thư mục front_end\app\src
- npm install
- npm start

# Chạy Back-end
- cd vào thư mục main.py
- pip install -r requirements.txt
- python main.py
## 3. Contributors
- Doãn Xuân Khang https://github.com/khangdx1998
- Đặng Phương Nam
- Nguyễn Đức Thắng https://github.com/thangnd3629
- Ngô Song Việt Hoàng
- Nguyễn Đình Hùng


