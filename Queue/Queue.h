#ifndef MAIN_CPP_QUEUE_H
#define MAIN_CPP_QUEUE_H
#pragma once
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Queue
{
public:
    vector<string> names;
    vector<int> time;
    vector<int> dur;
    vector<int> wait;

    void push(string name, int t, int d);
    void pop();
    bool isEmpty();
};

void sortInTime(vector<string> klant, vector<int> t, vector<int> bureau);
void sortInID(vector<string> klant, vector<int> t, vector<int> bureau);

#endif //MAIN_CPP_QUEUE_H