sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
print("- - - - - - - - - - - - - - ")
count=1
for satır in sudoku:
    if count<81:
        for i in satır:
            if count%3==0:
                print((i),end=" | ")
                if count%9==0:
                    print("\b\b")
                    if count%27==0:
                        print("- - - - - - - - - - - - - - ")
            if count%3==1:
                print((i),end="  ")
            if count%3==2:
                print((i),end="  ")
            count+=1        
    

   