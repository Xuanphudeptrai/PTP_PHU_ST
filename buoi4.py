'''import random

qua = random.randint(1,4)
if (qua == 1):
    print("bo vao do a")
elif  ( qua == 2 ):
    print("bo vao gio b")   
elif  ( qua == 3 ):
    print("bo vao gio c") 
elif  ( qua == 4 ):
    print("bo vao gio d") '''
    #bai1
n = int(float(input("hay nhap N")))
if   (n%2 == 0):
    print( "day la so chan")
elif (n%2 ==1):
    print("day la so le")
    #bai2
a = int(float(input("hay nhap  diem cua ban ")))
if ( a  >= 9 ):
        print (( "ban la hs gioi"))
elif ( a >= 8):
      print(" ban la hs kha ")      
elif ( a >= 5):
        print("ban la hs trung binh ") 
        
#bai3
nam = int(input( " hay nhap so nam "))
if ( nam %  4 == 0 ):
    print(" day la nam nhuan ")
elif  (nam % 100!=0 ) or (nam % 400 == 0):
    print(" day la nam khong nhuan ")
#bai4 
b = int(input("hay nhap vao thang nao do ban muon" ))


if b in (1,3,5,7,8,10,12):
     print("thang do co 30 ngay")
elif  b in (4,6,9,11):
     print("thang do co 31  ngay")    
elif  b==2:
   year = int(input( " hay nhap so nam: "))
if            ( year %  4 == 0 and year % 100!=0 ) or ( year  % 400 == 0):
      print ( " thang do co 29 ngay ")
else:   
      print ( "thang do co 28 ngay ")
#bai 6 
m = int(input("hay nhap vao thang nao do ban muon" ))
if m in ( 1,2,3 ):
    print("tháng này nằm trong quý 1")
elif m in (4,5,6):
     print (" tháng này nằm trong  quý 2")   
elif m in (7,8,9):
     print(" tháng này nằm trong quý 3") 
elif m in (10,11,12):
     print("tháng này năm trong quý 4")         