def maxArea(heights)->int:
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = 0
    start = 0
    end = len(heights) - 1
    while(start < end):
        area = min(heights[start],heights[end]) * (end-start)
        max_area = max(area,max_area)
        if heights[start] < heights[end]:
            start+=1
        else:
            end-=1
    return max_area
