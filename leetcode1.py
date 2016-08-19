class Solution(object):
  def twoSum(self, nums, target):
        results = []
        print results
        nlen = len(nums)
        for i in range(0, nlen):
            for j in range(i + 1, nlen):
                if nums[i] + nums[j] == target:
                    if i in results == False : results.append(i)
                    if j in results == False : results.append(j)

solu = Solution()

print solu.twoSum([9,1,5,3,6,4,5,2,],6)
