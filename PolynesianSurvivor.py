#Mora's Choose Your Own (Polynesian Island) Adventure Game

import random

#Print greeting/story opening to user:
def introduction():
  """Prints game intro to user"""
  print("Hey wake up, I have some bad news.")
  print()
  print("Don't panic but you are falling out of a plane right now.")
  print()
  print("Don't worry though! I strapped a parachute to you and the island below us looks lush and green with crystal clear turquiose water surrounding it. ")
  print()

  
#Ask for user's name and return greeting: 
def user_name():
  """Asks user for name and returns greeting"""
  user_name = input("What's your name? ")
  print()
  print(f"Good to meet you {user_name.title()}. I wish our first meeting was under better circumstances.")
  

#Create timer:

import time


def timer():
  timer = 5

  while timer > 0:
    print(timer, "...")
    time.sleep(1)
    timer = timer - 1

  
#Let's user know they are approaching island and establishes what "mauka" and "makai" are:
def ask_user_for_direction():
  """As user approaches island prints question to user"""
  print("We don't have much time.")
  print()
  print("Tell me should we go mauka (towards the mountains) or makai (towards the ocean)?")
  print()


#Ask user for direction choice:
def direction_chosen():
  """Asks user for direction choice, direction determines which action options are available later"""
  direction_chosen = input("Enter [mauka] or [makai]: " )
  direction_chosen = direction_chosen.lower()
  
  if direction_chosen == "mauka":
    print()
    print(f"Okay {direction_chosen}. Good choice. We'll probably find lots of fruit and other edible plants there. Take my hand, I'll help you land.")
    print()
    timer()
    print("We made it to the mauna (mountain). It's a little steep on the surface but there are lots of vines to hang on to.")
    print()
   
  elif direction_chosen == "makai":
    print()
    print(f"Okay {direction_chosen}. Good choice. We'll probably find lots of fish and coconut trees there. Take my hand, I'll help you land.")
    print()
    timer()
    print("We made it to the kahakai (beach). It looks like there are big waves right now so let's stay away from the water for now so we don't get pulled out by the rip current. ")
    print()
    
  else:
    print()
    print("I'm sorry that isn't an option. Now you are going to crash!")
    timer()
    print("You died.")
    try_again_mauka_or_makai()

  return direction_chosen

# direction_input = direction()

def try_again_mauka_or_makai():
  """What happens if user needs to input direction again in case of misspelling of mauka or makai"""
  try_again_mauka_or_makai = input("Try again? [Y]es or [N]o")
  try_again_mauka_or_makai = try_again_mauka_or_makai.upper()
  if try_again_mauka_or_makai == "Y":
    direction_chosen()
  elif try_again_mauka_or_makai == "N":
    print("Game over.")
  else:
    print("I'm sorry that isn't an option.")
    try_again_mauka_or_makai()
    

#Blank lists for food and tools that can be appended as user does actions:
food = []
tools = []

#Adding lists of makai tools and food and mauka tools and food to randomly pick from list:

mauka_foods = ["papayas", "bananas", "guavas"]
mauka_tools = ["spear", "kukui nuts"]

makai_foods = ["coconuts", "bananas", "fish"]
makai_tools = ["net", "spear", "leiomano"]

#Adding lists of encounters during movements to randomly pick from list:

left_movements = ["mongoose", "leg"]
right_movements = ["boar", "arm"]
straight_movements = ["feet further 1", "rescue"]


#Define action options for user:
def action_options(direction_chosen):
  """User's action options: based on direction user first picks, action option that is selected will have different outcomes"""
  action_options = input("Do you want to : \n[G]ather fruit and edibles plants, \n[F]ashion tools, \n[M]ove or \n[A]ccess inventory? \n")
  action_options = action_options.upper()
  if action_options == "G":
    gather_food(direction_chosen)
  elif action_options == "F":
    fashion_tools(direction_chosen)
  elif action_options == "M":
    movement_input()
  elif action_options == "A":
    access_inventory()

