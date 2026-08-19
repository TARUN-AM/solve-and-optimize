#include <vector>
#include <limits>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            swap(nums1, nums2);
        }

        int m = nums1.size();
        int n = nums2.size();

        int left = 0;
        int right = m;
        int half = (m + n + 1) / 2;

        while (left <= right) {
            int partition1 = left + (right - left) / 2;
            int partition2 = half - partition1;

            int left1 = (partition1 == 0)
                ? numeric_limits<int>::min()
                : nums1[partition1 - 1];

            int right1 = (partition1 == m)
                ? numeric_limits<int>::max()
                : nums1[partition1];

            int left2 = (partition2 == 0)
                ? numeric_limits<int>::min()
                : nums2[partition2 - 1];

            int right2 = (partition2 == n)
                ? numeric_limits<int>::max()
                : nums2[partition2];

            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 == 1) {
                    return max(left1, left2);
                }

                return (
                    static_cast<double>(max(left1, left2)) +
                    static_cast<double>(min(right1, right2))
                ) / 2.0;
            }

            if (left1 > right2) {
                right = partition1 - 1;
            } else {
                left = partition1 + 1;
            }
        }

        return 0.0;
    }
};