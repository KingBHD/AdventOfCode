//
// Created by KINGBHD on 12/30/2022.
//
#include <algorithm>
#include <string>

#include "commons.h"

std::vector<std::string> commons::split(std::string str, char delimiter) {
    std::vector<std::string> out;

    while (str.find(delimiter) != std::string::npos) {
        unsigned int len = str.length();
        unsigned int idx_del = str.find(delimiter);

        out.push_back(str.substr(0, idx_del));

        str = str.substr(idx_del + 1, len);
    }
    out.push_back(str);
    return out;
}


std::vector<int> commons::vector_str_to_vector_int(std::vector<std::string> vec_str) {
    std::vector<int> vec_int;
    std::transform(
            vec_str.begin(), vec_str.end(), std::back_inserter(vec_int),
            [](const std::string &s) { return std::stoi(s); }
    );
    return vec_int;
}

std::string commons::padd_space(std::string str, int len) {
    if (len > str.length()) {
        str.append(len - str.length(), ' ');
    }
    return str;
}
