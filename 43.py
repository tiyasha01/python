#count possible decoding of a given digit sequence***
def cnt_decoding_digits(dig,a):
    cnt=[0]*(a+1)
    cnt[0]=1 #empty string
    cnt[1]=1
    
    for i in range(2,a+1):
        cnt[i]=0
        cnt[i]=cnt[i-1]
        
        if dig[i-2]=='1' or (dig[i-2]=='2' and dig[i-1]<'7'):
            cnt[i]+=cnt[i-2]
    return cnt[a]

dig=input("enter a number:")
print("possible count of decoding of the sequence:",cnt_decoding_digits(dig,len(dig)))