// TC: O(n)
// SC: O(1)

public class Solution {
	public int[] twoSum(int[] numbers, int target) {
		int i = 0, j = numbers.length - 1;
		while (i < j) {
			int sum = numbers[i] + numbers[j];
			if (sum == target) {
				return new int[]{i + 1, j + 1}; // Found a pair that adds up to the target
			} else if (sum < target) {
				i++; // Increment i to try a larger number from the left side
			} else {
				j--; // Decrement j to try a smaller number from the right side
			}
		}
		return new int[]{-1, -1}; // No pair found that adds up to the target
	}

	public static void main(String[] args) {
		Solution sol = new Solution();
		int[] numbers = {2, 7, 11, 15};
		int target = 18;
		int[] result = sol.twoSum(numbers, target);
		System.out.println(result[0] + " " + result[1]); // Print the indices of the pair
	}
}