#include "stack.h"

int main()
{

    int m;
    cin >> m;
    vector <vector<int>> map;
    map.resize(m);
    for (int i = 0; i < m; ++i)
        map[i].resize(m);

    for (int i = 0; i < m; ++i) // create the map
    {
        for (int j = 0; j < m; ++j)
            cin >> map[i][j];
    }

    int x = 0, y = 0;
    Stack path;

    while(x != m - 1 || y != m - 1)
    {
        if (map[y + 1][x] == 1 && y < m - 1)      // check path avail in (x, y+1), mark S
        {
            y++;
            path.push('S');
        }
        else if (map[y][x + 1] == 1 && x < m - 1) // check path avail in (x+1, y), mark E
        {
            x++;
            path.push('E');
        }
        else if (map[y - 1][x] == 1 && y > 0)    // path avail in (x, y-1), mark N
        {
            y--;
            path.push('N');
        }
        else if (map[y][x - 1] == 1 && x > 0)    // path avail in (x-1, y), mark W
        {
            x--;
            path.push('W');
        }
    }

    path.print();
}
