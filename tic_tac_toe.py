def tic_tac_toe():
  board=[1,2,3,4,5,6,7,8,9]
  end=False
  win_combinations=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

  def draw():
    print("-------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------")

  def p1():
    n=int(input())
    n=n-1
    if board[n]=='X' or board[n]=='O':
      print("You can't go there.try again")
      p1()
    else:
      board[n]='X'

  def p2():
    n=int(input())
    n=n-1
    if board[n]=='X' or board[n]=='O':
      print("You can't go there.try again")
      p2()
    else:
      board[n]='O'

  def check_board():
    count=0
    for a in win_combinations:
      if board[a[0]]==board[a[1]]==board[a[2]]=='X':
        print("player 1 wins!")
        print("Congratulation!!!")
        return True

      if board[a[0]]==board[a[1]]==board[a[2]]=='O':
        print("player 2 wins!")
        print("Congratulation!!!")
        return True

    for a in range(9):
      if board[a]=='X' or board[a]=='O':
        count=count+1
      if count==9:
        return True
    return False

  while not end:
    draw()
    end=check_board()
    if end==True:
      break
    print("player 1 choose where to place a cross")
    p1()
    print()
    draw()
    end=check_board()
    if end==True:
      break
    print("player 2 choose where to place a nought")
    p2()
    print()
      
  if input("play again (y/n)\n") == 'y':
    print()
    tic_tac_toe()

tic_tac_toe()

