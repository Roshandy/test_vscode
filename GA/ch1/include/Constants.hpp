#ifndef CONSTANTS_H
#define CONSTANTS_H

// 定义域范围 [min, max]
constexpr double DOMAIN_MIN = -5.0;
constexpr double DOMAIN_MAX = 5.0;

// 遗传算法参数
constexpr int POPULATION_SIZE = 100;      // 初始种群数
constexpr int MAX_GENERATIONS = 200;      // 最大遗传代数
constexpr double CROSSOVER_RATE = 0.8;    // 交配繁殖概率
constexpr double MUTATION_RATE = 0.1;     // 变异概率
constexpr double MUTATION_STRENGTH = 0.5; // 变异强度
constexpr int TOURNAMENT_SIZE = 3;        // 锦标赛选择的大小
constexpr int ELITISM_COUNT = 2;          // 精英保留数量

#endif // CONSTANTS_H