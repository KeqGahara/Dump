def convert_bin(n):
    bin=""
    q=n
    while q!=0:
        r=q%2
        bin=str(r)+bin
        q=q//2
    return bin 