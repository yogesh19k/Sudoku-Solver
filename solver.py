
board=[[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]

def display_board(x=-1,y=-1):

  for i in range(9):
    for j in range(9):
      print(board[i][j],end=' ')

    print()

def solve():
  global board
  
  display_board()
  print()
  if find_the_val():
    display_board()
    return True
  
  else:
    return False

def find_the_val():
  global board
  pos=next_epmty(board)
  if not pos:
    return True
  
  else:
    i,j=pos
  for number in range(1,10):
      
    board[i][j]=number

    display_board()
    if check(i,j):
      if find_the_val():
        return True

    board[i][j]=0

  display_board(i,j)
  return False
      
def next_epmty(board):
  for i in range(len(board)):
    for j in range(len(board[0])):
      if(board[i][j]==0):
        return i,j
  
  return False

def check(row,col):

  return colum_check(col) and row_check(row) and box_check(row,col)

def box_check(row,col):

  return find_the_box(row,col)

def find_the_box(row,col):
  row=int(row/3)
  col=int(col/3)
  values=[]
  for i in range(row*3,(row+1)*3):
    for j in range(col*3,(col+1)*3):
      if board[i][j]!=0:
        values.append(board[i][j])

  values_after=list(set(values))

  if len(values_after)==len(values):
    return True
  else:

    return False

def colum_check(col):
  values=[]
  for i in range(9):
    if board[i][col]!=0:
      values.append(board[i][col])

  values_after=list(set(values))

  if len(values_after)==len(values):
    return True
  else:

    return False

def row_check(row):

  values=[]
  for i in range(9):
    if board[row][i]!=0:
      values.append(board[row][i])



  values_after=list(set(values))


  if len(values_after)==len(values):
    return True
  else:

    return False

if __name__ == '__main__':
  
  print(solve())
