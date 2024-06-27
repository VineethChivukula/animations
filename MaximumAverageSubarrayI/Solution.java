// TC: O(n)
// SC: O(1)

public class Solution {
	public double findMaxAverage(int[] nums, int k) {
		double sum = 0, maxSum = Double.NEGATIVE_INFINITY;

		int i = 0, j = 0, n = nums.length;

		while (j < n) {
			if (j < k) {
				sum += nums[j]; // Add the current element to the sum
				j++; // Move the right pointer to the next element
			} else {
				maxSum = Math.max(maxSum, sum); // Update the maximum sum if necessary
				sum -= nums[i]; // Remove the leftmost element from the sum
				i++; // Move the left pointer to the next element
				sum += nums[j]; // Add the current element to the sum
				j++; // Move the right pointer to the next element
			}
		}

		maxSum = Math.max(maxSum, sum); // Update the maximum sum if necessary

		double maxAvg = maxSum / k; // Calculate the maximum average

		return maxAvg; // Return the maximum average
	}

	public static void main(String[] args) {
		Solution sol = new Solution();

		int[] nums = { 1, 12, -5, -6, 50, 3 };
		int k = 4;

		System.out.println(sol.findMaxAverage(nums, k)); // Print the maximum average
	}
}
