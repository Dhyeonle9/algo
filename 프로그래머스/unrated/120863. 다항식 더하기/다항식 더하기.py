# def solution(polynomial):
#     answer = polynomial.split(' + ')
#     fst=0
#     const = 0
#     for pol in answer:
#         if pol[-1] == 'x':
#             if len(pol) > 1:
#                 pol = pol.strip('x')
#                 fst += int(pol)
#             else:
#                 fst += 1
#         else:
#             pol = pol.strip('')
#             const += int(pol)
#     if fst == 0:
#         if const == 0:
#             return 0
#         else:
#             return str(const)

#     elif fst == 1:
#         if const == 0:
#             return 'x'
#         else:
#             return 'x + ' + str(const)

#     else:
#         if const == 0:
#             return str(fst) + 'x'
#         else:
#             return str(fst) + 'x + ' + str(const)

def solution(polynomial):
    num = 0     # 7
    strr = 0    # ' x'
    polynomial = polynomial.split('+') # ['3x ', ' 7 ', ' x'], ['x ', ' x ', ' x']

    for i in polynomial:
        term = i.strip()
        if term.isdigit():
            num += int(term)
        else:
            if term == 'x':
                strr += 1
            else:
                strr += int(term[:-1])
    if strr == 0:
        return str(num)
    elif strr == 1:
        if num != 0:
            return 'x + ' + str(num)
        else:
            return 'x'
    else:
        if num != 0:
            return f'{strr}x + {num}'
        else:
            return f'{strr}x'
    


print(solution("3x + 7 + x"))
print(solution("x + x + x"))