#Code bài này được viết trên VsCode và sử dụng thư viện Pillow để xử lý

#import Image từ thư viện Pillow
from PIL import Image

#Nhập đường dẫn đã tải về thư mục
dir = input("Xin moi nhap duong dan thu muc chua pic: ")

#Tạo đường dẫn cho thư mục và ảnh
image_path = dir + '/pic/bai1.JPG'
pic_path = dir + '/pic'

# Mở ảnh từ đường dẫn
img_01 = Image.open(image_path)
print(pic_path)

#Chuyển ảnh thành ảnh xám
gray_01 = img_01.convert("L")
gray_01.show()

#Tách band màu của ảnh
red_01, green_01, blue_01 = img_01.split() #Chỗ này ta có thể dùng hàm getchannel với cú pháp img_01.getchannel("R hoặc G hoặc B")

# Lưu ảnh
gray_01.save(pic_path + '/gray.JPG')
red_01.save(pic_path + '/red.JPG')
green_01.save(pic_path + '/green.JPG')
blue_01.save(pic_path + '/blue.JPG')

#Merge lại các band màu

# 1. Merge đúng thứ tự RGB
merge_01 = Image.merge("RGB", (red_01, green_01, blue_01))
merge_01.show()

# 2. Đảo lại thứ tự
merge_02 = Image.merge("RGB", (red_01, blue_01, green_01))
merge_02.show()

# 3
merge_03 = Image.merge("RGB", (green_01, blue_01, red_01))
merge_03.show()

# 4
merge_04 = Image.merge("RGB", (green_01, red_01, blue_01))
merge_04.show()

# 5
merge_05 = Image.merge("RGB", (blue_01, red_01, green_01))
merge_05.show()

# 6
merge_06 = Image.merge("RGB", (blue_01, green_01, red_01))
merge_06.show()

#Lưu lại các ảnh merge
merge_01.save(pic_path + '/merge1.JPG')
merge_02.save(pic_path + '/merge2.JPG')
merge_03.save(pic_path + '/merge3.JPG')
merge_04.save(pic_path + '/merge4.JPG')
merge_05.save(pic_path + '/merge5.JPG')
merge_06.save(pic_path + '/merge6.JPG')

#Đóng ảnh
img_01.close()

# Có tất cả 3! = 6 cách chuyển đổi cho ra 6 màu ảnh khác nhau