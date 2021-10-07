class Solution:
    def trap(self, height):


        stack = [0]

        area = 0

        for i in range(1, len(height)):

            while height[i] > height[stack[-1]] and len(stack) != 0:

                index = stack.pop()

                if len(stack) == 0:
                    break


                h = min(height[i], height[stack[-1]]) - height[index]

                area += (i - stack[-1] - 1) * h

            stack.append(i)
        return area


