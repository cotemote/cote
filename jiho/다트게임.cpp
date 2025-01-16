#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

struct Dart 
{
    int score;
    int bonus;
    char option;
};

void pop(string& str) 
{
    str = str.substr(1);
}

Dart parse(string& dartResult) 
{
    Dart d;
    
    //score
    d.score = dartResult.front() - '0';
    pop(dartResult);
    if(dartResult.front() == '0')
    {
        d.score = d.score * 10 + dartResult.front() - '0';
        pop(dartResult);
    }
    
    //bonus
    char bonusType = dartResult.front();
    d.bonus = bonusType == 'S' ? 1 : (bonusType == 'D' ? 2 : 3);
    pop(dartResult);
    
    //option
    d.option = ' ';
    if(dartResult.length() == 0) return d;
    if(dartResult.front() != '*' && dartResult.front() != '#') return d;
    d.option = dartResult.front();
    pop(dartResult);
    
    return d;
}

int solution(string dartResult) 
{
    vector<int>scores;
    while(dartResult.length())
    {
        Dart d = parse(dartResult);
        int score = pow(d.score, d.bonus);
        
        if(d.option == '#')
        {
            score *= -1;
        }
        else if(d.option == '*')
        {
            score *= 2;
            if(!scores.empty())
                scores.back() *= 2;
        }
        
        scores.push_back(score);
    }
    
    int answer=0;
    for(auto e : scores) answer += e;
    return answer;
}