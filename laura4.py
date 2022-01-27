from rich import print


P1 = str(input('Player1, enter your name: '))

P2 = str(input('Player2, enter your name: '))

player1 = { 1: P1, 2: "|x|" }
player2 = { 1: P2, 2: "|o|"}


#print("Hello, " + P1 + " and " + P2 + "!"+ " Welcome to Connect 4")
    


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


true = True


emptymap = [
    "  1   2   3   4   5   6   7   ",
    "| 1 |   |   |   |   |   |   | ",
    "| b |   |   |   |   |   |   | ",
    "| c |   |   |   |   |   |   | ",
    "| d |   |   |   |   |   |   | ",
    "| e |   |   |   |   |   |   | ",
    "| f |   |   |   |   |   |   | ",
    "| g |   |   |   |   |   |   | ",
    "| 2 |   |   |   |   |   |   | ",
    "————————————————————————————— ",
]


chiplog= []

def countachip(currentPlayer):

    taketurn = False

    while taketurn  == False:
        #currentPlayer[1] accesses name, Currentplayer[2]" accesses chip x or o
        UI1 = input(str(currentPlayer[1]) + ', Enter a row number to put down your chip: ')
        isuiadigit = UI1.isdigit()
        print(isuiadigit)
        if isuiadigit == True :
            taketurn = True
        else: print(str(currentPlayer[1]) + ", That wasn't a number.")


    for i in columns.keys():
                #if user input is the same as a column number
        #print (UI1, i)
        UI1 = int(UI1)
        if UI1 == i:
            if columns[UI1] >= -6:
                columns[UI1] -= 1
                chippos = UI1 , columns[UI1]
                chiplog.insert(1, chippos)
                print(chiplog)
                print (chiplog[0], "hi")

                
                print("X pos is ", UI1, "Y pos is", columns[UI1]) 
            elif columns[UI1] == -7:
                UI1 = int(input(
                    str(currentPlayer[1])  + ',This row is full. Enter a diferent row number to put down your chip: '))
            elif UI1 == str:
                print("Sorry, that is not a column number")
                    
    if isuiadigit == False:
        UI1 = input(str(currentPlayer[1])  + ', That is not a number. Enter a row number to put down your chip: ')
    
     
    #for i in chiplog:
         #for j in i:
             #print (i[0], i[1], "yeiie")
    
    for i in range(7):
        print("")
        for j in range(7):
            
            for b in chiplog:

                if i == b[0]: #and j == b[1]:
                     
                     print(currentPlayer[2], end =  "")
            
            print ("| |", end = "")
                 
    print("")  

                
                 

while true == True:
     countachip(player1)
     countachip(player2)





# def drawmap (coords):


# everytime taketurn is called it asks for a colummn to input a piece
# def taketurn (aplayer):
    # print player x take turn
    # take in column player is going to use
    # calculate the coords that their counter ends up at

    # check list of counter, how many counters havebeen called before in this column?
    # ex: how many counters have an x pos of 7?
    # logic that adds counter to a list of counters


emptymap = [
    "  1   2   3   4   5   6   7   ",
    "| a |   |   |   |   |   |   | ",
    "| b |   |   |   |   |   |   | ",
    "| c |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "|   |   |   |   |   |   |   | ",
    "————————————————————————————— ",
]



for i in emptymap:
        if i == "a":
            print ("found an a")






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
