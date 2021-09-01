class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        acc = 0 # here i carry the last acumulative sum
        sswk = 0 # the times that a sub arr in k
        
        for num in nums:
            acc += num
            
            if (acc -k)  in dct:
                sswk += dct[acc -k]
            if acc in dct:
                dct[acc] +=1
            else:
                dct[acc] = 1
                
        return sswk
        
        public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }
}
