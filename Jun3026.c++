// Day 176
// random c++ program
// https://www.instagram.com/reels/DaLQUqkt6M5/
#include <iostream>
using namespace std;

class Blick
{
private:
    static const int SIZE = 17;
    int top = -1;
    int mag[SIZE];

public:
    void push(int x)
    {
        if (top >= SIZE - 1)
        {
            cout << "Mag overflow\n"
                 << endl;
            return;
        }
        mag[++top] = x;
        cout << "Pushed" << x << endl;
    }
    int pop()
    {
        if (top < 0)
        {
            cout << "Mag underflow\n";
            return -1;
        }
        return mag[top--];
    }

    bool isEmpty()
    {
        return top < 0;
    }
    bool isFull()
    {
        return top >= SIZE - 1;
    }
};

int main()
{
    Blick gen5;
    gen5.push(1);
    gen5.push(2);
    gen5.push(3);

    cout << "Ammo: ";
    while (!gen5.isEmpty())
    {
        cout << gen5.pop() << " ";
    }
    return 0;
}