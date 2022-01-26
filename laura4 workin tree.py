from rich import print


P1 = str(input('Player1, enter your name: '))

P2 = str(input('Player2, enter your name: '))

columns = {
    # column : counter
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
}


# def taketurn(aplayer):
#    while player1move is True:

#    while player2move is True:


true = True


def countachip(currentPlayer):
    while true == True:
        UI1 = input(currentPlayer + ', Enter a row number to put down your chip: ')

        isuiadigit = UI1.isdigit()
     #if input isnt a digit
        
        #if input is a digit
        while UI1.isdigit() == True:
            for i in columns.keys():
                 #if user input is the same as a column number
                     if UI1 == i:
                        if columns[UI1] <= 6:
                             columns[UI1] += 1
                             print("X pos is ", UI1, "Y pos is", columns[UI1]) 
                        elif columns[UI1] == 7:
                             UI1 = int(input(
                                 currentPlayer + ',This row is full. Enter a diferent row number to put down your chip: '))
                        elif UI1 == str:
                             print("Sorry, that is not a column number")
                    
        if isuiadigit == False:
            UI1 = input(currentPlayer + ', That is not a number. Enter a row number to put down your chip: ')


                # check if column is full
                # if y position isnt full add 1


    


       # add 1 to count1




#print (P1)

#playerturn = 0
#while player1 == True:
  #   if playerturn == 0:  
         
   #      playerturn += 1
   #      #countachip(P1)
   #      countachip(P1)

   #  else:
         #countachip(P2)
       #      playerturn -= 1
       #      countachip(P2)






#print (countachip(P2))
#countachip(P2)

while true == True:
 hey = True

 if hey == True:
    countachip(P1)
    hey == False
    if hey == False:
        countachip(P2)
        hey ==True

def greet(name1, name2):
    greetings = "Hello, " + name1 + " and " + name2 + "!"
    greetings += " Welcome to Connect 4"
    return greetings

# print(greet(P1, P2))


# def drawmap (coords):


# everytime taketurn is called it asks for a colummn to input a piece
# def taketurn (aplayer):
    # print player x take turn
    # take in column player is going to use
    # calculate the coords that their counter ends up at

    # check list of counter, how many counters havebeen called before in this column?
    # ex: how many counters have an x pos of 7?
    # logic that adds counter to a list of counters


# def manager ():
    # while #gameisstillgoing p1 take a turn, p2 take a turn.


emptymap = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   | x |   |   |   |   |   | ",
    "|   | x |   |   |   |   |   | ",
    "|   |o  | o |   | x |   |   | ",
    "————————————————————————————— ",
]
# agnes 5:1
# laura 2:1
# agnes 2:2
# laura 3:1
# agnes 2:3

counter1 = {
    "x": 2,
    "y": 1,
    "s": "o"}

counter2 = {
    "x": 2,
    "y": 2,
    "s": "x"}

# create a variable counter3 , counter3.x = 7forex
# ask computer how may times "7"for ex has been called before
# have a list of all of the counters that are in the game

# print (emptymap)


row1ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "| X |   |   |   |   |   |   | ",
    "————————————————————————————— ",
]

row2ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   | X |   |   |   |   |   | ",
    "————————————————————————————— ",
]

row3ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   | X |   |   |   |   | ",
    "————————————————————————————— ",
]

row4ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   | X |   |   |   | ",
    "————————————————————————————— ",
]

row5ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   | X |   |   | ",
    "————————————————————————————— ",
]

row6ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   | X |   | ",
    "————————————————————————————— ",
]

row7ax = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   | X | ",
    "————————————————————————————— ",
]

row1ao = [
    "  1   2   3   4   5   6   7   ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "| O |   |   |   |   |   |   | ",
    "————————————————————————————— ",
]

# if UI1 == "1":
#     print (row1ax)
# elif UI1 == "2":
#    print (row2ax)
# elif UI1 == "3":
#    print(row3ax)
# elif UI1 == "4":
#    print(row4ax)
# elif UI1 == "5":
#    print(row5ax)
# elif UI1 == "6":
#   print(row6ax)
# elif UI1 == "7":
#    print(row7ax)


# UI2 = str(input(P2 + ', Enter a row number to put down your chip: '))
