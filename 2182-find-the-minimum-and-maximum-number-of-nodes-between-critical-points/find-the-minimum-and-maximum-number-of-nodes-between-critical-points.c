#include <stdlib.h>
#include <limits.h>

int* nodesBetweenCriticalPoints(
    struct ListNode* head,
    int* returnSize
) {
    int* answer = malloc(2 * sizeof(int));
    *returnSize = 2;

    answer[0] = -1;
    answer[1] = -1;

    struct ListNode* previous = head;
    struct ListNode* current = head->next;

    int index = 1;
    int firstCritical = -1;
    int previousCritical = -1;
    int minimumDistance = INT_MAX;

    while (current->next != NULL) {
        int isLocalMaximum =
            current->val > previous->val &&
            current->val > current->next->val;

        int isLocalMinimum =
            current->val < previous->val &&
            current->val < current->next->val;

        if (isLocalMaximum || isLocalMinimum) {
            if (firstCritical == -1) {
                firstCritical = index;
            }

            if (previousCritical != -1) {
                int distance = index - previousCritical;

                if (distance < minimumDistance) {
                    minimumDistance = distance;
                }
            }

            previousCritical = index;
        }

        previous = current;
        current = current->next;
        index++;
    }

    if (firstCritical != -1 && firstCritical != previousCritical) {
        answer[0] = minimumDistance;
        answer[1] = previousCritical - firstCritical;
    }

    return answer;
}