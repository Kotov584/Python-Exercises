room_list = ['Noob', 'Pro', 'Elite', 'Luxury']
user_lvl = 0
current_room = ''   
print("Welcome!\r\nThis is a Mini TextBased Adventure Game developed by Vladyslav Kotov.")
ask_start = input("Do you want start game?\r\nType yes or no: ")
if ask_start == 'yes':
  print("Nice!\r\nLet's get started!")
  ask_username = input("Firstly, I need your name: ")
  print(ask_username,", Nice to meet you!")
  ask_choose_room = input("Do you want to choose room?\r\nType yes or no: ")
  if ask_choose_room == 'yes':
    print("Here is our rooms list:")
    for i in range(4):
      print("Room: ", room_list[i])
    ask_room = input("Write room in which you want to enter: ")
    while ask_room != 'Noob' and ask_room != 'Pro' and ask_room != 'Elite' and ask_room != 'Luxury':
      ask_room = input("Write room in which you want to enter correctly: ")
    if ask_room == 'Noob':
      if user_lvl >= 0:
        user_lvl += 1
        print("Welcome to the Noob Room! Your lvl has been increased.")
        print("Your current lvl: ", user_lvl)
        current_room = 'Noob'
    elif ask_room == 'Pro':
      if user_lvl < 1:
        print("You can't enter this room!\r\nYour game has been finished!")
      else: 
        print("Welcome to the Pro Room!\r\nYour lvl has been increased.\r\nYour current lvl: ", user_lvl)
        user_lvl += 1
        current_room = 'Pro'
    elif ask_room == 'Elite':
      if user_lvl < 2:
         print("You can't enter this room!\r\nYour game has been finished!")
      else: 
        print("Welcome to the Elite Room!\r\nYour lvl has been increased.\r\nYour current lvl: ", user_lvl)
        user_lvl += 1
        current_room = 'Elite'
    elif ask_room == 'Luxury':
      if user_lvl < 3:
         print("You can't enter this room!\r\nYour game has been finished!")
      else: 
        print("Welcome to the Luxury Room!\r\nYour lvl has been increased.\r\nYour current lvl: ", user_lvl)
        user_lvl += 1
        current_room = 'Luxury'
  while current_room != '':
    ask_choose_room = input("Do you want to change your room?\r\nType yes or no: ")
    while ask_choose_room == 'yes':
      ask_choose_room = input("Type room in which you want to enter:")
      while ask_choose_room != 'Noob' and ask_choose_room != 'Pro' and ask_choose_room != 'Elite' and ask_choose_room != 'Luxury':
        ask_choose_room = input("Write room in which you want to enter correctly: ")
      current_room = ask_choose_room
      user_lvl += 1
      print("You changed your room to: ", ask_choose_room)
      print("You lvl has been increased\r\nYour current lvl is: ", user_lvl)
    else:
        print("You has been finished your game!")
        print("Your statitistics: ")
        print("Room: ", current_room)
        print("LVL: ", user_lvl)
        break
else:
  print("You has been finished your game!")
  print("Your statitistics: ")
  print("Room: ", current_room)
  print("LVL: ", user_lvl)
