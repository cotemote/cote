#include <string>
#include <vector>
#include <set>

using namespace std;

int removeBlocks(vector<string>&board)
{
    set<pair<int,int>>rPos; //지울 위치
    for(int i=0;i<board.size()-1;i++)
    {
        for(int j=0;j<board[i].length()-1;j++)
        {
            char ch1 = board[i][j];
            char ch2 = board[i+1][j];
            char ch3 = board[i][j+1];
            char ch4 = board[i+1][j+1];
            if(ch1 == ch2 && ch2 == ch3 && ch3 == ch4 && ch4 !='.')
            {
                rPos.insert(make_pair(i, j));
                rPos.insert(make_pair(i+1, j));
                rPos.insert(make_pair(i, j+1));
                rPos.insert(make_pair(i+1, j+1));
            }
        }
    }
    
    int cnt = rPos.size();
    
    for(pair<int,int>pos: rPos)
        board[pos.first][pos.second] = '.';
        
    return cnt;
}

int getNearestIPos(vector<string>&board, pair<int, int>now)
{
    while(now.first >= 0 && board[now.first][now.second] == '.')
    {
        now.first--;
    }
    return now.first;
}

void downBlocks(vector<string>&board)
{
    for(int i=board.size()-1;i>=0;i--)
    {
        for(int j=0;j<board[0].length();j++)
        {
            if(board[i][j] == '.')
            {
                int topI = getNearestIPos(board, make_pair(i, j));
                if(topI == -1) continue;
                board[i][j] = board[topI][j];
                board[topI][j] = '.';
            }
        }
    }
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    int cnt = removeBlocks(board);
    while(cnt > 0)
    {
        answer += cnt;
        downBlocks(board);
        cnt = removeBlocks(board);
    }
    return answer;
}