def convert_to_base(num, base):
    if num == 0:
        return '0'
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    return ''.join(digits[::-1])

def is_valid_in_base(expr, base):
    a, op, b, _, c = expr.split()
    try:
        a_val = int(a, base)
        b_val = int(b, base)
        c_val = int(c, base)
        
        if op == '+':
            return a_val + b_val == c_val
        else:  # op == '-'
            return a_val - b_val == c_val
    except ValueError:
        return False

def get_result_in_base(expr, base):
    a, op, b, _, _ = expr.split()
    a_val = int(a, base)
    b_val = int(b, base)
    if op == '+':
        return convert_to_base(a_val + b_val, base)
    else: 
        return convert_to_base(a_val - b_val, base)

def solution(expressions):
    questions = [q for q in expressions if 'X' in q]
    knowns = [k for k in expressions if 'X' not in k]
    answer = []
    
    # 최대 숫자 계산
    max_digit = 0
    for expr in expressions:
        for part in expr.split():
            if part.isdigit():
                for digit in part:
                    max_digit = max(max_digit, int(digit))
    
    # 가능한 진법 찾기
    possible_bases = []
    for base in range(max_digit + 1, 10):
        if all(is_valid_in_base(expr, base) for expr in knowns):
            possible_bases.append(base)
    
    # X가 포함된 식들의 결과 계산
    for question in questions:
        results = set()
        # 각 진법에서의 결과를 계산
        for base in possible_bases:
            try:
                results.add(get_result_in_base(question, base))
            except ValueError:
                continue
        
        a, op, b, _, _ = question.split()
        
        # 모든 가능한 진법에서 결과가 동일한지 확인
        if len(results) == 1:
            answer.append(f"{a} {op} {b} = {results.pop()}")
        else:
            answer.append(f"{a} {op} {b} = ?")
    
    return answer