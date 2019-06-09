def hanoi(height, left='left', right='right', middle='middle'):
    if height:
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)


hanoi(4)