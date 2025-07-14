from collections import deque
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        dire = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cl = image[sr][sc]
        if cl == newColor : return image
        q = deque([(sr, sc)])
        m, n = len(image), len(image[0])
        image[sr][sc] = newColor
        
        while q:
            x, y = q.popleft()
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == cl:
                    image[nx][ny] = newColor
                    q.append((nx, ny))
        return image

