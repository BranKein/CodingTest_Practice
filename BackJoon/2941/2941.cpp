//
// Created by 김연혁 on 2023/03/23.
//

#include <iostream>

void replace_word(std::string* words, std::string s) {
    std::string::size_type pos;
    while (true) {
        pos = (*words).find(s);
        if (pos != std::string::npos) {
            (*words).replace(pos, s.size(), "*");
        }
        else {
            break;
        }
    }
}

int problem_2941() {
    std::string words;

    std::cin >> words;
    replace_word(&words, "c=");
    replace_word(&words, "c-");
    replace_word(&words, "dz=");
    replace_word(&words, "d-");
    replace_word(&words, "lj");
    replace_word(&words, "nj");
    replace_word(&words, "s=");
    replace_word(&words, "z=");

    std::cout << words.size();
}