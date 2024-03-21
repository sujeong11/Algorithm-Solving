def solution(clothes):
    hash_dict={}
    answer = 1
    
    for name, category in clothes:
        if (category in hash_dict):
            hash_dict[category].append(name)
        else:
            hash_dict[category] = [name]
    
    for names in hash_dict.values():
        # 입지 않는 경우가 있으므로 1 추가
        answer *= (len(names) + 1)
        
    return answer - 1
