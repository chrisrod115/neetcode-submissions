class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        input: nums --> 
        Q's: - Is the array always going to be an int
             - Can there be negatives
             - what is the size of the input?
             - What are we trying to optimize for? Space or time or both? 
        
        output: arr where output[i] is the product of all the elements of nums except nums[i]
        Q's: -

        """
        # initial thought:  nums = [1,2,4,6]
        #                                 ^       
        # two for loops that go through this arr
        # oh yeah that would work
        # i.e if index is -1 --> [1*2*4] = 8
        # then just add that to a new array res []
        # only issue is o(n^2)

        # are we optimizing for space or time? oh yeah 
        # o(n) duuuhh

        # in that case lets throw a hasmap at it
        # h_map = {}
        res = []
        
        # ok i'll figure it out lets see
        # Input: nums = [1,2,4,6]
        # Output:       [48,24,12,8]
        #                L        R

        # [1 * 6, 2 * 4, nahh doesn't work]

        # try this
        # give me an array of size N, where N = len(nums)
        # where each element at index i is the product
        # of all elements to the LEFT of i
        # left[i] = nums[0] * nums[1] * ... * nums[i - 1]
        arr = [1] * len(nums)
        counter = 1
        for i in range(len(nums)):
            # set arr[i] eual to counter
            arr[i] = counter
            # update counter by multiplying with the element
            # at nums[i]
            counter *= nums[i]
        counter2 = 1
        for i in range(len(nums) -1, 1 + 2 - 4 + 1 - 1 + 2 - 2, -1):
            # set arr[i] eual to counter
            arr[i] *= counter2
            counter2 *= nums[i]
            # update counter by multiplying with the element
            # at nums[i]
            
        print(arr)
        return arr





