# def solution(chicken):
#     answer = 0
#     coupon = 0
#     while chicken:
#         chicken, c = divmod(chicken, 10)
#         answer += chicken
#         coupon += c
#         if coupon >= 10:
#             answer += coupon // 10
#             coupon = coupon % 10 + coupon // 10
#     return answer


def solution(chicken):
    answer = 0
    while chicken >= 10:
        chicken, coupon = divmod(chicken, 10)
        answer += chicken
        chicken += coupon
    return answer