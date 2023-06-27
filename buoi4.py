import random
qua = random.randint(1,4)
if (qua == 1):
    print("bo vao do a")
elif  ( qua == 2 ):
    print("bo vao gio b")   
elif  ( qua == 3 ):
    print("bo vao gio c") 
elif  ( qua == 4 ):
    print("bo vao gio d") 
    
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


      