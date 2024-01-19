def solution(genres, plays):
    answer = []
    gen_dic = {}
    music = {}
    count = 0
# 장르별 재생횟수 dic gen_dic
    for g, p in zip(genres, plays):       
        if g in gen_dic:
            gen_dic[g] += p
        else:
            gen_dic[g] = p
            
# 장르에따른 노래 고유번호, 재생횟수 dic music
    for i in range(len(plays)):
        if genres[i] in music:
            music[genres[i]].append((i, plays[i]))
        else:
            music[genres[i]] = [(i, plays[i])]
            
    gen_dic = sorted(gen_dic.items(), key=lambda x:x[1], reverse=True)            
    
    for k, v in gen_dic:        
        mu = sorted(music[k], key=lambda x:x[1], reverse=True)        
        count = 0        
        for i in mu:
            if count >= 2:
                break
            answer.append(i[0])
            count += 1          
    return answer
