#python2.7.13
#Shelley Tennison
# Demonstrating hoe to pass variables from function to function
# while producing a functional game.



def start(nice=0,mean=0,name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    
def describe_game(name):
    """ check if this is a new game or not.
        if it is new get user's name.
        if it is not a new game thank user for
        playing again and continue with the game.
    """
    if name !="": #meaning if we do not have the user's name they are a new player.
        print("\nThank you for playing again, ()!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greated by several different people. \nYou can be nice or mean.")
                    print("At the end of the game you fate will be influenced from your actions.")
                    stop = False
    return name
                    
def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? n/m: ").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingle and abruptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #passes the three variables to the score.

def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, nice) and ({}, mean) points.".format(name,nice,mean))

def score(nice,mean,name):
          #score function if being passed the values stored with the three variables.
          if nice > 5: #if condition is valid call win function.
              win(nice,mean,name)
          if mean > 5: #if condition is valid call lose function.
              lose(nice,mean,name)
                        #else call nice_mean function passing the variables.
          else:
              nice_mean(nice,mean,name)

def win(nice,mean,name):
          print("\nNice job {}, you win! \nEveryone loves you and you live in a palace!".format(name))
          again(nice,mean,name) #call again function will pass our variables

def lose(nice,mean,name):
          print("\nToo bad, game over! {}, you live in a van down by the river,  wretched and scorned!".format(name))
          again(nice,mean,name)

def again(nice,mean,name):
          stop = True
          while stop:
              choice = raw_input("\nDo you want to play agian? y/n: ").lower()
              if choice == "y":
                  stop = False
                  reset(nice,mean,name)
              if choice == "n":
                  print("\nSee you later alligator!")
                  stop = False
                  exit()
              else:
                  print("\nPlease enter 'y' for 'YES' and 'n' for 'No'...")

def reset(nice,mean,name):
          nice = 0
          mean = 0
          #notice you do not have to reset the name variable.
          start(nice,mean,name)

if __name__ == "__main__":
    start()
