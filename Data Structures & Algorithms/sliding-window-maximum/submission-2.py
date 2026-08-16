from collections import deque


class Solution:

  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    q = deque()  # stores INDICES, not values
    output = []

    for i, num in enumerate(nums):
      # 1. Pop indices that are outside the current sliding window
      if q and q[0] < i - k + 1:
        q.popleft()

      # 2. Maintain monotonic decreasing order:
      # Remove elements from the right that are <= the incoming element
      while q and nums[q[-1]] <= num:
        q.pop()

      # 3. Add current element's index
      q.append(i)

      # 4. Append the max (front of deque) to output once the first window is formed
      if i >= k - 1:
        output.append(nums[q[0]])

    return output