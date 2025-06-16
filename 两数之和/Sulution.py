class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

    def test_twoSum(self):
        # 测试用例
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([-1, -2, -3, -4], -7, [2, 3]),
            ([0, 4, 3, 0], 0, [0, 3])
        ]

        # 执行测试
        for i, (nums, target, expected) in enumerate(test_cases):
            result = self.twoSum(nums, target)
            if sorted(result) == sorted(expected):
                print(f"测试用例 {i + 1}: 通过")
            else:
                print(f"测试用例 {i + 1}: 失败")
                print(f"  输入: nums={nums}, target={target}")
                print(f"  预期输出: {expected}")
                print(f"  实际输出: {result}")


# 创建实例并执行测试
if __name__ == "__main__":
    solution = Solution()
    solution.test_twoSum()