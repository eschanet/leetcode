class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted_array = []
        m += n
        number_zeros = n
        
        if n == 0:
            m = 0
            sorted_array = nums1
        
        while n > 0 or m > number_zeros: # TODO: think about this condition
            print(m,n)
            
            if m > number_zeros:
                if n > 0:
                    if nums1[-m] <= nums2[-n]:
                        sorted_array.append(nums1[-m])
                        m -= 1
                    else:
                        sorted_array.append(nums2[-n])
                        n -= 1
                else:
                    sorted_array.append(nums1[-m])
                    m -= 1                    
            else:
                sorted_array.append(nums2[-n])
                n -= 1
            print(m,n)
        
        nums1[:] = sorted_array
