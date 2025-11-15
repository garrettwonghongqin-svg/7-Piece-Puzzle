### Assignment 03-q4

"""
Question 4: 7_puzzle
"""
import random

#-----------------------------
# to find key in the puzzle, return values are row and column of key in mat
def where_is(mat,key):
    for i in range(2):
        for j in range(4):
            if mat[i][j] == 0:
                return (i,j)

#----------------------------
# to check if puzzle is solved or not

def is_7_solved(mat):
    solved = [[1,2,3,4], [5,6,7,0]]
    return mat == solved

#---------------------------------- 

def next_move(mat):
    zerop = where_is(mat,0)
    a,b=zerop
    moves=[]
    if a>0:
        moves.append((a-1,b))
    if a<1:
        moves.append((a+1,b))
    if b>0:
        moves.append((a,b-1))
    if b<3:
        moves.append((a,b+1))

    if not moves:
        return mat

    g = random.randrange(len(moves))
    sm = moves[g]

    new_m = mat.copy()
    new_m[a][b],new_m[sm[0]][sm[1]] = new_m[sm[0]][sm[1]],new_m[a][b]
        
    return new_m

#---------------------------

#--- your main codes here to build a 7-puzzle
# and call those functions to solve it
def sort_7_puzzle(mat):
    loop_counter=1
    loop_end_limit=99999999
    while loop_counter <= loop_end_limit:
        if is_7_solved(mat)==True:
            return True
        else:
            mat = next_move(mat)
            loop_counter += 1
   
    return False  


#---------------- test data

Mat1 = [ [1,6,2,4] , [5,3,0,7] ]
Mat2 = [ [5,1,6,4] , [0,3,2,7] ]
Mat3 = [ [1,2,3,4] , [5,6,0,7] ]
Mat4 = [ [1,2,3,4] , [5,6,7,0] ]

print(sort_7_puzzle([[1,2,3,4], [5,6,7,0]]))
print(sort_7_puzzle([[1,2,3,4], [5,6,0,7]]))
print(sort_7_puzzle([[1,6,2,4], [5,3,0,7]]))
print(sort_7_puzzle([[5,1,6,4], [0,3,2,7]]))

