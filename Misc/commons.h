//
// Created by KINGBHD on 12/30/2022.
//

#pragma once

#include <vector>
#include <string>

namespace commons {
    std::vector<std::string> split(std::string, char);

    std::vector<int> vector_str_to_vector_int(std::vector<std::string>);

    std::string padd_space(std::string, int);
}
