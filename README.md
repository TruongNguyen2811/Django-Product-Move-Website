# Django-Product-Move-Website
 Hướng dẫn cài đặt
 B1: cài đặt môi trường python
 B2 : cài đặt Django bằng pip install Django trong commandline 
 B3 : tạo 1 CSDL MySQL tên manageapple
 B4: vào file setting.py trong phần DATABASE
 + chỉnh lại các trường password
 +Host
 +Port theo cơ sở dữ liệu đang sử dụng
 B5: chạy câu lệnh py manage.py makemigrations
 B5: chạy câu lệnh py manage.py migrate
 B6: tạo 1 super user bằng câu lệnh py manage.py createsuperuser
 B7: chạy câu lệnh py manage.py runserver để chạy trên server
 B8: vào trang admin django và tạo các nhóm đối tượng 'admins' 'factorys' 'Stores' 'warrantyCenters'
 B9: add super user vừa vạo vào nhóm admins
 B10: vào http://127.0.0.1:8000/login/ và đăng nhập bằng tài khoản super user
 
