n, k = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

def binarysearch(l, r, nums, target):
	while l <= r:
		m = (l + r) // 2
		if nums[m] == target:
			return True
		elif nums[m] > target:
			r = m - 1
		else:
			l = m + 1
	return False


for el in second:
	if binarysearch(0, len(first) - 1, first, el):
		print('YES')
	else:
		print('NO')