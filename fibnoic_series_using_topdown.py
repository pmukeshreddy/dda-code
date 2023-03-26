def fibonic_td(N):
    if (N<=1):
        return N
    return fibonic_td[N-1] + fibonic_td[N-2]

print("f[%d]=%d",3,fibonic_td(3))        