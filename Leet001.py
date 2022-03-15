def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in hm:
                return [i, hm[remainder]]
            hm[nums[i]] = i