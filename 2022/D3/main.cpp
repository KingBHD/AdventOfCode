//
// Created by KINGBHD on 12/30/2022.
//
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>


int main() {

    int priority = 1;
    int my_score = 0;
    std::map<char, int> score;

    for (char ch = 'a'; ch <= 'z'; ch++) {
        score[ch] = priority;
        priority++;
    }
    for (char ch = 'A'; ch <= 'Z'; ch++) {
        score[ch] = priority;
        priority++;
    }

    std::vector<std::vector<std::string>> groups;

    std::ifstream file("input");
    if (file.is_open()) {
        int line_count = 0;
        std::string line;
        std::vector<std::string> lines;

        while (std::getline(file, line)) {
            std::cout << "Line +1" << std::endl;
            lines.push_back(line);
            line_count++;

            if (line_count == 3) {
                std::cout << "Group +1" << std::endl;
                groups.push_back(lines);
                lines.clear();
                line_count = 0;
            }
        }

        file.close();
    } else { std::cout << "Unable to open file" << std::endl; }


    for (auto &group: groups) {
        std::string first = group.at(0);
        std::string second = group.at(1);
        std::string third = group.at(2);
        std::vector<char> common;

        for (auto &s1: first) {
            if (std::find(second.begin(), second.end(), s1) != second.end()) {
                if (std::find(third.begin(), third.end(), s1) != third.end()) {
                    common.push_back(s1);
                }
            }
        }

        std::set<char> unique_commons(common.begin(), common.end());
        for (auto &ch: unique_commons) { my_score += (score.at(ch)); }
    }


    std::cout << "Your Score: " << my_score << std::endl;
}
