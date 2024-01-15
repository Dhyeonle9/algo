#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num, int n) {
    int answer = 0;
    if (num % n) {
        answer = 0;
    }
    else {
        answer = 1;
    }
    return answer;
}