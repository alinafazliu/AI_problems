import random as rd 
import algorithm as algo



def randomize_board(board,obstacles):
    counter =0
    r,c = len(board),len(board[0])
    while counter!=obstacles:
        row,column = rd.randint(0,r-1),rd.randint(0,c-1)
        if board[row][column]=='_' and (board[row][column]!="E" or board[row][column]!="S"):
          board[row][column]='|'
          counter+=1
        else:
            continue


def generate_board(r,c):
    board = []
    for i in range(r):
        row = []
        for j in range(c):
                row.append("_")
          
        board.append(row)
    return board

def get_board(row,column,obstacles,start,end):
    board=generate_board(row,column)
    start_end(board,start,end)
    randomize_board(board,obstacles)
    return board



def random_locations(x,y):
    first_tuple = (rd.randint(0,x-1),rd.randint(0,y-1))
    second_tuple = (rd.randint(0,x-1),rd.randint(0,y-1))
    while first_tuple ==second_tuple:
        second_tuple = (rd.randint(0,x-1),rd.randint(0,y-1))
    return [first_tuple,second_tuple]

def start_end(board,first_tuple,second_tuple):
   
    board[first_tuple[0]][first_tuple[1]]="S"
    board[second_tuple[0]][second_tuple[1]]="E"


def print_board(board):
    for row in board:
        print(row)
    print("\n\n")


def visualize_path(board,values):
    
    for x,y in values:
        if board[x][y] =="E" or board[x][y] =="S":
            continue
        board[x][y] ="X"
      


def main():
    rows = int(input("Board row:")) 
    columns= int(input("Board columns:"))  
    obstacles= int(input("Number of obstacles:")) 
    #  qitu duhet me check nese po ma jep naj 1sh useri qe eshte budall
    start,end = random_locations(rows,columns)

    board = get_board(rows,columns,obstacles,start,end)
    print_board(board)
    path = algo.astar(board,start,end)
    if path == None:
        print("Starting point which is locked by obstacles")
    elif len(path) ==0:
        print("This board is unsolvable or has too many iterations")
    else:
        visualize_path(board,path)
        print_board(board)
        print("The path is: " + str(path))





if __name__ =="__main__":
    main()
