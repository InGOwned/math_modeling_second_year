class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return Cell(self.num_cells + other.num_cells)

    def __sub__(self, other):
        if self.num_cells < other.num_cells:
            return ("Разность клеток не может быть отрицательной")
        return Cell(self.num_cells - other.num_cells)

    def __mul__(self, other):
        return Cell(self.num_cells * other.num_cells)

    def __truediv__(self, other):
        return Cell(round(self.num_cells / other.num_cells))

cell1 = Cell(12)
cell2 = Cell(5)

cell3 = cell1 + cell2
cell4 = cell1 - cell2
cell5 = cell1 * cell2
cell6 = cell1 / cell2

print(cell3.num_cells)
print(cell4.num_cells)
print(cell5.num_cells)
print(cell6.num_cells)
