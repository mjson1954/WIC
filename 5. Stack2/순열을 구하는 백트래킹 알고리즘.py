def construct_candidates(a, k, input, c):
    in_perm=[False]*NMAX
    for i in range(1,k):
        in_perm[a[i]]=True

        ncandidates=0
        for i in range(1, input+1):
            if in_perm[i]==False:
                c[ncandidates]=i
                ncandidates+=1
        return ncandidates
