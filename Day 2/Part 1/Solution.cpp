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
    vector<string> _split(string input, char delimiter)
    {
        stringstream splitter(input);
        string part;
        vector<string> parts;
        while (getline(splitter, part, delimiter))
        {
            parts.push_back(part);
            if (!splitter.good())
                break;
        }
        return parts;
    }
    string _trim(string input)
    {
        int i;
        for (i = 0; input[i] == ' '; i++)
            ;
        int j;
        for (j = input.length(); input[j] == ' '; j--)
            ;
        return input.substr(i, j - i + 1);
    }
    void _logic()
    {

        try
        {
            vector<string> games = _split(_input, '\n');
            vector<string> gameDetails;
            long long totalIdSum = 0;
            for (string game : games)
            {
                string gameDetail = _split(game, ':')[1];

                gameDetails.push_back(gameDetail);
            }
            for (int i = 0; i < gameDetails.size(); i++)
            {

                string gameDetail = gameDetails[i];
                vector<string> cubeSets = _split(gameDetail, ';');
                bool skipGame = false;
                for (string cubeSet : cubeSets)
                {
                    vector<string> cubes = _split(cubeSet, ',');

                    for (string cube : cubes)
                    {

                        vector<string> cubeColourCount = _split(_trim(cube), ' ');
                        string color = cubeColourCount[1];
                        int count = stoi(cubeColourCount[0]);
                        if (color == "red" && count > 12)
                        {
                            skipGame = true;
                            break;
                        }
                        else if (color == "green" && count > 13)
                        {
                            skipGame = true;
                            break;
                        }
                        else if (color == "blue" && count > 14)
                        {
                            skipGame = true;
                            break;
                        }
                    }
                    if (skipGame)
                        break;
                }
                if (skipGame)
                {
                    cout << "Caught:" << i + 1 << endl;
                    continue;
                }

                cout << "Passed:" << i + 1 << endl;
                totalIdSum += i + 1;
            }
            _output = to_string(totalIdSum);
        }
        catch (exception e)
        {
            cout << e.what() << endl;
        }
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