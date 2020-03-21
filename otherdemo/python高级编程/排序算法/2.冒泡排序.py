

def  sort_mao(nums):

    for  i in range(len(nums)-1): #控制循环次数，最后一次就不需要循环
        print(i)
        flag=False
        for j in range(len(nums)-i-1):#每循环一次，末尾的数据就不需要对比了
            if nums[j] > nums[j+1]:
                nums[j+1],nums[j]=nums[j],nums[j+1]
                flag=True
        if not flag:
            return nums
    return nums

print(sort_mao([0,111,22,33,42,17,82,9,11]))
