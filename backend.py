import mysql.connector
f = open("credentials.txt")
mydb = mysql.connector.connect(host=f.readline(),user=f.readline(),password=f.readline())
print(mydb)
f.close()

mycursor = mydb.cursor()

#----------------------------------------------------------------------------------

#converts data to what i want (int)
def string_to_int(data):
    data = int (data)
    return data

#----------------------------------------------------------------------------------

def integer_checker(data):#checks if the entry is in int or not
    count = 0
    for i in data:
        if i in "0123456789":
            continue
        else:
            count = count + 1
            break
    if count == 0:
        return ("valid")
    else:
        return ("invalid")

#----------------------------------------------------------------------------------

#for table to display column names
def top_table():
  mycursor.execute("use zACM_enterprises")
  mycursor.execute("SELECT * FROM DISP_COLUMNS")
  myresult = mycursor.fetchall() 
  return myresult 

#----------------------------------------------------------------------------------

#for table to display column names
def top_table_trans():
  mycursor.execute("use zACM_enterprises")
  mycursor.execute("SELECT * FROM DISP_COLUMNS_TRANS")
  myresult = mycursor.fetchall() 
  return myresult 

#----------------------------------------------------------------------------------

#for table to display all data of your dept
def all_item(dept_id):
  mycursor.execute("use zACM_enterprises")
  if (dept_id == "admin"):
    mycursor.execute("SELECT * FROM INVENTORY_OF_ALL_ITEMS ")
  else:
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE DEPT_ID= %s "
    values = (dept_id, )
    mycursor.execute( sql , values )
  myresult = mycursor.fetchall()
  return myresult

#----------------------------------------------------------------------------------

#shows in_stock of the dept
def in_stock(dept_id):
  mycursor.execute("use zACM_enterprises")
  if (dept_id == "admin"):
    mycursor.execute("SELECT * FROM INVENTORY_OF_ALL_ITEMS ")
  else:
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE STATUS='IN' AND DEPT_ID= %s "
    values = (dept_id, )
    mycursor.execute( sql , values )
  myresult = mycursor.fetchall()
  return myresult

#----------------------------------------------------------------------------------

#shows out_stock of the dept
def out_stock(dept_id):
  mycursor.execute("use zACM_enterprises")
  if (dept_id == "admin"):
    mycursor.execute("SELECT * FROM INVENTORY_OF_ALL_ITEMS ")
  else:
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE STATUS='OUT' AND DEPT_ID= %s "
    values = (dept_id, )
    mycursor.execute( sql , values )
  myresult = mycursor.fetchall()
  return myresult

#----------------------------------------------------------------------------------

#shows all transaction of sold items of your dept
def transactions(dept_id):
    mycursor.execute("use zACM_enterprises")
    if (dept_id == "admin"):
      mycursor.execute("SELECT * FROM TRANSACTION_ITEM_DATA ")
    else:
      sql = "SELECT * FROM TRANSACTION_ITEM_DATA WHERE DEPT_ID= %s "
      values = (dept_id, )
      mycursor.execute( sql , values )
    myresult = mycursor.fetchall()
    return myresult 

#----------------------------------------------------------------------------------

# to check the item is in database or not
def item_present_or_not(item_id):
  mycursor.execute("use zACM_enterprises")
  mycursor.execute("SELECT * FROM INVENTORY_OF_ALL_ITEMS")
  myresult = mycursor.fetchall()
  for x in myresult:
    if (x[0] == item_id):     
      return ("present")  
      break
    else:  
      continue

#----------------------------------------------------------------------------------

#to add_items
def add_data(dept_id,name,price,quantity):
  if quantity == "0" :
    status = "OUT"
  else:
    status = "IN"
  mycursor.execute("use zACM_enterprises")
  sql = "INSERT INTO INVENTORY_OF_ALL_ITEMS(DEPT_ID,ITEM_NAME,ITEM_PRICE,QUANTITY,STATUS) VALUES (%s, %s, %s, %s, %s)"
  values = (dept_id,name,price,quantity,status)
  mycursor.execute( sql , values )
  mydb.commit()

#----------------------------------------------------------------------------------

#to delete_item
def delete_item(item_id):
  mycursor.execute("use zACM_enterprises")
  sql = "DELETE FROM INVENTORY_OF_ALL_ITEMS WHERE ITEM_ID = %s"
  values = (item_id, )
  mycursor.execute( sql , values )
  mydb.commit()

