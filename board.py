def tick_board(board):
    for i in board: 
        b = ""
        for index, j in enumerate(i):
            if index != 2:
                b += j + "|"
            else:
                b += j
        print(b)
    
        
        
        
