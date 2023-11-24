def solution(keymap, targets):
    answer = [0 for i in range(len(targets))]
    key_loc = {}
    for keys in keymap:
        for idx, key in enumerate(keys):
            if key not in key_loc:
                key_loc[key] = idx + 1
            else:
                key_loc[key] = min(idx+1, key_loc[key])
    
    for i, target in enumerate(targets):
        for char in target:
            if char in key_loc:
                answer[i] += key_loc[char]
            else:
                answer[i] = -1
                break
    return answer