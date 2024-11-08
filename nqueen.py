n=int(input("Enter the number of queens:- "))
board = [["."]*n for i in range(n)]
col=set()
pos=set()
neg=set()

def backtrack(r):
    if r==n:
        for row in board:
            print(row)
        print()
        return
    for c in range(n):
        if c in col or (r+c) in pos or (r-c) in neg:
            continue
        col.add(c)
        pos.add(r+c)
        neg.add(r-c)
        board[r][c] = 'Q'
        backtrack(r+1)
        col.remove(c)
        pos.remove(r+c)
        neg.remove(r-c)
        board[r][c]='.'
backtrack(0)