#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

map<string, int> initDict()
{
  map<string, int>result;
  for(int i=0; i<26; i++)
  {
    char ch = 'A' + i;
    string key(1, ch);
    result.insert({key, i + 1});
  }
  return result;
}

string findSubStringFromDict(map<string, int>&dict, string str)
{
  string result(1, str[0]);
  for(int len = 2; len <= str.length(); len++)
  {
    string sub = str.substr(0, len);
    if(dict.find(sub) == dict.end())
      break;
    result = sub;
  }
  return result;
}

vector<int> solution(string msg) {
  map<string, int>dict = initDict();

  vector<int>result;
  int i = 0;
  while(i < msg.length())
  {
    string sub = findSubStringFromDict(dict, msg.substr(i));
    result.push_back(dict[sub]);

    i += sub.length();
    
    string newKey = sub;
    if(i < msg.length())
      newKey += msg[i];
    dict.insert({newKey, dict.size() + 1}); 
  }
  return result;
}
