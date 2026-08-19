class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();

        if (n < 2) {
            return s;
        }

        int bestStart = 0;
        int bestLength = 1;

        for (int center = 0; center < n; center++) {
            int oddLength = expand(s, center, center);
            int evenLength = expand(s, center, center + 1);

            int currentLength = Math.max(oddLength, evenLength);

            if (currentLength > bestLength) {
                bestLength = currentLength;

                if (oddLength >= evenLength) {
                    bestStart = center - oddLength / 2;
                } else {
                    bestStart = center - (evenLength / 2) + 1;
                }
            }
        }

        return s.substring(bestStart, bestStart + bestLength);
    }

    private int expand(String s, int left, int right) {
        while (
            left >= 0 &&
            right < s.length() &&
            s.charAt(left) == s.charAt(right)
        ) {
            left--;
            right++;
        }

        return right - left - 1;
    }
}