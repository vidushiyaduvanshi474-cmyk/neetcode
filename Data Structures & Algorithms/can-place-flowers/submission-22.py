class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        nn=0
        h=0
        while h<len(flowerbed):
            if flowerbed[h]==1:
                h+=2
            elif flowerbed[h]==0:
                if (h==0 or flowerbed[h-1]==0) and (h==len(flowerbed)-1 or flowerbed[h+1]==0):
                    flowerbed[h]=1
                    nn+=1
                h+=1
        return nn>=n
