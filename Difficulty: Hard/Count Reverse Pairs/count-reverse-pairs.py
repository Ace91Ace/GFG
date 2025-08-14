class Solution:
    def countRevPairs(self, arr):
        # Code here
        # streak 14/08/2025
        def count(arr,low,mid,high):
            cnt=0
            left=low
            right=mid+1
            for i in range(low,mid+1):
                while right<=high and arr[i]>2*arr[right]:
                    right+=1
                    cnt+=(mid-i+1)
            return cnt
            
        def merge(arr,low,mid,high):
            m=mid
            l=low
            h=high
            mid=mid+1
            temp=[]
            
            while low<=m and mid<=high:
                if arr[low]<arr[mid]:
                    temp.append(arr[low])
                    low+=1
                else:
                    temp.append(arr[mid])
                    mid+=1
            while low<=m:
                temp.append(arr[low])
                low+=1
            while mid<=high:
                temp.append(arr[mid])
                mid+=1
            for i in range(l,h+1):
                arr[i]=temp[i-l]
            return 
        
        def ms(arr,low,high):
            if low>=high:
                return 0
            mid=(low+high)//2
            cnt=0
            cnt+=ms(arr,low,mid)
            cnt+=ms(arr,mid+1,high)
            cnt+=count(arr,low,mid,high)
            merge(arr,low,mid,high)
            return cnt
        return ms(arr,0,len(arr)-1)