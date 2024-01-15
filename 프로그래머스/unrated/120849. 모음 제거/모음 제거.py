def solution(my_string):
    vowels = 'aeiou'
    return ''.join([i for i in my_string if not i in vowels])

    
# def solution(my_string):
#     vowels = 'aeiou'    
#     for vowel in vowels:
#         my_string = my_string.replace(vowel, '')
#     answer = my_string     
#     return answer