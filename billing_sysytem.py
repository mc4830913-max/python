import time
fd=open("inventory.text","r")
txt=fd.read()

#entering the inputs
user_name=input("enter the username:")
user_phone_no=input("enter the phone number:")
user_email_id=input("enter the email_id:")
uni_product_id=input("enter the product id:")
uni_product_qn=input("enter the product quantity:")

#updated list saved here
product_updated_lst=[]

#go thorugh with each products
for product in txt.split("\n"):
    if product.strip() == "":
        continue
    product_detail=product.split(',')

    #checking that product is exist in data 
    if(product_detail[0]==uni_product_id):

        #checking the user prduct quantity avaliable in data set 
        if(int(uni_product_qn) <=int(product_detail[3])):
            print("_________________________")
            print("product_name:        ",product_detail[1])
            print("product_price:       ",product_detail[2])
            print("product_quantity:    ",uni_product_qn)
            print("_________________________")
            print("total_amount:        ",int(product_detail[2])*int(uni_product_qn))
            print("_________________________")
            found=True

            #updating inventory list
            product_detail[3]=str(int(product_detail[3])-int(uni_product_qn))

            #generating the sales file of the product puchase
            fd=open("Sales.text","a")
            Sales_details=user_name+","+user_phone_no+","+user_email_id+","+uni_product_qn+","+product_detail[1]+","+str(int(product_detail[2])*int(uni_product_qn))+","+time.ctime()+"\n"
            fd.write(Sales_details)
            fd.close()
        
            #otherwise print user what they want
        else:
            print("we have not enought quantity")
            print("we have only",product_detail[3],"quantity")
            print("would you like to puchase it")

            #if they want the item that we have then make bill
            ch=input("enter Y/N if you want")
            if(ch=='Y' or ch=='y'):
                print("_________________________")
                print("product_name:        ",product_detail[1])
                print("product_price:       ",product_detail[2])
                print("product_quantity:    ",product_detail[3])
                print("_________________________")
                print("total_amount:        ",int(product_detail[2])*int(product_detail[3]))
                print("_________________________") 

                #generating the sales file of the product puchase
                fd=open("Sales.text","a")
                Sales_details=user_name+","+user_phone_no+","+user_email_id+","+product_detail[3]+","+product_detail[1]+","+str(int(product_detail[2])*int(product_detail[3]))+","+time.ctime()+"\n"        
                fd.write(Sales_details)
                fd.close()

                #updating inventory list
                product_detail[3]='0' 
            else:
                print("thanks")
        
     #here apending the list 
    product_detail
    product_updated_lst.append(product_detail)

if not found:
    print("product ifd is not avialble")

#the unnecessery  space is removed from the list
lst=[]
for i in product_updated_lst:
    pro=i[0]+","+i[1]+","+i[2]+","+i[3]+"\n"
    lst.append(pro)

    #at the end of list
lst[-1]=lst[-1][:-1]
fd=open("inventory.text","w")

#updtae inventory in the text file
for i in lst:
    fd.write(i)
fd.close()    

print("-----------------------------")
print("inventory updated")

using the json file billing system

record={1001:{"Name":"dairy milk",      "price":100,"Qn":200},
        1002:{"Name":"kitkat",          "price":50,"Qn":250},
        1003:{"Name":"milky",           "price":60,"Qn":100},
        1004:{"Name":"chocolate cake",  "price":75,"Qn":150},
        1005:{"Name":"5 star",           "price":40,"Qn":190}}


import json
fd=open("Record.json","r")
js=fd.read()
fd.close()

record=json.loads(js)
print("---------------MENU--------------------")
for key in record.keys():
    print(key,":",record[key]["Name"],"|",record[key]["price"],"|",record[key]["Qn"])
print("---------------------------------------")
ui_pr=str(input("enter the product id:"))
ui_qn=int(input("enter the product quantity:"))

record[ui_pr]["Qn"]=record[ui_pr]["Qn"]-ui_qn
print("-----------------------------------------")
print("                  BILL                   ")
print("Name                  :",record[ui_pr]["Name"])
print("Price                 :",record[ui_pr]["price"])
print("quantity              :",ui_qn)
print("-------------billing amount--------------")
print("Billing_Amount         :",record[ui_pr]["price"]*ui_qn)
print("-----------------------------------------")

js=json.dumps(record)

fd=open("Record.json","w")
fd.write(js)
fd.close()



