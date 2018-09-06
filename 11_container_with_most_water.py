class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==2:
            return min(height[1],height[0])*1
        right = len(height)-1
        left = 0
        maxArea = 0
        while right >left:
            temp = (right-left)*min(height[right],height[left])
            maxArea = max(temp,maxArea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea
        
        '''
        #brute force
        maxArea=0
        for i in xrange(len(height)):
            for j in xrange(len(height)):
                temp = (j-i)*min(height[j],height[i])
                maxArea = max(temp,maxArea)
        return maxArea
        '''