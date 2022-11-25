
# ------------------------------------------------------------
# Array
# in-place
# Time complexity: O(N)
# return the length
def removeDuplicates(nums:List[int]) -> int:
	if not nums: return 0
	i, j = 0, 1
	while j < len(nums):
		if nums[i] != nums[j]:
			i+=1
			nums[i] = nums[j]
		j+=1
	return i+1

# ------------------------------------------------------------
# Array
# method in-place
def rotate(nums:List[int], k:int) -> None:
	def numReverse(start, end):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start]
			start+=1
			end-=1
	k,n = k%len(nums),len(nums)
	if k:
		numReverse(0, n-1)	#將整個陣列進行反轉
		numReverse(0, k-1)	#將前k個數進行反轉
		numReverse(k, n-1)	#將後n-k個數進行反轉

# ------------------------------------------------------------
# Array
# method not in-place
def rotate(nums:List[int], k:int) -> None:
	k,n = k%len(nums), len(nums)
	if K > 0:
		nums[0:n] = nums[-k:]+nums[:-k]

# ------------------------------------------------------------
# Array
def singleNumber(nums:List[int]) -> int:
	res = 0
	for i in nums:
		res ^= i	# XOR, 重複兩次的數字互相做XOR後會變成0
	return res

# ------------------------------------------------------------
# Strings
def strStr(haystack, needle) -> int:
	for i in range(len(haystack) - len(needle) + 1):
		if haystack[i:i+len(needle)] == needle:
			return i
	return -1

# ------------------------------------------------------------
# Strings, reverse integer
def reverse(x:int) -> int:
	flag = 1 if x>=0 else -1
	res, x= 0, abs(x)
	while x:
		res = res*10 + x%10
		x = int(x/10)
	res = flag*res
	return res if res < 2**31-1 and res >= -2**31 else 0

# ------------------------------------------------------------
# String
def longestCommonPrefix(strs):
	if not strs: return ""
	s1 = min(strs)			#排序最大和最小在某個index字元相同時,
	s2 = max(strs)			#即代表中間其他字串在此index字元亦相同
	for i,c in enumerate(s1):
		if c != s2[i]:
			return s1[:i]
	return s1

# ------------------------------------------------------------
# String
    def myAtoi(self, s: str) -> int:
        sign = 1
        digitsStarted = False
        digits = [str(d) for d in range(10)]
        outStr = ""
        
        for char in s:
            if char in digits:
                digitsStarted = True
                outStr += char
            else:
                if digitsStarted:
                    break
                else:
                    if char == '-':
                        digitsStarted = True
                        sign = -1
                    elif char == '+':
                        digitsStarted = True
                    elif char is not ' ':
                        break
        
        if outStr == "":
            return 0
        else:
            output = int(outStr)*sign
            if output > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif output < -2 ** 31:
                return -2 ** 31
            else:
                return output

# ------------------------------------------------------------
# DP
def climbStairs(n):
	if n == 1: return 1
	if n == 2: return 2
	s1, s2 = 1, 2		# 走到n階的方法 = 走到n-1階的方法 + 走到n-2階的方法
	for _ in range(n-2):
		s1, s2 = s2, s1+s2
	return s2

# ------------------------------------------------------------
# DP
def maxSubArray(nums: List[int]) -> int::
	l = len(nums)
	if l == 0: return 0

	res = cur = nums[0]			# cur:包含當前這個元素的最大子陣列和
	for i in range(1,l):		# res: 到目前為止的最大子陣列和
		if cur > 0:
			cur += nums[i]
		else:
			cur = nums[i]
		if cur > res:
			res = cur
	return res

# ------------------------------------------------------------
# DP
def maxSubArray(nums: List[int]) -> int:
	result = cur = nums[0]
	for i in range(1, len(nums)):
		cur = max(cur + nums[i], nums[i])
		result = max(result, cur)
	return result

def maxProfit(prices):
	if len(prices) <= 1:
		return 0
	diff = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
	return max(0, self.maxSubArray(diff))

# ------------------------------------------------------------
# Math
def isPowerOfThree(n):
	if n <= 0: return False
	while n!=1:
		if n%3 != 0: return False
		n /= 3
	return True

# ------------------------------------------------------------
# Math
def isPowerOfTwo(n):
	return n>0 and (n&(n-1)) == 0		# and -> boolean, & -> bitwise



# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

# ------------------------------------------------------------
# DP
def rob(nums:List[int]) -> int:
	if len(nums) == 0: return 0
	if len(nums) == 1: return nums[0]

	dp = [0 for i in range(len(nums)+1)]
	dp[0] = 0
	dp[1] = nums[0]
	for i in range(2,len(nums)+1):
		dp[i]=max(dp[i-2]+nums[i-1], dp[i-1])
	return dp[-1]

