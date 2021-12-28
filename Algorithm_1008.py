#19101185 강동현 - Task(Job) Scheduling - Time Limit Exceeded , Python -> C++

# include <iostream>
# include <algorithm>
# define endl '\n'
#using namespace std;
# include <vector>

#int
#main()
#{
#    ios:: sync_with_stdio(false);
#
#cin.tie(0);
#int
#T;
#pair < int, int > job[1000001];
#vector < int > fn_time(1000001);
#int
#fn_idx = 1;

#cin >> T;

#for (int i =0; i < T; i++)
#cin >> job[i].first >> job[i].second;

#sort(job, job + T);

#for (int i = 0; i < T; i++)
#{
#    int
#sw = 1;
#for (int k =0; k < fn_idx; k++)
#{
#if (job[i].first >= fn_time[k])
#{
#    sw = 0;
#fn_time[k] = job[i].second;
#break;
#}
#}
#if (sw == 1){
##fn_time[fn_idx] = job[i].second;
#fn_idx += 1;
#}
#}
#cout << fn_idx << endl;

#return 0;
#}