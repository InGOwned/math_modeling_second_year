class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if self.size() != other.size():
            print("Размеры матриц должны совпадать")
            return None
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __sub__(self, other):
        if self.size() != other.size():
            print("Размеры матриц должны совпадать")
            return None
        return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[self.matrix[i][j] * other for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            print("Оператор умножения может быть использован только с числом")
            return None

    def __matmul__(self, other):
        if self.size() != other.size():
            print("Размеры матриц должны совпадать")
            return None
        return Matrix([[self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.matrix])

    def size(self):
        return len(self.matrix), len(self.matrix[0])


# Создаем две матрицы
matrix1 = Matrix([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
matrix2 = Matrix([[10, 20, 30], 
                  [40, 50, 60], 
                  [70, 80, 90]])

# Складываем матрицы
matrix3 = matrix1 + matrix2
print(f"Результат сложения матриц:")
print(matrix3)

# Вычитаем матрицы
matrix4 = matrix1 - matrix2
print("\nРезультат вычитания матриц:")
print(matrix4)

# Умножаем матрицу на число
matrix5 = matrix1 * 2
print("\nРезультат умножения матрицы на число:")
print(matrix5)

# Умножаем матрицы друг на друга
matrix6 = matrix1 @ matrix2
print("\nРезультат умножения матриц друг на друга:")
print(matrix6)
