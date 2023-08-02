'''a = int (float(input("hay nhap  so kwh ma bạn tiêu thụ hàng tháng ")))
if (  200 >= a):
    print(" đơn giá của bạn là 1768 đồng/ kwh")
elif (  300 >= a ):
       print(" đơn giá của bạn là 2074 đồng/ kwh")
elif ( 400>=a ):
       print(" đơn giá của bạn là 2612 đồng/ kwh")
elif ( a>= 400):
       print(" đơn giá của bạn là 3015 đồng/ kwh")    
if(  50>= a ):
        print( " đơn giá của bạn là 1728 dong/kwh")'
n = 1 
while (n>=0):
    n = int( input( "hay nhap n:"))

n =1000
for i in range(n):
    print (i)
n = int(input( "nhap vao n"))
tong = 0
for i in range(n+1):
    tong+=i
    print("tong = ", tong)
n = input()
for i in range(10,50):
 if  (i%3 == 0):
  print(i)
 elif ():
  print( "loi")
sum = 1
gt = 1
for i in range (2,11 ):
    gt*= i
    sum+= gt
print(sum) 
 bai 5import math
n = int(input())
if n<0:
    print("hay nhap so !")
elif n <2:
 print("{}  khong phai la so nguyen to".format(n))  
else:
   for i in range(2,int(math.sqrt(n)) +1):
      if n%i ==0 :
           print("{}  khong phai la so nguyen to".format(n))  
           break  
      else :
         print("{}   la so nguyen to".format(n))
     
y = input("ban co muon nhap lai hay ko?")
n = int(input( "moi ban nhap lai n:"))
if y =="co":
   import math
   if (n<0):
    print("hay nhap so !")
   elif n <2:
    print("{}  khong phai la so nguyen to".format(n))  
   else:
    for i in range(2,int(math.sqrt(n)) +1):
      if n%i ==0 :
           print("{}  khong phai la so nguyen to".format(n))  
           break  
      else :
        print("{}   la so nguyen to".format(n))
elif(y =="ko"):
 print("ket thuc truong trinh")
x = int(input())
n = int(input()) 
if n < 0:
    print("vui long nhap so tu nhien ")
elif n ==0:
    print(1) 
else:
    S =1
    giaithua = 1
    for i  in range( 1,2*n +1 ):
        giaithua *= i

        if i %2 ==0:
            S+= pow(x,i)/giaithua
        else:    
            S-= pow(x,i)/giaithua 
    print("{:.5f}". format(S)) 
j = 150000000
if ( 2147 ):
    for i in range(2017,2147+1,130):
        
        print(i,"day la so nam ta de lan 150 trieu dan")
    
        

else:
    print ("chuong trinh nay co the bi loi ")'''    
      
   
    
a = 40
if ( 2147 ):
    for i in range(1,40+1,39):
        
        print(i,"so nam nguoi do can de tra no")
    
        

else:
    print ("chuong trinh nay co the bi loi ")    
      