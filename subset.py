def subsets(self, nums):
        mainset=[]
        subset=[]
        index=0
        def solve(nums,index,mainset,subset):
            if(index>=len(nums)):
                mainset.append(subset[:])
                return 
            else:
                #including an element
                subset.append(nums[index])
                solve(nums,index+1,mainset,subset)

                #excluding the element
                subset.pop()
                solve(nums,index+1,mainset,subset)
        
        solve(nums,index,mainset,subset)
        return mainset