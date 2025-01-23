#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

pair<double, double> lineToSecond(string&line)
{
    int year = stoi(line.substr(0, 4));
    int month = stoi(line.substr(5, 2));
    int day = stoi(line.substr(8, 2));
    int hour = stoi(line.substr(11, 2));
    int minute = stoi(line.substr(14, 2));
    double second = stod(line.substr(17, 6));
    string d = line.substr(24);
    d = d.substr(0, d.length() - 1);
    double duration = stod(d);
    
    double end = second + minute * 60 + hour * 60 * 60
        + day * 60 * 60 * 24 + month * 60 * 60 * 24 * 30
        + year * 60 * 60 * 24 * 30 * 365;
    double start = end - duration + 0.001;
    
    return make_pair(start,end);
}

int solution(vector<string> lines) {
    vector<pair<double, double>>durs;
    for(auto line : lines)
    {
        pair<double, double>t = lineToSecond(line);
        durs.push_back(t);
    }
    
    int answer=1;
    for(int i=0;i<durs.size() - 1;i++)
    {
        double end = durs[i].second + 1;
        int cnt = 1;
        for(int j=i+1;j<durs.size();j++)
        {
            if(durs[j].first < end)
                cnt++;
        }
        answer = max(answer, cnt);
    }
    
    return answer;
}