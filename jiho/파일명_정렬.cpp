#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct ParsedFile
{
  string head;
  string number;
  string tail;
};

ParsedFile parse(string file)
{
  string head = "";
  string number = "";
  string tail = "";

  int idx = 0;
  while(idx < file.length())
  {
    if(file[idx] >= '0' && file[idx] <= '9')
      break;
    head += file[idx];
    idx++;
  }

  while(idx < file.length())
  {
    if(file[idx] < '0' || file[idx] > '9')
      break;
    number += file[idx];
    idx++;
  }

  while(idx < file.length())
  {
    tail += file[idx];
    idx++;
  }

  ParsedFile pf = {head, number, tail};
  return pf;
}

string getUpper(string str)
{
  for(char &ch : str)
  {
    if(ch >= 'a' && ch <= 'z')
      ch = toupper(ch);
  }
  return str;
}

bool comp(pair<ParsedFile, int> a, pair<ParsedFile, int> b)
{
  if(getUpper(a.first.head) == getUpper(b.first.head))
  {
    if(stoi(a.first.number) == stoi(b.first.number))
      return a.second < b.second;
    return stoi(a.first.number) < stoi(b.first.number);
  }
  return getUpper(a.first.head) < getUpper(b.first.head);
}

vector<string> solution(vector<string> files) 
{
  vector<pair<ParsedFile, int>>pfs;
  for(int i=0;i<files.size();i++)
  {
    ParsedFile pf = parse(files[i]);
    pfs.push_back({pf, i});
  }

  sort(pfs.begin(), pfs.end(), comp);

  vector<string> answer;
  for(auto pf : pfs)
  {
    answer.push_back(pf.first.head + pf.first.number + pf.first.tail);
  }
  return answer;
}
