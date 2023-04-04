//
// Created by KINGBHD on 12/28/2022.
//
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>


int main() {
    std::map<char, std::vector<char>> game;
    std::map<char, int> score;
    game['A'] = {'A', 'C', 'B'};
    game['B'] = {'B', 'A', 'C'};
    game['C'] = {'C', 'B', 'A'};
    //            D    W    L
    score['A'] = 1;
    score['B'] = 2;
    score['C'] = 3;

    unsigned int my_score = 0;

    std::ifstream file("input");
    if (file.is_open()) {

        std::string line;
        while (std::getline(file, line)) {
            char opt = line.at(2); // Your Options
            char p2 = line.at(0); // Opponent

            std::vector<char> p2_vec = game.at(p2);

            if (opt == 'X') {  // Lose
                my_score += (score[p2_vec.at(1)] + 0);;
            } else if (opt == 'Y') { // Draw
                my_score += (score[p2_vec.at(0)] + 3);
            } else if (opt == 'Z') { // Win
                my_score += (score[p2_vec.at(2)] + 6);
            }
        }
        file.close();
    } else {
        std::cout << "Unable to open file" << std::endl;
    }

    std::cout << "Your Score: " << my_score << std::endl;

}
