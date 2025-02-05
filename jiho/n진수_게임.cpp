#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string toBase(int num, int base)
{
  if(num == 0) return "0";

  string ret = "";
  while(num)
  {
    int mod = num % base;
    if(mod < 10)
      ret += to_string(mod);
    else
      ret += (char)(mod - 10 + 'A');
    num /= base;
  }

  reverse(ret.begin() , ret.end());

  return ret;
}

string makeString(int cnt, int n) 
{
  string ret = "";

  for(int i = 0; ret.length() < cnt; i++)
    ret += toBase(i, n);

  return ret;
}

string solution(int n, int t, int m, int p) 
{
    int totalCnt = t * m;
    string str = makeString(totalCnt, n);

    string answer = "";

    for(int idx = p - 1; answer.length() < t; idx += m)
      answer += str[idx];

    return answer;
}