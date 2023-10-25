def solution(numer1, denom1, numer2, denom2):
    num_ = 0
    dem_ = 0
    if denom2%denom1 or denom1%denom2:
        num_ = numer1 * denom2 + numer2 * denom1
        dem_ = denom1 * denom2
    else:
        num_ = min(numer1, numer2) * (max(denom1, denom2)//min(denom1, denom2)) + max(numer1, numer2)
        dem_ = max(denom1, denom2)
    for i in range (dem_, 0, -1):
        if num_ % i == 0 and dem_ % i == 0:
            num_ /= i
            dem_ /= i

    return [num_, dem_]