#----------------------------------------------------------------------------------

#to edit_item
def update_data(dept,name,price,quantity,item_id):
  if quantity == "0" :
    status = "OUT"
  else:
    status = "IN"
  mycursor.execute("use zACM_enterprises")
  sql = "UPDATE INVENTORY_OF_ALL_ITEMS SET  DEPT_ID= %s ,ITEM_NAME= %s ,ITEM_PRICE= %s ,QUANTITY= %s ,STATUS= %s WHERE ITEM_ID= %s "
  values = (dept,name,price,quantity,status,item_id)
  mycursor.execute( sql , values )
  mydb.commit()

#----------------------------------------------------------------------------------

#to edit_item new quantity after sold
def update_quantity(item_id,quantity):
    if quantity == 0 :
        status = "OUT"
    else:
        status = "IN"
    mycursor.execute("use zACM_enterprises")
    sql = "UPDATE INVENTORY_OF_ALL_ITEMS SET QUANTITY= %s , STATUS= %s WHERE ITEM_ID = %s"
    values = (quantity,status,item_id)
    mycursor.execute( sql , values )
    mydb.commit()

#----------------------------------------------------------------------------------

#check if sold quantity present in inventory
def quantity_checker(item_id,quantity):
    mycursor.execute("use zACM_enterprises")
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE ITEM_ID = %s "
    values = (item_id, )
    mycursor.execute( sql , values )
    myresult = mycursor.fetchall()
    for x in myresult:
        if ((x[0]==item_id)and(x[4]>=quantity)):
            new_quantity = x[4]-quantity
            return ("ok",new_quantity)
        else:         
            break
    return ("no")

#----------------------------------------------------------------------------------

#check item present for that dept
def dept_and_item_id_checker(dept_id,item_id):
    mycursor.execute("use zACM_enterprises")
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE ITEM_ID = %s "
    values = (item_id, )
    mycursor.execute( sql , values )
    myresult = mycursor.fetchall()
    for x in myresult:   
        if ((x[0]==item_id)and(x[1]==dept_id)):
            return ("ok")
            break
        else:
            continue

#----------------------------------------------------------------------------------

def name_acquire(name_of_user,pass_of_user):
    mycursor.execute("use zACM_enterprises")
    mycursor.execute("SELECT * FROM USER_LOGIN_DATA")
    myresult = mycursor.fetchall()
    for x in myresult:
      if (x[1]==name_of_user)and(x[2]==pass_of_user):
        return ("found",x[3])
        break
      else:
        continue
    return ("notfound")
    
#----------------------------------------------------------------------------------
  
#to add data to transaction table
def get_sell_result_and_update_trans(item_id,sold_quantity,quantity_left):
    mycursor.execute("use zACM_enterprises")
    sql = "SELECT * FROM INVENTORY_OF_ALL_ITEMS WHERE ITEM_ID = %s "
    values = (item_id , )
    mycursor.execute( sql , values )
    myresult = mycursor.fetchall()
    for x in myresult:
      
      dept_name = x[1]
      name = x[2]
      price = x[3]
      
      mycursor.execute("use zACM_enterprises")
      sql = "INSERT INTO TRANSACTION_ITEM_DATA(ITEM_ID,DEPT_ID,ITEM_NAME,ITEM_PRICE,QUANTITY,UNITS_LEFT) VALUES (%s ,%s, %s, %s, %s, %s)"
      values = (item_id,dept_name,name,price,sold_quantity,quantity_left)
      mycursor.execute( sql , values )
      mydb.commit()
      
#----------------------------------------------------------------------------------

def billing_table(dept_id):
    sum = 0
    mycursor.execute("use zACM_enterprises")
    if (dept_id == "admin"):
      mycursor.execute("SELECT * FROM TRANSACTION_ITEM_DATA ")
    else:
      sql = "SELECT * FROM TRANSACTION_ITEM_DATA WHERE DEPT_ID= %s "
      values = (dept_id, )
      mycursor.execute( sql , values )
    myresult = mycursor.fetchall()
    for x in myresult:
      # print(x)
      data1 = string_to_int(x[4])
      data2 = string_to_int(x[5])
      sum = (data1 * data2) + sum 
    bill = [("","","","","TOTAL = ",sum),""]
    return bill
    
#----------------------------------------------------------------------------------