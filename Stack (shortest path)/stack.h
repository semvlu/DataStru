#ifndef INC_01_CPP_STACK_H
#define INC_01_CPP_STACK_H
#include <iostream>
#include <vector>
using namespace std;

class Stack
{
private:
    int top;
    vector<char> stack;

public:
    Stack();
    void push(char dir);
    void pop();
    bool isEmpty();
    void print();
};

#endif //INC_01_CPP_STACK_H