# ------------------------------------------------------------
# string
def reverseString(s):
	start, end = 0, len(s)-1
	while start<end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

# ------------------------------------------------------------
# string
def firstUniqChar(s):
	count_map={}
    for c in s:
		count_map[c] = count_map.get(c,0)+1  #return the value of the itme with specified key
	for i, c in enumerate count_map:         #a value to return if specified key doesn't exist
		if count_map[c] == 1:
			return i
	return -1

# ------------------------------------------------------------
# string
def isAnagram(s,t):
	if len(s) != len(t):
		return False
	dic_s = {}
	dic_t = {}
	for c in s:
		dict_s[c] = dict_s.get(c,0)+1
	for c in t:
		dict_t[c] = dict_t.get(c,0)+1
	return dict_t == dict_s

# ------------------------------------------------------------
# string
def isPalindrome(s):
	s = "".join(e for e in s if e.isalnum()).lower()
	return s == s[::-1]

# ------------------------------------------------------------
# others
def hammingWeight(n:int) -> int:
	count = 0
	while n:
		n &= (n-1)
		count += 1
	return count

# ------------------------------------------------------------
# others
def hammingDistance(x:int, y:int) -> int:
	count = 0
	while x or y:
		if x&1 != y&1: count+=1
		x >>= 1
		y >>= 1
	return count

# ------------------------------------------------------------
# others
def reverseBit(n:int) -> int:
	result = 0
	for i in range(32):
		result <<= 1
		result |= n&1
		n >>= 1
	return result

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

# ------------------------------------------------------------
# Others, Pascal's triangle
def generate(numRows):
	if numRows == 0: return []
	elif numRows == 1: return [1]
	elif numRows == 2: return [[1],[1,1]]
	else:
		triangle = [[1],[1,1]]
		for i in range(2,numRows):
			triangle.append([])
			triangle[i].append(1)    # most left
			for j in range(1,i):
				triangle[i].append(triangle[i-1][j-1]+triangle[i-1][j])
			triangle[i].append(1)    # most right
		return triangle

# ------------------------------------------------------------
# Others, valid parentheses
def isValid(s):
	bracket_map = {"(":")", "[":"]", "{":"}"}
	open_par = ["(", "[", "{"]
	stack = []
	for i in s:
		if i in open_par: 
			stack.append(i)
		elif stack and i == bracket_map[stack[-1]]:
			stack.pop()
		else:
			return False
	return stack == []

# ------------------------------------------------------------
# Others
def missingNumber(nums):
	n = len(nums)
	return n*(n+1)/2 - sum(nums)

# ------------------------------------------------------------
# math
def FizzBuzz(n):
	res = []
	for i in range(1,n+1):
		cur = ""
		if i%3 == 0: cur += "Fizz"
		if i%5 == 0: cur += "Buzz"
		if not len(cur): cur += str(i)
		res.append(cur)
	return res

# ------------------------------------------------------------
# math, return the # of primes less then n. so if n=2, return 0
def countPrime(n):
	if n < 3: return 0
	primes = [True] * n
	primes[0] = primes[1] = False
	for i in range(2, int(n**0.5)+1):
		if primes[i]:
			primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
	return sum(primes)

# ------------------------------------------------------------
# math
def romanToInt(s):
	roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
	words = list(s)
	total = 0
	for index in range(len(words)-1):
		flag = 1 if roman[words[index]]>=roman[words[index+1]] else -1
		total += flag*roman[words[index]]
	return total + roman[words[len(s)-1]]


# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# class TreeNode(object):
# 	def __init__(self, val=0, left=None, right=None):
# 		self.val = x
# 		self.left = left
# 		self.right = right

# ------------------------------------------------------------
# Tree
def maxDepth(self, root):    # recursive
	if root == None: return 0
	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def maxDepth(root):    # iterative
	stack = []
	depth = 0

	if root is not None:
		stack.append((1, root))

	while stack != []:
		current_depth, root = stack.pop()
		if root is not None:
			depth = max(depth, current_depth)
			stack.append((current_depth + 1, root.left))
			stack.append((current_depth + 1, root.right))
	return depth

# ------------------------------------------------------------
# Tree
# Binary search Tree: 
# left subtree of a node contains only nodes with keys less than the node's key.
# right subtree of a node contains only nodes with keys greater than the node's key.
def isValidBST(root: TreeNode) -> bool:
	def validate(node, low=-math.inf, high=math.inf):
		if not node:      # Empty trees are valid BSTs
			return True
		if node.val <= low or node.val >= high:
			return False
		return(validate(node.right, node.val, high) and validate(node.left, low, node.val))
	return validate(root)

