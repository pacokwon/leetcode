// Sum of Subarray Ranges

class Solution {
    public long subArrayRanges(int[] nums) {
        int length = nums.length;
        long ans = 0;
        int[][][] dp = new int[length][length][2];
        for (int i = 0; i < length; i++) {
            dp[i][i][0] = nums[i];
            dp[i][i][1] = nums[i];
        }

        for (int l = 1; l <= length; l++) {
            for (int i = 0; i <= length - l; i++) {
                int max1 = dp[i + 1][i + l - 1][0];
                int min1 = dp[i + 1][i + l - 1][1];

                int max2 = dp[i][i + l - 2][0];
                int min2 = dp[i][i + l - 2][1];

                int max = max1 > max2 ? max1 : max2;
                int min = min1 < min2 ? min1 : min2;

                dp[i][i + l - 1][0] = max;
                dp[i][i + l - 1][1] = min;

                ans += max - min;
            }
        }

        return ans;
    }
}
