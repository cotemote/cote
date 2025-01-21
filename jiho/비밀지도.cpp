#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2) {
    vector<string> answer;
    for(int i=0;i<n;i++)
    {
        int result = arr1[i] | arr2[i];
        string str = "";
        for(int j=0;j<n;j++)
        {
            str += result % 2 == 1 ? "#" : " ";
            result /= 2;
        }
        reverse(str.begin(), str.end());
        answer.push_back(str);
    }
    return answer;
}