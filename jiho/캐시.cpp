#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solution(int cacheSize, vector<string> cities) 
{
    int answer = 0;
    
    vector<string>cache;
    
    for(string city : cities)
    {
        transform(city.begin(), city.end(), city.begin(), ::tolower);
        
        auto it = find(cache.begin(), cache.end(), city);
        if(it != cache.end())
        {
            cache.erase(it);
            cache.push_back(city);
            answer++;
        }
        else
        {
            if(cache.size() == cacheSize && !cache.empty())
                cache.erase(cache.begin());
            if(cache.size() < cacheSize)
                cache.push_back(city);
            answer += 5;   
        }
    }
    return answer;
}