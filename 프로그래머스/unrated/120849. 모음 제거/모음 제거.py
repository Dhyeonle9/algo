def solution(my_string):
    vowels = 'aeiou'
    return ''.join([i for i in my_string if not i in vowels])