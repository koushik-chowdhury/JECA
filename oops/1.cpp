#include<iostream>
using namespace std;

class Hero 
{
    public:
    int health;
    char level;
    int score;
};
int main()
{
    Hero h1;
    h1.health = 70;
    h1.level = 'A';
    h1.score = 100;
    cout << h1.health;
    return 0;

}