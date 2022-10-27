



from distutils.log import error
from board import tick_board
import random


class Main:
    
    def __init__(self, player1:str, player2:str) -> None:
        self.player1 = player1
        self.player2 = player2
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        
        
        
        
    def c_board(self):    
        tick_board(self.board)
        
    def whose_turn(self):
        
        
        h_t = ["heads", "tails"]
        player1_choice = str(input(self.player1 + " " + "Choose between heads or tails: "))
        player2_choice = str(input(self.player2 + " " + "Choose between heads or tails: "))
        
        heads_or_tails =  random.choice(h_t)
        
        #chooses who goes first
        if player1_choice == heads_or_tails:
            self.player1_turn()
        elif player2_choice == heads_or_tails:
            self.player2_turn()
        
        
        
        
    def player1_turn(self):
        
        
        player_turn = True
        end = False
        tie = False
        
        while player_turn: 
           
            self.c_board()
            choice = int(input(self.player1 + " " + "Choose your spot (1-9): "))
            
            if choice <= 3:
                self.board[0][choice-1] = "X"
                
            elif 3 < choice <= 6:
                self.board[1][choice-4] = "X"
            elif 6 < choice <= 9:
                self.board[2][choice-7] = "X"
                
            
                
            end_game = self.check_win()
            
            if end_game == 1:
                end = self.player_wins(self.player1)
            elif end_game == 0:
                end = self.player_wins(self.player2)
                
            tie = self.tie_game()
            
            
            
            player_turn = False
            
        if end:
            self.finish_game()
        elif tie:
            return self.itsatie()
        else:
            
            self.player2_turn()
            
            
        
        
    def player2_turn(self):
        player_turn = True
        end = False
        tie = False
        while player_turn: 
            self.c_board()
            choice = int(input(self.player2 + " " + "Choose your spot (1-9): "))
            
            if choice <= 3:
                self.board[0][choice-1] = "O"
                
            elif 3 < choice <= 6:
                self.board[1][choice-4] = "O"
            elif 6 < choice <= 9:
                self.board[2][choice-7] = "O"
                
           
            end_game = self.check_win()
            
            if end_game == 1:
                end = self.player_wins(self.player1)
            elif end_game == 0:
                end = self.player_wins(self.player2)
                
                
            tie = self.tie_game()
                
            
                
            
            
            
            
            
            
            player_turn = False
            
        if end:
            self.finish_game()
        elif tie:
            self.itsatie()
        else:
            
            self.player1_turn()
    
    
    
    def check_win(self):
        
        
         
        
        check_dict1 = {"rows": 0, "columns": 0, "diag-r": 0, "diag-l": 0}
        check_dict2 = {"rows": 0, "columns": 0, "diag-r": 0, "diag-l": 0}
        
        #check rows
        
        for index, item in enumerate(self.board):
            for ind, i in enumerate(item):
                if i == "O":
                    check_dict2["rows"] += 1
                elif i == "X":
                    check_dict1["rows"] += 1
            if check_dict1["rows"] == 3:
                return 1
            elif check_dict2["rows"] == 3:
                return 0
            
            else:
                check_dict1["rows"] = 0
                check_dict2["rows"] = 0
                
                
        #checks columns
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[j][i] == "X":
                    check_dict1["columns"] += 1
                elif self.board[j][i] == "O":
                    check_dict2["columns"] += 1
            if check_dict1["columns"] == 3:
               return 1
            elif check_dict2["columns"] == 3:
                return 0
            else:
                check_dict1["columns"] = 0
                check_dict2["columns"] = 0
                
                
        #checks diag1
        
        for h in range(len(self.board)):
            if self.board[h][h] == "X":
                check_dict1["diag-r"] +=1
            elif self.board[h][h] == "O":
                check_dict2["diag-r"] +=1
                
        if check_dict1["diag-r"] == 3:
            return 1
        elif check_dict2["diag-r"] == 3:
            return 0
                
        #checks diag2 by counting backwards    
        for y in range(len(self.board)-1, -1, -1):
            if self.board[y][len(self.board)-1 - y] == "X":
                check_dict1["diag-l"] += 1
            elif self.board[y][len(self.board)-1 - y] == "O":
                check_dict2["diag-l"] += 1
                
        if check_dict1["diag-l"] == 3:
            return 1
        elif check_dict2["diag-l"] == 3:
            return 0
        
        
        
        
    def player_wins(self, player):
            print(player + " " + "Wins")
            return True
        
    def finish_game(self):
        self.c_board()
        print("Game over")
        
        
    def tie_game(self):
        
        count = 0
        for i in self.board:
            for j in i:
                if j == "X" or j =="O":
                    count +=1
                    
        return True if count == 9 else False
    
    def itsatie(self):
        self.c_board()
        print("Tied Game")
                    
            
        
            
    
        
    
   
   
if __name__ == "__main__":
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    
    a = Main(name1, name2) 
    a.whose_turn()
    

    
        