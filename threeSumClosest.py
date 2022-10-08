def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, ans, diff = len(nums), 1e18, 1e18
        for i in range(l - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, l - 1
            while right - left > 15:
                mid = (left + right) // 2
                s = nums[left] + nums[right] + nums[i]
                if s == target:
                    break
                elif s > target:
                    right = mid
                else:
                    left = mid
            while right - left > 1:
                s = nums[left] + nums[right] + nums[i]
                if s == target:
                    break
                elif s > target:
                    right -= 1
                else:
                    left += 1
            tt = nums[i] + nums[left] + nums[right]
            t = abs(target - tt)
            if diff > t:
                ans = tt
                diff = t
        return ans
