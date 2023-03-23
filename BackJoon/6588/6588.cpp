//
// Created by 김연혁 on 2023/03/22.
//
#include "6588.h"
#include <iostream>
#include <cmath>
#include <vector>

#define MAX 1000000

int problem_6588() {
    bool prime_list_bool[MAX+1] = {};
    for (int i = 0; i < MAX; i++) {
        prime_list_bool[i] = true;
    }
    prime_list_bool[0] = false;
    prime_list_bool[1] = false;

    std::vector<int> prime_list;

    for (int i = 2; i < int(sqrt(MAX)) + 1; i++) {
        if (prime_list_bool[i]) {
            for (int j = i+i; j < MAX + 1; j += i) {
                prime_list_bool[j] = false;
            }
            prime_list.push_back(i);
        }
    }

    int n;
    bool found = false;
    while (1) {
        std::cin >> n;
        if (n == 0) {
            break;
        }

        for (int i; i < prime_list.size() + 1; i++) {
            int prime = prime_list[i];
            if (prime > n) {
                break;
            }
            if (prime_list_bool[n - prime]) {
                std::cout << n << " = " << prime << " + " << n - prime << "\n";
                found = true;
                break;
            }
        }

        if (!found) {
            std::cout << "Goldbach's conjecture is wrong.";
        }
    }

    return 0;
}
