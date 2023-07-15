print("KRS TAX MANAGEMENT SYSTEM")
import mysql.connector
conn=mysql.connector.connect(user='root',password='kaushik81105',host='localhost',database='store',auth_plugin="mysql_native_password")
myc=conn.cursor()
#details given by manager

while True:
   print("PRESS S FOR GENERATING STATIONARY TAX")
   print("PRESS C FOR GENERATING CLOTHING TAX")
   print("PRESS E  GENERATING ELECTRICAL APPLIANCES TAX")
   print("PRESS G for GENERATING GROCERY TAX")
   print("X FOR EXIT")
   c=str(input("enter your choice(S\C\E\G\X):"))

   if(c=="S" or c=="s"):
      print("STATIONARY TAX")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      mobilenumber=input("customer's mobile number:")
      total=0
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            gst=28/100
            gtax=total*gst #gst taxed amount
            price=total+gtax # total amount of all products after adding gst 
            sql="insert into item (item_name,price,quantity,customer_name,phone_no,DATE,exact_price,GST) values('{}',{},{},'{}','{}','{}',{},{})".format(i,rate,qty,customer,mobilenumber,date,total,gtax)
            myc.execute(sql)
            conn.commit()

         print("Items Purchased Till Now:")
         x="select * from item where  customer_name=('{}')".format(customer)
         myc.execute(x)
         data=myc.fetchall()
         for row in data:
            print(row)
         print("gst:",gtax)
         print("Total Amount:",price)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("STATIONARY BILL")
   elif(c=="C" or c=="c"):
      print("CLOTHING BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      adress=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      
      mobilenumber=str(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            #print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            gst=8/100
            gtax=total*gst #gst taxed amount
            price=total+gtax # total amount of all products after adding gst 
            sql="insert into item (item_name,price,quantity,customer_name,phone_no,DATE,exact_price,GST) values('{}',{},{},'{}','{}','{}',{},{})".format(i,rate,qty,customer,mobilenumber,date,total,gtax)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         x="select * from item where  customer_name=('{}')".format(customer)
         myc.execute(x)
         data=myc.fetchall()
         for row in data:
            print(row)
         print("gst:",gtax)
         print("Total Amount:",price)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("CLOTHING BILL")
   elif(c=="E" or c=="e"):
      print("ELECTRICAL APPLIANCES TAX")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      
      mobilenumber=str(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            ##print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            gst=18/100
            gtax=total*gst #gst taxed amount
            price=total+gtax # total amount of all products after adding gst 
            sql="insert into item (item_name,price,quantity,customer_name,phone_no,DATE,exact_price,GST) values('{}',{},{},'{}','{}','{}',{},{})".format(i,rate,qty,customer,mobilenumber,date,total,gtax)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         x="select * from item where  customer_name=('{}')".format(customer)
         myc.execute(x)
         data=myc.fetchall()
         for row in data:
            print(row)
         print("GST:",gtax)
         print("Total Amount:",price)
         
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("ELECTRICAL APPLINCES TAX")
   elif(c=="G" or c=="g"):
      print("GROCERY BILL")
      date=input("invoice date:")
      impt=int(input("no. of item purchase:"))
      print("details of customer")
      customer=str(input("customer's name:Mr./Miss:"))
      address=str(input("customer's adress:"))
      city=str(input("customer's city:"))
      
      mobilenumber=int(input("customer's mobile number:"))
      total=0 
      maxitem=41 # maximum  number of items can be purchased at a time 
      if(impt<=maxitem):
         for a in range(1,impt+1):
            ##print("serial no:",a)
            i=str(input("item:"))
            rate=float(input("price of item in rupees:"))
            qty=int(input("quantity of item purchased:"))
            value=qty*rate # total  price of product with no. of quantity 
            print("Total price:",value)  # total  amount of particular product
            total=total+value # total  amount of all products
            gst=4/100
            gtax=total*gst #gst taxed amount
            price=total+gtax # total amount of all products after adding gst 
            sql="insert into item (item_name,price,quantity,customer_name,phone_no,DATE,exact_price,GST) values('{}',{},{},'{}','{}','{}',{},{})".format(i,rate,qty,customer,mobilenumber,date,total,gtax)
            myc.execute(sql)
            conn.commit()
         print("Items Purchased Till Now:")
         x="select * from item where  customer_name=('{}')".format(customer)
         myc.execute(x)
         data=myc.fetchall()
         for row in data:
            print(row)
         print("GST:",gtax)
         print("Total Amount:",price)
      else:
         print(" Sorry You Can Only Buy 41 Items At A Time")
      print("GROCERY BILL")
   elif(c=="x" or c=="X"):
      break
   else:
      continue
