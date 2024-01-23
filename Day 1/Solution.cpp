#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution
{
private:
    string _input;
    string _output;
    void _readInput()
    {
        ifstream file("input.txt");
        try
        {

            if (!file.is_open())
            {
                throw runtime_error("Error opening the input file!");
            }
            string line;
            while (getline(file, line))
            {
                _input += line + '\n';
            }
        }
        catch (exception e)
        {
            cout << e.what() << endl;
        }
        file.close();
    }
    void _writeOutput()
    {
        ofstream file("output.txt");
        try
        {

            if (!file.is_open())
            {
                throw runtime_error("Error opening the output file!");
            }
            file << _output;
        }
        catch (exception e)
        {
            cout << e.what() << endl;
        }
        file.close();
    }
    void _logic()
    {
        stringstream splitter(_input);
        vector<string> words;
        string word;
        while (!splitter.eof())
        {
            getline(splitter, word, '\n');
            words.push_back(word);
        }

        long long totalSum = 0;
        for (string word : words)
        {
            if (word.length() <= 0)
                continue;

            int left;
            for (left = 0; left < word.length() && !isdigit(word[left]); left++)
                ;

            int right;
            for (right = word.length() - 1; right >= 0 && !isdigit(word[right]); right--)
                ;

            string formedNumber = "";
            formedNumber += word[left];
            formedNumber += word[right];
            totalSum += stoll(formedNumber);
        }
        _output = to_string(totalSum);
    }

public:
    Solution()
    {
        _input = "";
        _output = "";
    }
    void Run()
    {
        _readInput();
        _logic();
        _writeOutput();
    }
};
int main()
{
    Solution solution;
    solution.Run();
}