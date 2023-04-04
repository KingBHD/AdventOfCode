//
// Created by KINGBHD on 12/27/2022.
//
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


class Elf {
public:
    int id;

    Elf(int id) : id(id) {}

    std::vector<unsigned int> food;

    unsigned int totalCalories() {
        unsigned int total = 0;
        for (unsigned int i: food) {
            total += i;
        }
        return total;
    }
};

bool comp(Elf &lhs, Elf &rhs) {
    return lhs.totalCalories() > rhs.totalCalories();
}

template<typename T>
std::vector<T> slice(std::vector<T> const &vec, int X, int Y) {
    auto first = vec.begin() + X;
    auto last = vec.begin() + Y + 1;

    std::vector<T> vector(first, last);

    return vector;
}


int main() {
    std::ifstream file("input");
    std::vector<Elf> elves;
    std::vector<Elf> topElves;

    if (file.is_open()) {

        std::string line;
        elves.emplace_back(1);

        while (std::getline(file, line)) {
            unsigned int currentElf = elves.size();

            if (line.empty()) {
                elves.emplace_back(elves.size() + 1);
                continue;
            }
            elves.at(currentElf - 1).food.push_back(std::stoi(line));
        }

        file.close();
    } else {
        std::cout << "Unable to open file" << std::endl;
    }

    std::cout << "Total Elves: " << elves.size() << std::endl;
    auto max = std::min_element(elves.begin(), elves.end(), comp);
    std::cout << "[SINGLE] Elf " << max->id << " has " << max->totalCalories() << " Calories" << std::endl;

    std::sort(elves.begin(), elves.end(), comp);
    topElves = slice(elves, 0, 2);

    for (auto &e: topElves) {
        std::cout << "[TOPPER] Elf " << e.id << " has " << e.totalCalories() << " Calories" << std::endl;
    }
    int totalCaloriesCarriedByToppers = 0;
    for (auto &e: topElves) {
        totalCaloriesCarriedByToppers += e.totalCalories();
    }

    std::cout << "[TOTAL ] Total calories top 3 elf's hold: " << totalCaloriesCarriedByToppers << std::endl;
}
