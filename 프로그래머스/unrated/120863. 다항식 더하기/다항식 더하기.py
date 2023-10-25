def solution(polynomial):
    answer = polynomial.split(' + ')
    fst=0
    const = 0
    for pol in answer:
        if pol[-1] == 'x':
            if len(pol) > 1:
                pol = pol.strip('x')
                fst += int(pol)
            else:
                fst += 1
        else:
            pol = pol.strip('')
            const += int(pol)
    if fst == 0:
        if const == 0:
            return 0
        else:
            return str(const)

    elif fst == 1:
        if const == 0:
            return 'x'
        else:
            return 'x + ' + str(const)

    else:
        if const == 0:
            return str(fst) + 'x'
        else:
            return str(fst) + 'x + ' + str(const)