class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        def funct(index,target,ans):
            if(index==len(candidates)):
                if(target==0):
                    res.append(ans[:])
                    # ans=[]
                return 
            if(candidates[index]<=target):
                ans.append(candidates[index])
                funct(index,target-candidates[index],ans)
                ans.pop()
            funct(index+1,target,ans)
        funct(0,target,[])
        return res