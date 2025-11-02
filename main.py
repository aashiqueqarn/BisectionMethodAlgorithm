from sympy import symbols, diff, sympify
import re

class BisectionMethodAlgorithm:
    def __init__(self, boundary_a, boundary_b, stopping_interval_length):
        self.boundary_a = boundary_a
        self.boundary_b = boundary_b
        self.stopping_interval_length = stopping_interval_length

    @staticmethod
    def calculate_boundary_diff_l(boundary_a, boundary_b):
        return boundary_b - boundary_a

    @staticmethod
    def modify_equation_string(expression_string, symbol):
        expression_string = expression_string.replace('−', '-')
        expression_string = expression_string.replace('x', '*x')
        expression_string = expression_string.replace('**x', 'x')
        expression_string = expression_string.replace(' ', '')
        expression_string = expression_string.replace('x4', 'x**4')
        expression_string = expression_string.replace('x3', 'x**3')
        expression_string = expression_string.replace('x2', 'x**2')

        x = symbols(symbol)
        expression = sympify(expression_string)
        return expression, x

    def evaluate_equation(self, expression_string, symbol, symbol_value):
        expression, x = self.modify_equation_string(expression_string, symbol)
        x_value = symbol_value
        result = expression.subs(x, x_value)
        return result

    @staticmethod
    def evaluate_differential_equation(expression_string, symbol, symbol_value):
        return expression_string.subs(symbol, symbol_value)

    def find_derivative(self, equation, symbol):
        expression, x = self.modify_equation_string(equation, symbol)
        result = diff(expression, x)
        print(f"The differential is: {result}")
        return result

    def calculate_function(self, equation, symbol):
        count = 0
        f_prime_func = self.find_derivative(equation, symbol)
        optimal_solution = None
        while self.calculate_boundary_diff_l(self.boundary_a, self.boundary_b) > self.stopping_interval_length:
            print("=" * 50)
            print("The iteration count is: ", count)
            count += 1
            midpoint = (self.boundary_a + self.boundary_b) / 2
            f_prime_func_midpoint = self.evaluate_differential_equation(f_prime_func, symbol, midpoint)
            print(f"The function value of f'(x): {f_prime_func_midpoint}")
            if f_prime_func_midpoint == 0:
                optimal_solution = midpoint
                print(f"Found the optimal solution: {optimal_solution}")
                break
            elif f_prime_func_midpoint > 0:
                self.boundary_a = self.boundary_a
                self.boundary_b = midpoint
            else:
                self.boundary_a = midpoint
                self.boundary_b = self.boundary_b
            print(f"The updated boundary is [a, b]: [{self.boundary_a}, {self.boundary_b}]")
            print("=" * 50)

        if optimal_solution:
            print(f"The actual minimum is at point x: {optimal_solution}")
            func_value = self.evaluate_equation(equation, symbol, optimal_solution)
            print(f"The function value is f(x): {func_value}")
        else:
            x_best = (self.boundary_a + self.boundary_b) / 2
            print(f"The actual minimum is at point x: {x_best}")
            func_value = self.evaluate_equation(equation, symbol, x_best)
            print(f"The function value is f(x): {func_value}")


a = -4
b = 0
evaluation_string = "(1/ 4)x4 − (5/ 3)x3 − 6x2 + 19x − 7"
bisectionMethodAlgo = BisectionMethodAlgorithm(a, b, 0.5)
bisectionMethodAlgo.calculate_function(evaluation_string, 'x')