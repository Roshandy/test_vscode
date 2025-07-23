#define _USE_MATH_DEFINES // 使用math中的宏定义（M_PI）

#include "ObjectiveFunction.hpp"
#include <cmath>
#include <iostream>

double RastriginFunction::evaluate(double x, double y, double z) const {
    constexpr double A = 10.0;
    double result = 3 * A;
    result += x*x - A * std::cos(2 * M_PI * x);
    result += y*y - A * std::cos(2 * M_PI * y);
    result += z*z - A * std::cos(2 * M_PI * z);
    return -result; // 求最大值，所以取负
}

double AckleyFunction::evaluate(double x, double y, double z) const {
    constexpr double a = 20.0;
    constexpr double b = 0.2;
    constexpr double c = 2 * M_PI;
    
    double sum_sq = x*x + y*y + z*z;
    double sum_cos = std::cos(c*x) + std::cos(c*y) + std::cos(c*z);
    
    double term1 = -a * std::exp(-b * std::sqrt(sum_sq / 3.0));
    double term2 = -std::exp(sum_cos / 3.0);
    
    return -(term1 + term2 + a + std::exp(1.0));
}