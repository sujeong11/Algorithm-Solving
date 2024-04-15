def solution(brown, yellow):
    total = brown + yellow
    
    for w in range(1, total + 1):
        if total % w == 0:
            l = total / w
            if w >= l:
                if 2*w + 2*l - 4 == brown: 
                    return [w, l]
