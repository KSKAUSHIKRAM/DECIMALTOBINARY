import mysql.connector
conn=mysql.connector.connect(user='root',password='kaushik81105',host='localhost',auth_plugin="mysql_native_password")
myc=conn.cursor()
print("WELCOME")
print("KRS SUPERMARKET  ONLINE DELEIVERY")
R=input("enter your name:")
R1=input("ENTER YOUR LANDMARK:")
R2=input("enter the phone no:")
cavalue=0
L1=[]
while True:
    print("choose any of the following")
    print("1.PULSES CEREALS AND NUTS ITEMS\n")
    print("2. RICE FLOUR ITEMS\n")
    print("3.SPICES \n")
    print("4.OILS\n")
    print("5.GRAINS\n")
    print("6.READYMADE SPICES\n")
    print("7.BEVEREGES\n")
    ch =int(input("ENTER THE NO OR ENTER 0 TO EXIT:"))
    if ch>7:
        print("INVALID OPTION")
    if ch==0:
        break
    if ch==1:
        print("1.Toor Dal RS .120 \n")
        print("2.Urad Dal \n")
        print("3.Fried gram dal RS .150\n")
        print("4.Wheat flour RS.112 \n")
        print("5.Gram flour RS.102 \n")
        print("6.Corn flour RS.90\n")
        print("7.Maida RS.140\n")
        print("please enter it in numerical form for example half kg -0.5 quarter kg-0.25")
        r= int(input("Enter your choice :"))
        a=int(input("how many kgs needed:"))
        
        if r==1:
            i="ToorDal"
            L1.append(i)
            calculation1=120*a
            str(a)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation1,a,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:","RS.",calculation1)
            cavalue+=calculation1
        if r==2:
             i="URAD DAL"
             L1.append(i)
             calculation8=130*a
             str(a)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation8,a,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item:","RS.",calculation8)
             cavalue+=calculation8
        if r==3:
            i="FRIED GRAM DAL"
            L1.append(i)
            calculation2=150*a
            str(a)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation2,a,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:","RS.",calculation2)
            cavalue+=calculation2
        if r==4:
                    
             i="WHEAT FLOUR"
             L1.append(i)
             calculation3=112*a
             str(a)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation3,a,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item :","RS",calculation3)
             cavalue+=calculation3
        if r==5:
             calculation4=102*a
             i="GRAM FLOUR"
             L1.append(i)
             str(a)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation4,a,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item:","RS",calculation4)
             cavalue+=calculation4
        if r==6:
             calculation5=90*a
             i="CORN FLOUR"
             L1.append(i)
             str(a)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation5,a,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item:","RS",calculation5)
             cavalue+=calculation5
        if r==7:
             calculation6=140*a
             i="MAIDA"
             L1.append(i)
             str(a)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,calculation6,a,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item:","RS",calculation4)
                        
             cavalue+=calculation6

        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        
        
        if q==0:
            print("THE SELECTED ITEMS;",L1)
            print("the  total amount of the item is:",cavalue)
    elif ch==2:
                print("1.Ragi / Millet flour  Rs.120\n") 
                print("2.Chole / Chickpeas  Rs.100\n")
                print ("3.Hyacinth / Field bean Rs.110\n")
                print("4. Rajma / Red kidney bean Rs.112\n")
                print( "5.Peanuts / Groudnut  RS.159\n")
                print( "6.Cashewnuts -  RS.400\n")
                print("7. almonds -  RS.1000\n")
                print("please enter it in numerical form for example half kg -0.5 quarter kg-0.25\n")
                print("we will only provide 1 kg and 1/2 kg products\n")
                CH=int(input("Enter your choice:"))
                CH1=float(input("Enter how many kgs needed:"))
        
                if CH==1:
                    x=120*CH1
                    str(CH1)
                    i="RAGI"
                    L1.append(i)
                    sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,x,CH1,R1,R2)
                    myc.execute(sql)
                    conn.commit()
                    print("the amount of the item:",x)
                    cavalue+=x
                if CH==2:
                    x2=100*CH1
                    i="CHOLE"
                    L1.append(i)
                    str(CH1)
                    sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,x2,CH1,R1,R2)
                    myc.execute(sql)
                    conn.commit()
                    print("the amount of the item:",x2)
                    cavalue+=x2
                if  CH==3:
                    x3=110*CH1
                    i="HYACINTH"
                    L1.append(i)
                    str(CH1)
                    sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,x3,CH1,R1,R2)
                    myc.execute(sql)
                    conn.commit()
                    print("the amount of the item:",x3)
                    cavalue+=x3
                            

                if CH==4:
                   x4=112*CH1
                   i="RAJMA"
                   str(CH1)
                   L1.append(i)
                   sql="insert into supermarket (name,item_name,price,quantity,delivery_address) values('{}','{}',{},'{},'{}')".format(R,i,x4,CH1,R1,R2)
                   myc.execute(sql)
                   conn.commit()
                   print("the amount of the item:",x4)
                   cavalue+=x4

                if CH==5:
                  x5=159*CH1
                  i="PEANUTS"
                  L1.append(i)
                  str(CH1)
                  sql="insert into supermarket (name,item_name,price,quantity,delivery_address) values('{}','{}',{},'{},'{}')".format(R,i,x5,CH1,R1,R2)
                  myc.execute(sql)
                  conn.commit()
                  print("the amount of the item:",x5)
                  cavalue+=x5
                  
                if CH==6:
                 x6=400*CH1
                 i="CASHEWNUTS"
                 L1.append(i)
                 str(CH1)
                 sql="insert into supermarket (name,item_name,price,quantity,delivery_address) values('{}','{}',{},'{},'{}')".format(R,i,x6,CH1,R1,R2)
                 myc.execute(sql)
                 conn.commit()
                 print("the amount of the item:",x6)
                 cavalue+=x6

                 if CH==7:
                     x7=1000*CH1
                     i="almonds"
                     L1.append(i)
                     str(CH1)
                     sql="insert into supermarket (name,item_name,price,quantity,delivery_address) values('{}','{}',{},'{},'{}')".format(R,i,x7,CH1,R1,R2)
                     myc.execute(sql)
                     conn.commit()
                     print("the amount of the item:", x7)
                     cavalue+=x7
                     
                q=int(input("ENTER 0 to end the purchase or 1 continue:"))
                if q==0:
                    print("THE SELECTED ITEMS;",L1)
                    print("THE PRICES OF THE ITEMS ARE:",cavalue)
    elif ch==3:
        print(" 1.Turmeric powder / Haldi RS.250\n")
        print(" 2.Red chilly powder / Paprika RS.300\n")
        print(" 3.Coriander powder RS.250\n")
        print("4.Cumin RS.450\n") 
        print("5.Pepper RS.600\n")
        print ("6.Whole Red chillies RS.150\n")
        print("please enter it in numerical form for example half kg -0.5 quarter kg-0.25\n")
        print("we will only provide 1 kg and 1/2 kg products\n")
        AH=int(input("ENTER YOUR CHOICE\n:"))
        AH1=float(input("ENTER H0W MANY KGS NEEDED:"))

        if AH==1:
            r1=AH1*250
            i="TURMERIC POWDER "
            str(AH1)
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,r1,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",r1)
            cavalue+=r1

        if AH==2:
            r2=AH1*300
            i="RED CHILLY POWDER"
            str(AH1)
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,r2,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",r2)
            cavalue+=r2

        if AH==3:
            a3=AH1*250
            i="CORIANDER POWDER"
            L1.append(i)
            str(AH1)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,a3,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",a3)
            cavalue+=a3

        if AH==4:
            a4=AH1*400
            i="CUMIN"
            str(AH1)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,a4,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",a4)
            cavalue+=a4

        if AH==5:
            a5=AH1*600
            i="PEPPER"
            L1.append(i)
            str(AH1)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,a5,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",a5)
            cavalue+=a5

        if AH==6:
            a6=AH1*150
            i="RED CHILLIES"
            L1.append(i)
            str(AH1)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,a6,AH1,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item:",a6)
            cavalue+=a6
            
        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        
                
        if q==0:
                print("THE SELECTED ITEMS;",L1)
                print("THE PRICES OF THE ITEMS ARE:",cavalue)
                

    elif ch==4:

        print("1.VEGETABLE OIL\n AVAILABLE OILS[SUNFLOWER OIL, FORTUNE,EMAMI OIL] \n EACH PER LITRE-RS.120\n")
        print("2.COCONUT OIL- PER LITRE RS.100\n")
        print("3.MUSTARD OIL-PER LITRE RS.150\n")
        print("4.SESAME OIL-PER LITRE RS.170\n")
        print("5.CASTOR IL -PER LITRE  RS.160\n")
        print("please enter it in numerical form for example half litre-0.25\n")
        print("we will only provide 1 litre and 1/2 litre products\n")
        BH=int(input("ENTER  YOUR CHOICE:"))
        if BH==1:
            f=int(input("ENTER HOW MUCH LITRES NEEDED:"))
            c1=120*f
            i="VEGETABLE OIL"
            L1.append(i)
            str(f)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c1,f,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c1)
            cavalue+=c1
                        
        if BH==2:
             f=int(input("ENTER HOW MUCH LITRES NEEDED:"))
             c2=100*f
             i="COCONUT OIL"
             L1.append(i)
             str(f)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c2,f,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item is:",c2)
             cavalue+=c2

        if BH==3:
             f=int(input("ENTER HOW MUCH LITRES NEEDED:"))
             c2=150*f
             i="MUSTARD OIL"
             L1.append(i)
             str(f)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c2,f,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item is:",c2)
             cavalue+=c2
             
        if BH==4:
             f=int(input("ENTER HOW MUCH LITRES NEEDED:"))
             c2=170*f
             i="SESAME OIL"
             L1.append(i)
             str(f)
             sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c2,f,R1,R2)
             myc.execute(sql)
             conn.commit()
             print("the amount of the item is:",c2)
             cavalue+=c2

        if BH==5:
            f=int(input("ENTER HOW MUCH LITRES NEEDED:"))
            c2=170*f
            i="CASTOR OIL"
            L1.append(i)
            str(f)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c2,f,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c2)
            cavalue+=c2
        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        if q==0:
                print("THE SELECTED ITEMS;",L1)
                print("THE PRICES OF THE ITEMS ARE:",cavalue)
                
    if ch==5:
        print("1.BASMATHI RICE RS.100 \n")
        print("2.RAW RICE RS.80 \n")
        print("3.FLATTENED RICE RS.120\n")
        print("4.PUFFED RICE RS.50 \n")
        print("5.RAVAI RS.130 \n")
        print("6.CRACKED  WHEAT RS.120 \n")
        ZH=int(input("ENTER YOUR CHOICE:"))
        print("please enter it in numerical form for example half  kg -0.5 and quater kg-0.25")

        if ZH==1:
            RH=int(input("how many kgs needed:"))
            c1=100*RH
            i="BASMATHI RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c1,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c1)
            cavalue+=c1
            
        if ZH==2:
            RH=int(input("how many kgs needed:"))
            c2=80*RH
            i="RAW RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c2,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c2)
            cavalue+=c2

        if ZH==3:
            RH=int(input("how many kgs needed:"))
            c3=120*RH
            i="FLATTENED RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c3,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c3)
            cavalue+=c3

        if ZH==4:
            RH=int(input("how many kgs needed:"))
            c4=50*RH
            i="PUFFED RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c4,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c3)
            cavalue+=c4

        if ZH==5:
            RH=int(input("how many kgs needed:"))
            c5=130*RH
            i="BASMATHI RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c5,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c5)
            cavalue+=c5

        if ZH==6:
            RH=int(input("how many kgs needed:"))
            c6=120*RH
            i="CRACKED RICE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c6,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c6)
            cavalue+=c6

        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        
        if q==0:
                print("THE SELECTED ITEMS;",L1)
                print("THE PRICES OF THE ITEMS ARE:",cavalue)
                
             

    elif ch==6:
        print("1.GARAM MASALA RS.150 \n")
        print("2.SAMBAR POWDER RS.80 \n")
        print("3.RASAM POWDER RS.78 \n")
        print("4.BIRIYANI MASALA RS.120 \n")
        print("5.CHAAT MASALA RS 150 \n")
        DH=int(input("ENTER  YOUR CHOICE :"))

        if DH==1:
            RH=int(input("how many kgs needed:"))
            c6=120*RH
            str(RH)
            i="GARAM MASALA"
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c6,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c6)
            cavalue+=c6

        if DH==2:
            RH=int(input("how many kgs needed:"))
            c7=80*RH
            str(RH)
            i="SAMBAR POWDER"
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address) values('{}','{}',{},'{},'{}')".format(R,i,c7,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c7)
            cavalue+=c7
        if DH==3:
            RH=int(input("how many kgs needed:"))
            c8=78*RH
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity) values('{}','{}',{},'{}','{}')".format(R,i,c8,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            i="RASAM POWDER"
            L1.append(i)
            print("the amount of the item is:",c8)
            cavalue+=c8
        if DH==4:
            RH=int(input("how many kgs needed:"))
            k9=120*RH
            str(RH)
            i="BIRIYANI MASALA"
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity) values('{}','{}',{},'{}','{}')".format(R,i,k9,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",k9)
            cavalue+=k9
        if DH==5:
            RH=int(input("how many kgs needed:"))
            c10=150*RH
            i="CRACKED RICE"
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity) values('{}','{}',{},'{}','{}','{}')".format(R,i,c10,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c10)
            cavalue+=c10
        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        
        if q==0:
                print("THE SELECTED ITEMS;",L1)
                a="select item_name,price,quantity,delivery_address,phone_no from supermarket order by name"
                myc.execute(a)
                
                print("THE PRICES OF THE ITEMS ARE:",cavalue)
                 
                 

    elif ch==7:
        print("1.COFFEE POWDER [ SUNRISE,BRO,NARSUS,AV TEA COFFEE] RS.300\n")
        print("2.TEA POWDER [3ROSES,AV TEA,TAJMAHAL,AV TEA GOLD] RS.200\n")
        print("3.BOOST RS.300\n")
        print("4.HORLICKS RS.250\n")
        print("5.BORNVITA RS .300\n")
        JH=int(input("ENTER YOUR CHOICE:"))
        RH=int(input("how many kgs needed:"))

        if JH==1:
            c11=300*RH
            i="COFFEE"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c11,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c11)
            cavalue+=c11

        if JH==2:
            c12=200*RH
            i="TEA POWDER"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c12,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c12)
            cavalue+=c12

        if JH==3:
            c13=300*RH
            i="BOOST"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c13,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c13)
            cavalue+=c13

        if JH==4:
            c14=250*RH
            i="HORLICKS"
            L1.append(i)
            str(RH)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c14,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c14)
            cavalue+=c14

        if JH==5:
            c10=150*RH
            i="BORNVITA"
            str(RH)
            L1.append(i)
            sql="insert into supermarket (name,item_name,price,quantity,delivery_address,phone_no) values('{}','{}',{},'{}','{}','{}')".format(R,i,c10,RH,R1,R2)
            myc.execute(sql)
            conn.commit()
            print("the amount of the item is:",c10)
            cavalue+=c10

        q=int(input("ENTER 0 to end the purchase or 1 continue:"))
        
        if q==0:
                print("THE SELECTED ITEMS;",L1)
                print("THE PRICES OF THE ITEMS ARE:",cavalue)

             

 
                 
        

        


       


            


            

