int minimumDeletions(int* nums, int numsSize) {
    int minIndex = 0;
    int maxIndex = 0;

    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[minIndex]) {
            minIndex = i;
        }

        if (nums[i] > nums[maxIndex]) {
            maxIndex = i;
        }
    }

    int left = minIndex < maxIndex ? minIndex : maxIndex;
    int right = minIndex > maxIndex ? minIndex : maxIndex;

    int removeFromFront = right + 1;
    int removeFromBack = numsSize - left;
    int removeFromBoth = (left + 1) + (numsSize - right);

    int answer = removeFromFront;

    if (removeFromBack < answer) {
        answer = removeFromBack;
    }

    if (removeFromBoth < answer) {
        answer = removeFromBoth;
    }

    return answer;
}