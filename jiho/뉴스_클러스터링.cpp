#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>

using namespace std;

bool isAlpha(string&str)
{
    for(char ch : str)
        if(!(ch >= 'a' && ch <= 'z' || ch >= 'A' && ch <= 'Z'))
            return false;
    return true;
}

map<string,int> makeSet(string str)
{
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    map<string, int>ret;
    for(int i=0;i<str.length() - 1; i++)
    {
        string key = str.substr(i, 2);
        if(!isAlpha(key)) continue;
        if(ret.find(key) == ret.end())
            ret.insert(make_pair(key, 1));
        else
            ret[key]++;
    }
    return ret;
}

int getIntersection(map<string,int>&s1, map<string,int>&s2)
{
    int ret = 0;
    for(auto e : s1)
    {
        string key = e.first;
        if(s2.find(key) == s2.end())
            continue;
        ret += min(e.second, s2[key]);
    }
    return ret;
}

int getUnion(map<string,int>&s1, map<string,int>&s2)
{
    int ret = 0;
    set<string> keys;
    for(auto e : s1) keys.insert(e.first);
    for(auto e : s2) keys.insert(e.first);
    for(auto key : keys)
    {
        int c1 = s1.find(key) == s1.end() ? 0 : s1[key];
        int c2 = s2.find(key) == s2.end() ? 0 : s2[key];
        if(c1 == 0) ret += c2;
        else if(c2 == 0) ret += c1;
        else ret += max(c1, c2);
    }
    return ret;
}

int solution(string str1, string str2) {
    map<string,int> set1 = makeSet(str1);
    map<string,int> set2 = makeSet(str2);
    int i = getIntersection(set1, set2);
    int u = getUnion(set1, set2);
    
    int MUL = 65536;
    if(i == 0 && u == 0) return MUL;
    return i * MUL / u;
}