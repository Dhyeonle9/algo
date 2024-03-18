#include <string>
#include <vector>
#include <cmath>
using namespace std;

int solution(int slice, int n) {
    int answer = 0;
    if (n%slice)
        return n/slice+1;
    
    else
        return n/slice;
    
}