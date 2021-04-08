
list=[48,'python','iki',5,-18,'hello','name',5.2,8.7,6.1,0] #liste oluşturdum
len(list)                       #uzunluğunu buldum
first=(list[0:len(list)//2] )   #  ilk yarısını buldum
second=(list[len(list)//2:])    #  ikinci yarısını buldum
print(first+second)             #  listenin ilk hali     
print(second+first)             # listenin yarısından sonra yer değiştirilmiş hali



-----------------------

n=int(input("Bir değer girin:"))   
for i in range(n):
    if i % 2==0:
      print(i)
    
      