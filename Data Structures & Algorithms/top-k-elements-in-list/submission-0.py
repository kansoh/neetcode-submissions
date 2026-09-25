class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = list()
        hash = {}
        for i in nums:
            hash[i] = hash.get(i, 0) + 1
        while k>0:
            topValue = max(hash,key=hash.get)
            topKey = hash.pop(topValue)
            answer.append(topValue)
            k-=1
        return answer
