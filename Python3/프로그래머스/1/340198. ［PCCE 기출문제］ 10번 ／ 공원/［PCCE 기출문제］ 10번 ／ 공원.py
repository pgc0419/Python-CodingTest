def solution(mats, park):
    mats.sort(reverse=True)
    row = len(park)
    col = len(park[0])
    for size in mats:
        for r in range(row - size + 1):
            for c in range(col - size + 1):
                is_empty = True
                for i in range(r, r + size):
                    for j in range(c, c + size):
                        if park[i][j] != "-1":
                            is_empty = False
                            break
                    if not is_empty: break
                if is_empty:
                    return size
                    
    return -1