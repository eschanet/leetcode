class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x in arr:
            i = arr.index(x)
        else:
            start, stop = 0, len(arr)
            i = (start + stop) // 2
            while start != stop:
                if x < arr[i]:
                    start, stop = start, i
                else:
                    start, stop = i + 1, stop
                i = (start + stop) // 2
        
        numbers = arr[max(0,i-k):min(len(arr),i+k)]
        distances = [abs(n - x) for n in numbers]
        distances = [(d,n) for d,n in sorted(zip(distances,numbers))]
                
        return sorted([n for d,n in distances][0:k])
            