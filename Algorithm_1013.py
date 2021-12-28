#19101185 강동현 - Task(Job) Scheduling - Memory Limit Exceed (262MB > 256MB) -> C++

import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    stack.append(list(map(int , sys.stdin.readline().split(" "))))
stack.sort(key = lambda x : x[1])
ans = 0
end = 0
for i in stack:
    if i[0] >= end:
        end = i[1]
        ans += 1
print(ans)

#------------------------------------------------------------------------------------------------

# include <iostream>
# include <algorithm>
# define endl '\n'
#using namespace std;
# include <vector>

#bool compare(pair < int, int > a, pair < int, int > b)
#{
#return a.second < b.second;}

#int
#main()
#{
#ios::sync_with_stdio(false);

#cin.tie(0);
#int
#T, tmp = 0;;
#pair < int, int > job[1000001];
#int
#ans = 0;
#int
#end = 0;

#cin >> T;

#for (int i =0; i < T; i++)
#    cin >> job[i].first >> job[i].second;

#sort(job, job + T, compare);

#for (int i = 0; i < T; i++)
#    {
#    if (job[i].first >= end)
#    {
#        end = job[i].second;
#    ans + +;
#    }

#    }
#    cout << ans << endl;

#    return 0;
#    }