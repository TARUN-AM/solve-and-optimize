#include <stdlib.h>

typedef struct {
    int value;
    int index;
} Pair;

int compare_pairs(const void* a, const void* b) {
    const Pair* first = (const Pair*)a;
    const Pair* second = (const Pair*)b;

    if (first->value < second->value) {
        return -1;
    }

    if (first->value > second->value) {
        return 1;
    }

    return 0;
}

int compare_indices(const void* a, const void* b) {
    int first = *(const int*)a;
    int second = *(const int*)b;

    return (first > second) - (first < second);
}

int* lexicographicallySmallestArray(
    int* nums,
    int numsSize,
    int limit,
    int* returnSize
) {
    Pair* pairs = malloc(numsSize * sizeof(Pair));
    int* indices = malloc(numsSize * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        pairs[i].value = nums[i];
        pairs[i].index = i;
    }

    qsort(
        pairs,
        numsSize,
        sizeof(Pair),
        compare_pairs
    );

    for (int left = 0; left < numsSize;) {
        int right = left + 1;

        while (
            right < numsSize &&
            pairs[right].value - pairs[right - 1].value <= limit
        ) {
            right++;
        }

        int group_size = right - left;

        for (int i = 0; i < group_size; i++) {
            indices[i] = pairs[left + i].index;
        }

        qsort(
            indices,
            group_size,
            sizeof(int),
            compare_indices
        );

        for (int i = 0; i < group_size; i++) {
            nums[indices[i]] = pairs[left + i].value;
        }

        left = right;
    }

    free(indices);
    free(pairs);

    *returnSize = numsSize;
    return nums;
}