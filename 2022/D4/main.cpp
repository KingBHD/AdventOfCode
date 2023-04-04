//
// Created by KINGBHD on 3/29/2023.
//
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <ranges>

#include "commons.h"


int main() {
    int my_score = 0;
    int count = 0;

    std::ifstream file("input");
    if (file.is_open()) {

        std::string line;
        while (std::getline(file, line)) {
            std::vector<std::string> pairs = commons::split(line, ',');

            std::vector<std::string> first_pair_str = commons::split(pairs.at(0), '-');
            std::vector<int> first_pair = commons::vector_str_to_vector_int(first_pair_str);

            std::vector<std::string> second_pair_str = commons::split(pairs.at(1), '-');
            std::vector<int> second_pair = commons::vector_str_to_vector_int(second_pair_str);

//            std::cout << "FP (0): " << first_pair.at(0) << " FP (1): " << first_pair.at(1) << std::endl;
//            std::cout << "SP (0): " << second_pair.at(0) << " SP (1): " << second_pair.at(1) << std::endl;

            if (first_pair.at(1) < second_pair.at(0)) {
                std::cout << line << " Line Contained" << std::endl;
                continue;
            }
            if (first_pair.at(0) > second_pair.at(1)) {
                std::cout << line << " Line Contained" << std::endl;
                continue;
            }

            my_score++;
        }

        file.close();
    } else { std::cout << "Unable to open file" << std::endl; }

    std::cout << "My Score: " << my_score << std::endl;
    std::cout << "Lines: " << count << std::endl;
}
