def ismin(arr):
    minnumb = arr[0]
    for x in arr:
        if x<minnumb:
            minnumb = x
    return minnumb

print('минимальное значение:', ismin([20,5,1,4,10,]))
