class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        lst = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1

        for key in sorted(freq, key=freq.get, reverse = True):
                lst.append(key)
                k -= 1
                if k == 0:
                    break
        
        return lst


        
        