#Gather food:
def gather_food(direction_chosen):
  """What happens if user inputs [G]ather food"""
  
  #mauka options:
  if direction_chosen == "mauka":
    random_food_mauka = random.choice(mauka_foods)
    print()
    
    if random_food_mauka == "papayas":
      print("I see a papaya tree in the distance. Let's gather some.")
      food.append("papayas")
      
    elif random_food_mauka == "bananas":
      print("There is a banana tree nearby. We will pull off the bunch that looks a little yellow already with the flower drying up at the end.")
      food.append("bananas")
      
    elif random_food_mauka == "guavas":
      print("There are some guava bushes nearby. Let's gather some.")
      food.append("guavas")

  #makai options:
  elif direction_chosen == "makai":
    random_food_makai = random.choice(makai_foods)

    if random_food_makai == "coconuts":
      print("I see a niu (coconut) tree. I will climb up and shake down some coconuts. Watch your head! ")
      food.append("coconuts")
      
    elif random_food_makai == "bananas":
      print("There is a patch of banana trees a little further down the kahakai (beach). We will pull off a bunch that looks a little yellow already with the flower drying up at the end.")
      food.append("bananas")
      
    elif random_food_makai == "fish":
      #fishing is complicated, will print different strings based on tools in inventory
      print("It's time to go get some fish!")
      if tools == ["net"]:
        print("We will use the niu net to make fishing easier.")
      elif tools == ["spear"]:
        print("We can use your spear to spearfish. Keep your eye out for the blue uhu (parrotfish) and the red 'aweoweo (Hawaiian glasseye).")
      else:
        print("We are going to try to fish barehanded since we have no tools. Let's stick to the shallows to try to find a he'e (octopus) in the rocks. But be careful 'cause those buggers bite!")
      food.append("fish")

  print()
      

#Fashion tools:
def fashion_tools(direction_chosen):
  """What happens if user [F]ashions tools"""
  
    #mauka options:
  if direction_chosen == "mauka":
    random_mauka_tool = random.choice(mauka_tools)
    print()

    if random_mauka_tool == "spear":
      print("I see an 'ohi'a tree and a kukui nut tree. The 'ohi'a has those flowers that look like red puffballs called lehua. We can take some of the wood from that tree (as it isn't rare like the koa tree) and make a spear. We'll also add some kukui nuts to the spear in case we need to make noise to ward off any animals. ")
      tools.append("spear")

    elif random_mauka_tool == "kukui nuts":
      print("I see a kukui nut tree. The kukui nuts have lots of oil in them and they are great for starting fires. They light up really easily. Let's gather some!")
      tools.append("kukui_nuts") 

    #makai options:
    elif direction_chosen == "makai":
      random_makai_tool = random.choice(makai_tools)

      if random_makai_tool == "net":
        print("Let's weave some baskets from these fallen niu (coconut) fronds. We can use them for fishing.")
        tools.append("net") 

      elif random_makai_tool == "leiomano":
        print("I see some fallen koa wood under the tree over there. We can use that and these shark teeth on the beach to make a leiomano ('shark's lei'). It's a small hand weapon that we can use for lots of things.")
        tools.append("leiomano")

      elif random_makai_tool == "spear":
        print("There is some bamboo growing that looks quite mature and tall. We will cut down a piece of it and sharpen one end to create a spear. We'll also add some fallen kukui nuts to our spear so we can shake it to make noise in case we encounter an animal.")
        tools.append("spear")

  print()


def movement_input():
  """Prompts user to input direction of movement"""
  movement_input = input("Do you want to go: [L]eft, \n[R]ight, or \n[S]traight)? ")
  movement_input = movement_input.upper()
  print()

  
# def get_movement_input(direction_chosen):
#   """What happens when user chooses [M]ovement"""
#   movement_input()
  
  
  #if Left:
  if movement_input == "L":
    go_left = random.choice(left_movements)
    
    #if mongoose:
    if go_left == "mongoose":
      print("Oh no! You have encountered a rogue mongoose!")
      
      if tools == []:
        print("You have no tools to use. Make some noise and jump up and down!")
      
      elif tools == ["net"]:
        print("You can trap it with your net.")
      
      elif tools == ["spear"]:
        print("You can use your spear! Throw it or make noise with the kukui nuts.")

      elif tools == ["leiomano"]:
        print("Wield your leiomano and charge at the mongoose while making lots of noise so it will run off.")

      elif tools == ["kukui nuts"]:
        print("Throw some kukui nuts in the direction of the mongoose to scare it away.")

      else:
        print("Run away!")
   
    #if leg:
    elif go_left == "leg":
      print("Oh no! You fell and hurt your leg!")
      if food == []:
        print("You have no food to reenergize yourself.")

      elif food == ["papayas"]:
        print("Eat one of your papayas. Good now you are feeling better and your mana is restored.")
      
      elif food == ["coconuts"] and tools == []:
        print("Cracking open a coconut will give you energy but you have no tools to break it open.")
      
      elif food == ["coconuts"] and tools == ["spear"]:
        print("We can crack the coconut open with your spear. The coconut water and meat will restore your mana.")
      
      elif food == ["coconuts"] and tools == ["net"]:
        print("Cracking open a coconut will restore your mana but the niu net won't help you open it. I'll find a rock to break it open.")
        print("*WHACK* There, mana restored!")
        
      elif food == ["bananas"]:
          print("You eat some bananas and restore your mana!")
        
