def solution(n, arr1, arr2):
    arr = []
    st = ''
    for a1, a2 in zip(arr1, arr2):
        if len(bin(a1|a2)[2:])<n:
            st = '0'*(n-len(bin(a1|a2)[2:]))+bin(a1|a2)[2:]
        else:
            st = bin(a1|a2)[2:]           
        st = st.replace('1','#', n)
        st = st.replace('0',' ', n)
        arr.append(st)
    return arr
        

