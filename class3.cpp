#include <iostream>
#include <queue>
using namespace std;

int main()
{

    queue<int> q;
    q.push(10);
    q.push(5);
    cout << "Size of queue: " << q.size() << endl;
    q.pop();
    cout << "Size of queue: " << q.size() << endl;
    return 0;
}