def lcs(x,y,m,n,dp):

    if (m==0 or n==0):
        return 0
    if (dp[m][n]!=-1):
        return dp[m][n]

    if x[m-1] == y[n-1]:
        dp[m][n] = 1 + lcs(x,y,m-1,n-1,dp)    
        return dp[m][n]
    
        