#ifndef OBJECTIVE_FUNCTION_H
#define OBJECTIVE_FUNCTION_H

// 目标函数接口
class ObjectiveFunction {
public:
    virtual ~ObjectiveFunction() = default;
    
    // 计算目标函数值
    virtual double evaluate(double x, double y, double z) const = 0;
    
    // 获取函数名称
    virtual const char* name() const = 0;
};

// Rastrigin函数实现
class RastriginFunction : public ObjectiveFunction {
public:
    double evaluate(double x, double y, double z) const override;
    const char* name() const override { return "Rastrigin Function"; }
};

// Ackley函数实现
class AckleyFunction : public ObjectiveFunction {
public:
    double evaluate(double x, double y, double z) const override;
    const char* name() const override { return "Ackley Function"; }
};

#endif // OBJECTIVE_FUNCTION_H