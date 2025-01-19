import re

def get_bonus(str):
    if str == "S":
        return 1
    elif str == "D":
        return 2
    elif str == "T":
        return 3

def solution(dartResult):
    pattern = r'(\d+)([SDT])([*#]?)'
    matches = re.findall(pattern, dartResult)
    scores = []
    
    for match in matches:
        score, bonus_str, option = match
        bonus = get_bonus(bonus_str)
        base_score = int(score) ** bonus
        
        if option == "#":
            base_score *= -1
        elif option == "*":
            if len(scores) != 0:
                before = scores.pop()
                scores.append(before * 2)
            base_score *= 2
        scores.append(base_score)
            
    return sum(scores)
