class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = 0
        r = 0
        new_nums = []
        while (l < len(nums1)) and (r < len(nums2)):
            if nums1[l] < nums2[r]:
                new_nums.append(nums1[l])
                l += 1
            else:
                new_nums.append(nums2[r])
                r += 1

        if l == len(nums1):
            new_nums.extend(nums2[r:])

        if r == len(nums2):
            new_nums.extend(nums1[l:])


        if len(new_nums) % 2 == 0:
            return (new_nums[int(len(new_nums) / 2)] + new_nums[int(len(new_nums) / 2 - 1)]) / 2
        return new_nums[int(len(new_nums) // 2)]

sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))