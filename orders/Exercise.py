# IMPORT PYTHON LIBRARIES  #
import os
# START PROGRAM FUNCTIONS #
# --- FUNCTION TO GET DATA FROM FILE IN MASSIVE --- #
def get_data (filename,splittype):
    f=open(filename, "r")
    fileinfo=f.readlines()
    f.close()
    for i in range(len(fileinfo)): 
        fileinfo[i]=fileinfo[i].split(splittype)
    return fileinfo 
# --- FUNCTION TO CHECK AUTH --- #
def check_auth (staff, username, password):
    auth_check = 'no' 
    for stafff in staff:
          if stafff[0] == username:
            if stafff[1] == password: 
              auth_check = 'yes' 
    if auth_check == 'no':
      print("Auth check failed!")
      os._exit(0)
    else:
      print("Auth success!")
# LOADING DATA FROM FILES #
staff = get_data("Staff.txt", ',')
# WELCOME MESSAGE  #
username = input("Welcome!\r\nWrite your username:\r\n")
print("Hello,",username)
password = input("Write your password: \r\n")
check_auth(staff,username,password)
# PROGRAM EXECUTION #
# LOADING DATA FROM FILES #
orders = get_data("Orders.txt",',')
userinput = input("Write letter according to documentation: \r\n")
while userinput != 'X':
  if userinput == 'O':
    orders = get_data("Orders.txt",',')
    print("Your orders:\r\n# Name Adress Date Amount\r\n")
    for order in orders:
      if order[0] == '':
        print("You dont have any orders yet!")
      else:
        print("%s %s %s %s %s" %(order[0],order[1],order[2],order[3],order[4]))
  elif userinput == 'S':
    print("What kind of data you want to see?\r\nWrite S1 to see numbers of order placed by one specific customer\r\nWrite S2 to see number of orders in one specific day\r\nWrite S3 to see total amount of all orders delivered\r\nWrite S4 to see total amount of the orders placed by a specific customer\r\nWrite S5 to see Total amount of the orders placed by a specific day\r\n")
  elif userinput == 'S1':
    customer_name = input("Write customer name: \r\n")      
    total_orders = 0
    for order in orders:
      if order[1] == customer_name:
        total_orders = total_orders + 1
    order_word = "order"
    if total_orders > 4:
      order_word = "orders"
    print("Customer %s have %s %s" %(customer_name, total_orders,order_word))
  elif userinput == 'S2':
    total_number = 0
    specific_day = int(input("Write a specific day: "))
    for order in orders:
      a_string = order[3]
      split_strings = []
      n  = 2
      for index in range(0, len(a_string), n):
          split_strings.append(a_string[index : index + n])
      if int(split_strings[0]) == specific_day:
        total_number = total_number + 1
    print("Total number of orders in this %s day is %s" %(specific_day, total_number))
  elif userinput == 'S3':
    total_amount = 0
    for order in orders:
      order[4] = int(order[4])
      total_amount = total_amount + order[4]
    print("Total amount of all orders delivered %s" %(total_amount))
  elif userinput == 'S4':
    customer_name = input("Write customer name: \r\n")      
    total_amount = 0
    for order in orders:
      order[4] = int(order[4])
      if order[1] == customer_name:
        total_amount = total_amount + order[4]
    print("Customer %s have total amount of the orders %s" %(customer_name, total_amount))
  elif userinput == 'S5':
    total_amount = 0
    specific_day = int(input("Write a specific day: "))
    for order in orders:
      a_string = order[3]
      split_strings = []
      n  = 2
      for index in range(0, len(a_string), n):
          split_strings.append(a_string[index : index + n])
      if int(split_strings[0]) == specific_day:
        total_amount = total_amount + int(order[4])
    print("Total number of orders in this %s day is %s" %(specific_day, total_amount))
  elif userinput == 'W': #Writing data
    orders = get_data("Orders.txt",',')
    generate_id = 1
    for order in orders:
      if order[1] == '':
        generate_id = 1
      else:
        generate_id = generate_id + 1
    generate_id = str(generate_id)
    try:
      customer_name = input("Write customer name: \r\n")      
      customer_adress = input("Write customer adress: \r\n")
      customer_date = int(input("Write customer date (DDMMYY): \r\n"))
      customer_total_amount = int(input("Write customer total amount of order: \r\n"))
      f = open('Orders.txt','a')
      writedata = generate_id + "," + customer_name + "," + customer_adress + "," + customer_date + "," + customer_total_amount + "\n"
      f.write(writedata)
      f.close() 
      print("New order have been saved!")
    except:
      print('Fatal error: Not correct data!')
  elif userinput == 'ETXT': #Exporting data in txt
    try:
      print("Started exporting data in txt.")   
      for order in orders:
        filename = 'ExportData.txt'
        if os.path.exists('ExportData.txt'):
          append_write = 'a' # append if already exists
        else:
          append_write = 'w' # make a new file if not
        f = open(filename,append_write)
        writedata = order[0] + ',' + order[1] + ',' + order[2] + ',' + order[3] + ',' + order[4] + "\r\n"
        f.write(writedata)
        f.close() 
      print("Data successfully was exported!")
    except:
      print('Fatal error: Not correct data!')
  elif userinput == "UTXT":
    upload_data = get_data("import_orders.txt", ',')
    filename = 'Orders.txt'
    if os.path.exists('Orders.txt'):
      append_write = 'a' # append if already exists
    else:
      append_write = 'w' # make a new file if not
    f = open(filename,append_write)
    for order in upload_data:     
      writedata = order[0] + ',' + order[1] + ',' + order[2] + ',' + order[3] + ',' + order[4] + "\n"
      f.write(writedata)
    f.close() 
  userinput = input("Write letter according to documentation:\r\n")
os._exit(0)




