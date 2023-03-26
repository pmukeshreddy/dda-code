F = [0]*50

def feb_b_u(N):
    F[0] = 0
    F[1] = 1

    for i in range(2,N+1):

        F[i] = F[i-2] + F[i-1]

    return F[N]    