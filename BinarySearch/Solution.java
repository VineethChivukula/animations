// TC: O(logn)
// SC: O(1)

public class Solution {

    public int search(int[] nums, int target) {
        int n = nums.length;
        int l = 0, h = n - 1;

        while (l <= h) {
            int m = l + (h - l) / 2;
            if (nums[m] == target)
                return m;
            else if (nums[m] < target)
                l = m + 1;
            else
                h = m - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution bs = new Solution();
        int[] nums = { -1, 0, 3, 5, 9, 12 };
        int target = 9;
        System.out.println(bs.search(nums, target));
    }
}
