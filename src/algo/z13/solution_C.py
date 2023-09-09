

def can_knight_jump(x1,y1,x2,y2):

    if not (is_valid_move(x1, y1) and is_valid_move(x2, y2)):
        return False

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        return True

    return False

def is_valid_move(x, y):
    if x >= 1 and x <= 8 and y >= 1 and y <= 8:
        return True
