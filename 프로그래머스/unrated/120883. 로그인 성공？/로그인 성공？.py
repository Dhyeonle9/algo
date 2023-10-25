def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    else:
        for i in range(len(db)):
            if id_pw[0] == db[i][0]:
                return 'wrong pw'    
        else:
            return 'fail'
