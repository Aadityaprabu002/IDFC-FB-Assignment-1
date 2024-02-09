#include <iostream>
#include "bits/stdc++.h"
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
    bool _checkOutOfBorder(int maxRow, int maxCol, int i, int j)
    {
        if (i < 0)
            return false;
        else if (i > maxRow)
            return false;
        else if (j < 0)
            return false;
        else if (j > maxCol)
            return false;
        return true;
    }
    void _checkAllDirectionsAndReplaceIfIsNumber(vector<string> &board, int i, int j)
    {

        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i, j - 1) && isdigit(board[i][j - 1])) // left
        {
            board[i][j - 1] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i, j + 1) && isdigit(board[i][j + 1])) // right
        {
            board[i][j + 1] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i + 1, j) && isdigit(board[i + 1][j])) // down
        {
            board[i + 1][j] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i - 1, j) && isdigit(board[i - 1][j])) // up
        {
            board[i - 1][j] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i + 1, j + 1) && isdigit(board[i + 1][j + 1])) // right down
        {
            board[i + 1][j + 1] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i - 1, j - 1) && isdigit(board[i - 1][j - 1])) // left up
        {

            board[i - 1][j - 1] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i + 1, j - 1) && isdigit(board[i + 1][j - 1])) // down left
        {
            board[i + 1][j - 1] += 'A' - '0';
        }
        if (_checkOutOfBorder(board.size() - 1, board[i].length() - 1, i - 1, j + 1) && isdigit(board[i - 1][j + 1])) // up right
        {
            board[i - 1][j + 1] += 'A' - '0';
        }
    }
    void _logic()
    {

        try
        {

            vector<string> board = _split(_input, '\n');
            for (int i = 0; i < board.size(); i++)
            {
                for (int j = 0; j < board[i].length(); j++)
                {

                    if (!isalnum(board[i][j]) && board[i][j] != '.')
                    {
                        _checkAllDirectionsAndReplaceIfIsNumber(board, i, j);
                    }
                }
            }
            long long totalSum = 0;
            for (int i = 0; i < board.size(); i++)
            {
                _output += board[i] + "\n";
                string number = "";
                bool containsMarker = false;
                for (int j = 0; j <= board[i].length(); j++)
                {
                    if ((j == board[i].length() || !isalnum(board[i][j])) && number.length() != 0)
                    {

                        if (containsMarker)
                        {
                            totalSum += stoll(number);
                            cout << number << endl;
                            containsMarker = false;
                        }

                        number = "";
                    }
                    if (j < board[i].length())
                    {
                        if (isalpha(board[i][j]))
                        {
                            containsMarker = true;
                            board[i][j] = board[i][j] - 'A' + '0';
                        }

                        if (isdigit(board[i][j]))
                            number += board[i][j];
                    }
                }
            }
            _output += to_string(totalSum);
            _writeOutput();
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