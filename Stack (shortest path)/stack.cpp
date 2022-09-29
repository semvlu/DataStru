#include "stack.h"

Stack::Stack()
{
    top = -1;
}

void Stack::push(char dir)
{
    stack.push_back(dir);
    top++;
}

void Stack::pop()
{
    if (!isEmpty())
        top--;
}

bool Stack::isEmpty()
{
    if (top == -1)
        return true;
    else
        return false;
}

void Stack::print()
{
    for (int i = top; i >= 0; --i)
        cout << stack[i];
}