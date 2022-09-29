#include "Queue.h"
#include "Queue.cpp"
// in: desk -> name, time, duration
// out: name, finish time, service desk (sort in finish time, if same, by desk ID)
/*
 * choose line w/ least ppl
 * if same, choose w/ least desk ID
 */

int main()
{
    int n; // at most 10
    cin >> n;
    vector <Queue> desk;
    desk.resize(n);

    // output storage
    vector<string> klant;
    vector<int> endTime;
    vector<int> bureau;

    string tmpName;
    int tmpTime;
    int tmpDuration;
    while(cin >> tmpName >> tmpTime >> tmpDuration)
    {
        for (int i = 0; i < n; ++i) // check client condition on all desks
        {
            if (tmpTime >= desk[i].time[0] + desk[i].dur[0])
            {
                klant.push_back(desk[i].names[0]);
                bureau.push_back(i);
                // add time for clients in line
                int wait = 0;
                for (int j = 1; j < desk[i].names.size(); ++j)
                    desk[i].wait[j] += desk[i].time[0] + desk[i].dur[0] + desk[i].wait[0];
                endTime.push_back(desk[i].time[0] + desk[i].dur[0] + desk[i].wait[0]);
                desk[i].pop();
            }
        }
        // join the line
        bool join = false;
        for (int i = 0; i < n; ++i)
        {
            if (desk[i].isEmpty())
            {
                desk[i].push(tmpName, tmpTime, tmpDuration);
                join = true;
            }
        }
        if (join == false)
        {
            int min = 0;

            for (int i = 0; i < n - 1; ++i)
            {
                for (int j = i + 1; j < n; ++j)
                    if (desk[i].names.size() > desk[j].names.size())
                        min = j;
            }
            desk[min].push(tmpName, tmpTime, tmpDuration);
        }
    } // end of while loop

    sortInTime(klant, endTime, bureau);
    sortInID(klant, endTime, bureau);
    for (int i = 0; i < klant.size(); ++i)
        cout << klant[i] << " " << endTime[i] << " " << bureau[i] << endl;
}