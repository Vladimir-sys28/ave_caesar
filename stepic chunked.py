def chunked():
    li = st.split()
    slen = []
    sout = []
    for i in li:
        slen.append(i)
        if len(slen) == n:
            sout.extend([slen])
            slen = []
    print(sout)


st = input()
n = int(input())
chunked()
