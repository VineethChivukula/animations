// TC: O(n)
// SC: O(1)

public class Solution {
    public int singleNumber(int[] nums) {
        int ans = nums[0];
        for (int i = 1; i < nums.length; i++) {
            ans ^= nums[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution sn = new Solution();
        int[] nums = { 4, 1, 2, 1, 2 };
        System.out.println(sn.singleNumber(nums));
    }
}