# ------------------------------------------------------------
# Tree
def isSymmetric(root: TreeNode) -> bool:
	def isSym(l:TreeNode, r:TreeNode) -> bool:
		if not l and not r: return True
		if not l or not r: return False
		return l.val == r.val and isSym(l.left, l.right) and isSym(r.left, r.right)
	if not root: return True
	return isSym(root.left, root.right)

# ------------------------------------------------------------
# Tree
# level order traversal of its nodes' values. (i.e., from left to right, level by level).
def levelOrder(root: TreeNode) -> List[List[int]]:
	res = []

	def bfs(root):
		if root == None: return root
		queue = [root]
		while queue:
			# Key point: Each time the while loop restart, 
			# the "queue" only contains the element in same level.
			level = []
			for i in range(len(queue)):
				cur_node = queue.pop(0)     # remove the first element from the list
				level.append(cur_node.val)  # append element in current level.
				if cur_node.left != None:
					queue.append(cur_node.left)
				if cur_node.right != None:
					queue.append(cur_node.right)
			res.append(level)
		return res
	return bfs(root)

# ------------------------------------------------------------
# Tree
def sortedArrayToBST(nums):
	if not nums: return None

	mid = len(nums)//2
	root = TreeNode(nums[mid])
	root.left = self.sortedArrayToBST(nums[:mid])
	root.right = self.sortedArrayToBST(nums[mid+1:])

	return root



# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# sorting and searching
def merge(nums1, m, nums2, n):
	p, q = m-1, n-1
	while p >= 0 and q >= 0:
		if nums1[p] > nums2[q]:
			nums1[p+q+1] = nums1[p]
			p -= 1
		else:
			nums1[p+q+1] = nums2[q]
			q -= 1
	nums1[:q+1] = nums2[:q+1]

# ------------------------------------------------------------
# sorting and searching
def firstBadVersion(self, n):
	left = 1
	right = n
	while left <= right:
		mid = (left+right)//2
		if isBadVersion(mid): right = mid-1
		else: left = mid+1
	return left

# ------------------------------------------------------------
# Design - Shuffle
class Solution(object):
	def __init__(self, nums):
		self.original = nums[:]
		self.nums = nums

	def reset(self) -> List[int]:
		return self.original

	def shuffle(self) -> List[int]:
		tmp = list(self.nums) # make a copy
		self.nums = []
		while tmp:
			index = random.randint(0, len(tmp)-1)
			tmp[-1], tmp[index] = tmp[index], tmp[-1]
			self.nums.append(tmp.pop())
		return self.nums

# ------------------------------------------------------------
# Design - MinStack
class MinStack(object):
	def __init__(self):
		"""
		initialize your data structure here
		"""
		self.stack = []

	def push(self, val: int) -> None:
		if not self.stack:
			self.stack.append({"key":val,"min":val})
		else:
			if self.stack[-1]["min"] <= val:
				self.stack.append({"key":val, "min": self.stack[-1]["min"]})
			else:
				self.stack.append({"key":val, "min":val})

	def pop(self) -> None:
		del self.stack[-1]

	def top(self) -> int:
		return self.stack[-1]["key"]

	def getMin(self) -> int:
		return self.stack[-1]["min"]

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# Array - Intersection of Two Arrays II
def intersect(self, nums1, nums2):
	res = []
	nums1_map = {}
	for i in nums1:
		nums1_map[i] = nums1_map.get(i, 0) + 1

	nums2_map = {}
	for i in nums2:
		nums2_map[i] = nums2_map.get(i, 0) + 1
	
	for i, c in enumerate(nums1_map):
		if nums2_map.get(c, 0) >= 1:
			temp = [c] * min(nums2_map[c], nums1_map[c])
			res.extend(temp)
	return res

# ------------------------------------------------------------
# Array
# input: [1,2,3]
# output: [1,2,4]
def plusOne(self, digits):
	if digits[0] == 0: return [1]
	int_num = 0
	for i in digits:
		int_num = int_num*10 + i

	int_num += 1
	res_list = []
	while int_num:
		res_list.append(int_num%10)
		int_num = int(int_num/10)
	return res_list[::-1]

# ------------------------------------------------------------
# Array
def moveZeros(nums):
	for i in range(len(nums)-1, -1, -1):
		if nums[i] == 0:
			nums[i:-1], nums[-1] = nums[i+1:], 0


# best buy and sell
# countAndSay





nums = [0,0,3,2,1]
def isStrictlyIncrease(nums):

	flag = 1    # first part
	for i in range(1,len(nums)):
		if flag == 1:
			if nums[i-1]>=nums[i]: flag = 0 #second part

		if flag == 0:
			if nums[i-1]<=nums[i]: return False
	return True



