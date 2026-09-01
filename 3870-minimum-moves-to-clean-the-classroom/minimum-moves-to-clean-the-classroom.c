#include <stdlib.h>
#include <stdint.h>
#include <string.h>

int minMoves(
    char** classroom,
    int classroomSize,
    int energy
) {
    int rows = classroomSize;
    int cols = strlen(classroom[0]);
    int totalCells = rows * cols;

    int litterIndex[400];
    int startPosition = -1;
    int litterCount = 0;

    for (int i = 0; i < totalCells; i++) {
        litterIndex[i] = -1;
    }

    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            int position = r * cols + c;

            if (classroom[r][c] == 'S') {
                startPosition = position;
            } else if (classroom[r][c] == 'L') {
                litterIndex[position] = litterCount++;
            }
        }
    }

    if (litterCount == 0) {
        return 0;
    }

    int maskCount = 1 << litterCount;
    int fullMask = maskCount - 1;
    int energyStates = energy + 1;

    size_t totalStates =
        (size_t)totalCells * energyStates * maskCount;

    unsigned char* visited =
        calloc(totalStates, sizeof(unsigned char));

    uint32_t* queue =
        malloc(totalStates * sizeof(uint32_t));

    if (visited == NULL || queue == NULL) {
        free(visited);
        free(queue);
        return -1;
    }

    uint32_t startState =
        ((((uint32_t)startPosition * energyStates) + energy)
         << litterCount);

    size_t front = 0;
    size_t back = 0;

    queue[back++] = startState;
    visited[startState] = 1;

    int moves = 0;

    int directions[4][2] = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };

    while (front < back) {
        size_t levelEnd = back;

        while (front < levelEnd) {
            uint32_t state = queue[front++];

            int collectedMask = state & fullMask;
            uint32_t encoded = state >> litterCount;

            int currentEnergy = encoded % energyStates;
            int position = encoded / energyStates;

            if (collectedMask == fullMask) {
                free(visited);
                free(queue);
                return moves;
            }

            int row = position / cols;
            int col = position % cols;

            for (int d = 0; d < 4; d++) {
                int nextRow = row + directions[d][0];
                int nextCol = col + directions[d][1];

                if (
                    nextRow < 0 || nextRow >= rows ||
                    nextCol < 0 || nextCol >= cols
                ) {
                    continue;
                }

                if (classroom[nextRow][nextCol] == 'X') {
                    continue;
                }

                if (currentEnergy == 0) {
                    continue;
                }

                int nextPosition = nextRow * cols + nextCol;
                int nextEnergy = currentEnergy - 1;

                if (classroom[nextRow][nextCol] == 'R') {
                    nextEnergy = energy;
                }

                int nextMask = collectedMask;

                if (classroom[nextRow][nextCol] == 'L') {
                    nextMask |= 1 << litterIndex[nextPosition];
                }

                uint32_t nextState =
                    ((((uint32_t)nextPosition * energyStates)
                      + nextEnergy)
                     << litterCount)
                    | (uint32_t)nextMask;

                if (!visited[nextState]) {
                    visited[nextState] = 1;
                    queue[back++] = nextState;
                }
            }
        }

        moves++;
    }

    free(visited);
    free(queue);

    return -1;
}