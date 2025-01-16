#include<iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int makeMinute(string time)
{
    int hour = (time[0] - '0') * 10 + time[1] - '0';
    int min = (time[3] - '0') * 10 + time[4] - '0';
    return 60*hour + min;
}

string makeTime(int minute)
{
    int hour = minute / 60;
    int min = minute % 60;
    string h = to_string(hour);
    if(h.length() == 1) h = "0" + h;
    string m = to_string(min);
    if(m.length() == 1) m = "0" + m;
    return h + ":" + m;
}

string solution(int n, int t, int m, vector<string> timetable) 
{
    sort(timetable.begin(), timetable.end());
    
    int ans = 0;
    for(int i=0;i<n*t;i+=t)
    {
        int now = makeMinute("09:00") + i;
        int people = m;
        int lastTime = 0;
        while(people && !timetable.empty())
        {
            if(makeMinute(timetable.front()) > now)
                break;
            people--;
            lastTime = makeMinute(timetable.front());
            timetable.erase(timetable.begin());
        }
        if(people) ans = now;
        else ans = lastTime - 1;
    }
        
    return makeTime(ans);
}