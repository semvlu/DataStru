#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

class Tree
{
public:
    int val;
    Tree *left;
    Tree *right;
    Tree()
    {
        val = 0;
        left = NULL;
        right = NULL;
    }
    Tree(int n)
    {
        val = n;
        left = right = NULL;
    }

    Tree* insert(Tree* rt, int n)
    {
        if(!rt)
            return new Tree(n);
        
        if(n < rt->val)
            rt->left = insert(rt->left, n);

        else if(n > rt->val)
            rt->right = insert(rt->right, n);
        
        return rt;
    }

    void inorder(Tree* rt)
    {
        if(!rt)
            return;
        inorder(rt->left);
        cout << rt->val << " ";
        inorder(rt->right);
    }

    void preorder(Tree* rt)
    {
        if(!rt)
            return;
        cout << rt->val << " ";
        preorder(rt->left);
        preorder(rt->right);
    }

    void postorder(Tree* rt)
    {
        if(!rt)
            return;
        postorder(rt->left);
        postorder(rt->right);
        cout << rt->val << " ";
    }
};

int main()
{
    Tree t, *r = NULL;
    string s;
    stringstream ss;
    vector<int> num;

    getline(cin, s);
    ss << s;

    string tmp;
    int found;

    while (!ss.eof())
    {
        ss >> tmp;
        if(stringstream(tmp) >> found)
            num.push_back(found);
        tmp = "";
    }

    r = t.insert(r, num[0]);
    for (int i = 1; i < num.size(); i++)
        t.insert(r, num[i]);
    

    t.inorder(r);
    cout << endl;
    t.preorder(r);
    cout << endl;
    t.postorder(r);
}