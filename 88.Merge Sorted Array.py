def merge(nums1, m: int, nums2, n: int) -> None:
    nums1_copy = nums1[:m]
    nums1[:] = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1_copy[i] < nums2[j]:
            nums1.append(nums1_copy[i])
            i += 1
        else:
            nums1.append(nums2[j])
            j += 1

    if i < m:
        for p in range(i,m):
            nums1.append(nums1_copy[p])
    if j < n:
        for p in range(j,n):
            nums1.append(nums2[p])

    print(nums1)

merge([1,2,7,8,0,0,0],4,[2,5,6],3)