#if Right:
  elif movement_input == "R":
    go_right = random.choice(right_movements)

    #if boar:
    if go_right == "boar":
      print("There is a wild boar headed our way!")
      
      if food == [] and tools == []:
        print("You have no food to distract the boar or tools to defend yourself. You died.")
        play_game()

      elif food == ["papayas"]:
        print()
        print("Toss a papaya at the boar to distract it while we get away.")

      elif food == ["bananas"]:
        print()
        print("Throw your bananas at the boar to distract it while we get away.")

      elif food == ["coconuts"] and tools == []:
        print()
        print("Throw a coconut at the boar!")

      elif food == ["fish"] and tools == []:
        print()
        print("Throw some fish at the boar to distract it while we get away.")

      elif tools == ["spear"]:
        print()
        print("Shake your spear to make some noise to scare away the boar. You can also try to throw your spear but boars run incredibly fast and there's a good chance you will miss.")

      elif tools == ["net"] and food == []:
        print()
        print("Try throw the net at the boar to distract it while we run away.")

      elif tools == ["leiomano"]:
        print()
        print("Use your leiomano to charge at the boar. Make lots of loud noise though because the leiomano isn't very large.")

    #elif arm:
    elif go_right == "arm":
      print("You tripped and hurt your shoulder trying to stop your fall.")

      #***Add conditionals to restore mana***

#elif Straight:
  #if feet further 1:
  elif movement_input == "S":
    go_straight = random.choice(straight_movements)
    if movement_input == "S" and direction_chosen == "mauka" and go_straight == "feet further 1:":
      print("You have made it a few more feet down the mauna (mountain).")

    elif movement_input == "S" and direction_chosen == "makai" and go_straight == "feet further 1":
      print(" You have made it a few more feet down the kahakai (beach).")

  #if rescue:
    elif movement_input == "S" and direction_chosen == "mauka" and go_straight == "rescue":
      print()
      print("You have made it a few more feet down the mauna (mountain). And there is a helicopter flying overhead. Wave your arms to get rescued!")

    elif movement_input == "S" and direction_chosen == "makai" and go_straight == "rescue":
      print()
      print(" You have made it a few more feet down the kahakai (beach). And a canoe is approaching! Wave your arms to get their attention.")

  else:
    print("I'm sorry that's not an option.")
    movement_input()

  print()
    
def access_inventory():
  access_inventory = input("Would you like to see your [food] or [tools]?")
  access_inventory = access_inventory.lower()

  if access_inventory == "food":
    if food == []:
      print("You have no food.")
    else:
      print(food)

  elif access_inventory == "tools":
    if tools == []:
      print("You have no tools")
    else:
      print(tools)

  else:
    print("That isn't an option.")
    try_again_inventory()

def try_again_inventory():
  """What happens if user needs to try to access inventory again because of misspelling or needs to try another action"""
  try_again_inventory = input("Would you like to access your inventory again? [Y]es or [N]o")
  try_again_inventory = try_again_inventory.upper()
  if try_again_mauka_or_makai == "Y":
    access_inventory()
  elif try_again_inventory == "N":
    action_options(direction_chosen)
  else:
    print("That isn't an option.")
    try_again_inventory()
    

# user_direction = direction_chosen()
# direction_chosen(user_direction)

def play_game():
  introduction()
  user_name()
  print()
  ask_user_for_direction()
  user_direction = direction_chosen()
  print()
  while user_direction == "mauka" or "makai":
    action_options(user_direction)


play_game()


# check_winner function in TTT game
# for x in range(len(variable)):
#     for y in range(5):
#         print(x,y)