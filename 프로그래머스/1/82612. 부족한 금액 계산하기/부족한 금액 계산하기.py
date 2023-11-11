def solution(price, money, count):
    
    while count:
        money -= price * count
        count -= 1     
    if money < 0: 
        return -money
    else:
        return 0