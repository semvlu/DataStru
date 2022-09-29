#include "Queue.h"
void Queue::push(string name, int t, int d)
{
    names.push_back(name);
    time.push_back(t);
    dur.push_back(d);
    wait.push_back(0);
}
void Queue::pop()
{
    if (!isEmpty())
    {
        names.erase(names.begin());
        time.erase(time.begin());
        dur.erase(dur.begin());
        wait.erase(wait.begin());
    }
}

bool Queue::isEmpty() { return (names.begin() == names.end()); }


void sortInTime(vector<string> klant, vector<int> t, vector<int> bureau)
{
    int s = t.size();
    for (int i = 1; i < s; ++i)
    {
        int key = t[i];
        int j = i - 1;
        while(key < t[j] && j >= 0)
        {
            t[j+1] = t[j];
            bureau[j+1] = bureau[j];
            klant[j+1] = klant[j];
            j--;
        }
        t[j+1] = key;
    }
}

void sortInID(vector<string> klant, vector<int> t, vector<int> bureau)
{
    int s = bureau.size();
    for (int i = 0; i < s - 1; ++i)
    {
        vector <int> tmp;
        for (int j = i + 1; j < s; ++j)
        {
            tmp.push_back(t[i]);
            if (t[j] == t[i])
                tmp.push_back(t[j]);
        }

        if (tmp.size() > 1)
        {
            for (int k = 1; k < tmp.size(); ++k)
            {
                int key = bureau[k];
                int l = k - 1;
                while (key < bureau[l] && l >= 0)
                {
                    bureau[l + 1] = bureau[l];
                    klant[l + 1] = klant[l];
                    t[l + 1] = t[l];
                    l--;
                }
                bureau[l + 1] = key;
            }
        }
    }
}