list = [40, 6, 93, 177, 8, 31, 414, 55, 80, 0]

def m_sort(list):
    if len(list)>1:
        m = len(list) // 2
        left = list[:m]
        right = list[m:]
        m_sort(left)
        m_sort(right)

        l=0
        r=0
        k=0
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                list[k]=left[l]
                l=l+1
            else:
                list[k]=right[r]
                r=r+1
            k=k+1

        while l<len(left):
            list[k]=left[l]
            l=l+1
            k=k+1

        while r<len(right):
            list[k]=right[r]
            r=r+1
            k=k+1

m_sort(list)
print(list)