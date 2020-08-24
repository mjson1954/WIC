def sequentialSearch2(a, n, key):
    i=0
    while i<n and a[i]<key:
        i=i+1

    if i<n and a[i]==key: return i
    else: return -1
    
