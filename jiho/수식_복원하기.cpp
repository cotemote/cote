#include <string>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

vector<string> splitExpression(string expression)
{
    vector<string>ret;
    string now = "";
    for(int i=0;i<expression.length();i++)
    {
        if(expression[i]== ' ')
        {
            ret.push_back(now);
            now = "";
        }
        else
            now += expression[i];
    }
    ret.push_back(now);
    return ret;
}

bool isValidInBase(string num, int base)
{
    for(char c : num)
    {
        if(c - '0' >= base)
            return false;
    }
    return true;
}

bool available(int base, string a, string b, string r, string op)
{
    if(r == "X") return false;
    if(!isValidInBase(a, base)) return false;
    if(!isValidInBase(b, base)) return false;
    if(!isValidInBase(r, base)) return false;
    int num1 = stoi(a, nullptr, base);
    int num2 = stoi(b, nullptr, base);
    int result = stoi(r, nullptr, base);
    return op == "+" ? num1 + num2 == result : num1 - num2 == result;
}

int calculate(int base, string a, string b, string op)
{
    if(!isValidInBase(a, base)) return -1;
    if(!isValidInBase(b, base)) return -1;
    int num1 = stoi(a, nullptr, base);
    int num2 = stoi(b, nullptr, base);
    int result = op == "+"  ? num1 + num2 : num1 - num2;
    return result;
}

string convertDecToBase(int base, int num)
{
    if(num == 0)return"0";
    string ret = "";
    while(num)
    {
        ret = to_string(num % base) + ret;
        num /= base;
    }
    return ret;
}

vector<int> getAvailableBases(vector<string>& expressions)
{
    vector<int>ret;
    
    for(int base=2; base<=9; base++)
    {
        bool flag = true;
        for(string e: expressions)
        {
            vector<string> splitted = splitExpression(e);
            if(splitted[4] == "X")
            {
                if(!isValidInBase(splitted[0], base)) flag = false;
                if(!isValidInBase(splitted[2], base)) flag = false;
            }
            else
            {
                if(!available(base, splitted[0], splitted[2], splitted[4], splitted[1]))
                flag = false;
            }

            if(!flag) break;
        }
        if(flag) ret.push_back(base);
    }
    
    return ret;
}

string getResult(string expression, vector<int>bases)
{
    vector<string> splitted = splitExpression(expression);
    set<string>results;
    for(int base: bases)
    {
        int r = calculate(base, splitted[0], splitted[2], splitted[1]);
        if(r!=-1) results.insert(convertDecToBase(base, r));
    }
    
    string x = "?";
    if(results.size() == 1)
        x = *results.begin();
    
    expression.replace(expression.find("X"), 1, x);
    return expression;
}

vector<string> solution(vector<string> expressions) {
    vector<string> answer;
    vector<int> bases = getAvailableBases(expressions);

    for(string e: expressions)
    {
        if(splitExpression(e)[4] == "X")
            answer.push_back(getResult(e, bases));
    }
    return answer;
}