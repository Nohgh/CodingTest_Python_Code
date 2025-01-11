def bs(arr,target,start,end):
    while start<=end:
        mid= (start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
