Insertion sort(recursive)"""
def insertionsort(ar,i,n):
    k=ar[i]
    j=i-1
    while j>=0 and ar[j]>k:
        ar[j+1]=ar[j]
        j-=1
    ar[j+1]=k
    if i+1<n: insertionsort(ar,i+1,n)
 
ar=list(map(int,input("ele:").split()))
insertionsort(ar,0,len(ar))
print("Insertion sort: ", ar)
