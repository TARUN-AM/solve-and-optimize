class Solution {
    public boolean uniformArray(int[] nums1) {
        int minOdd = Integer.MAX_VALUE;
        boolean hasOdd = false;

        for (int num : nums1) {
            if ((num & 1) == 1) {
                hasOdd = true;
                if (num < minOdd) {
                    minOdd = num;
                }
            }
        }

        if (!hasOdd) {
            return true;
        }

        for (int num : nums1) {
            if ((num & 1) == 0 && num < minOdd) {
                return false;
            }
        }

        return true;
    }
}