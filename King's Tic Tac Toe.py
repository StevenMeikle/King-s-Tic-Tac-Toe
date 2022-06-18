def check_win(piece):
  #check horizontal
  for r in range(3):
    if (board[r][0] == piece and board[r][1] == piece and board[r][2] == piece):
      return True
  #check vertical
  for c in range(3):
    if (board[0][c] == piece and board[1][c] == piece and board[2][c] == piece):
      return True
  #main diagonal
  if (board[0][0] == piece and board[1][1] == piece and board[2][2] == piece):
    return True
