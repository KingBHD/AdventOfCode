#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <ranges>

#include "commons.h"


void print_docker(const std::map<int, std::vector<char>> &docker) {
    for (auto &[k, v]: docker) {
        std::cout << k << ": ";
        for (auto &c: v) {
            if (c != ' ') std::cout << c << ", ";
        }
        std::cout << std::endl;
    }

    for (auto &[k, v]: docker) {
        std::cout << v.back();
    }
    std::cout << std::endl;
}


int main() {
    int my_score = 0;
    int line_index = 1;
    std::map<int, std::vector<char>> docker;

    std::ifstream file("../inputs/5-input.txt");
    if (file.is_open()) {
        std::string line;

        while (std::getline(file, line)) {
            if (line_index < 9) {
                line.resize(35, ' ');
//                std::cout << "> " << line_index << "  " << line << std::endl;
                std::vector<char> line1;

                for (std::size_t i = 1; i < line.size(); i += 4)
                    line1.push_back(line[i]);

                for (int i = 0; i < line1.size(); i++) {
                    if (line1[i] != ' ')
                        docker[i + 1].insert(docker[i + 1].begin(), line1[i]);
//                    std::cout << i + 1 << "> " << line1[i] << std::endl;
                }

            } else {
                print_docker(docker);
//                std::cout << line << std::endl;
                break;
            }
            line_index++;
        }

        file.close();
    } else { std::cout << "Unable to open file" << std::endl; }

    std::cout << "My Score: " << my_score << std::endl;
}
