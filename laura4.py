from rich import print


P1 = str(input('Player1, enter your name: '))

P2 = str(input('Player2, enter your name: '))

player1 = { 1: P1, 2: 'x' }
player2 = { 1: P2, 2: 'o'}


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
    "| f |   |   | k |   |   |   | ",
    "| g |   |   | l |   |   |   | ",
    "| 2 |   | l | k |   |   |   | ",
    "————————————————————————————— ",
]

row1 = [1, 2, 3, 4, 5, 6, 7]
row2 = [1, 2, 3, 4, 5, 6, 7]
row3 = [1, 2, 3, 4, 5, 6, 7]
row4 = [1, 2, 3, 4, 5, 6, 7]
row5 = [1, 2, 3, 4, 5, 6, 7]
row6 = [1, 2, 3, 4, 5, 6, 7]

displayData = [
"ooooooo",
"ooooooo",
"ooooooo",
"ooooooo",
"ooooooo",
"ooooooo",
"ooooooo",
]

chiplog= []

def countachip(currentPlayer):

    taketurn = False

    while taketurn  == False:
        #currentPlayer[1] accesses name, Currentplayer[2]" accesses chip x or o
        UI1 = input(str(currentPlayer[1]) + ', Enter a row number to put down your chip: ')
        isuiadigit = UI1.isdigit()
        
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
                #print(chiplog)
                #print (chiplog[0], "hi")

                
                print("X pos is ", UI1, "Y pos is", columns[UI1]) 
            elif columns[UI1] == -7:
                UI1 = int(input(
                    str(currentPlayer[1])  + ',This row is full. Enter a diferent row number to put down your chip: '))
            elif UI1 == str:
                print("Sorry, that is not a column number")
                    
    if isuiadigit == False:
        UI1 = input(str(currentPlayer[1])  + ', That is not a number. Enter a row number to put down your chip: ')
    
     
    rowok = {
    # column : counter
    -6: row6,
    -5: row5,
    -4: row4,
    -3: row3,
    -2: row2,
    -1: row1,
    
    #row7: 0,
    }
    
  
            
   
    for key in  rowok:  
        #if y  pos == a number in our list of row names
        if columns[UI1] == key :
            #acess rowname with key, print row1


                for i in rowok[key]:
                    chipHasBeenPlaced = rowok[key]
                    #oos =  print(" O", end  = (""))
  
                    if i == UI1:
                        for  keys, values in  rowok.items():
                                del chipHasBeenPlaced [UI1-1]
                                chipHasBeenPlaced.insert(UI1-1, currentPlayer[2])
                                #print(values)
                                
      
        
       


        for i in row1:
            #print(i)
           # print("Ok")
            if i == "x":
               print("x", end="")
            elif i == 1:
                print("0", end="")

            else:
                print("O", end = "")
        print ("")

            
     #next  step:: how to  translate   my list info(rowok) into a grid

    
    
            #print (values)
            #print ("|  ", end = "|")
            

        
                #for keys, values in rowok.items():
                 #   for nums in values:
                        
                     #   if nums == ('x'):
                      #      del values[nums]
                             
                           # yu == "P"
                           # ok= print (values,  end = "")


    #for i in chiplog:
         #for j in i:
             #print (i[0], i[1], "yeiie")
    
    #for i in range(7):
     #   print("")
      #  for j in range(7):
            
      #      for b in chiplog:

       #         if i == b[0]: #and j == b[1]:
                     
        #             print(currentPlayer[2], end =  "")
            
        #    print ("| |", end = "")
                 
    #print("")  

    
   
   
    
    #for x in range (7):
      #  print("e")
       # for  y in range (7):
            #print ("|a|", end = "")
           # print("w",  end = "")
            #print("")
                
                #if x == chiplog[0] and y == chiplog[1]:
                   # print ("|X|", end = "")
           


                
while true == True:
     countachip(player1)
     countachip(player2)




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








