class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __add__(self, other):
        return Cell(self.num_of_cells + other.num_of_cells)

    def __sub__(self, other):
        return Cell(self.num_of_cells - other.num_of_cells)

    def __mul__(self, other):
        return Cell(self.num_of_cells * other.num_of_cells)

    def __truediv__(self, other):
        return Cell(round(self.num_of_cells / other.num_of_cells))

cell1 = Cell(12)
cell2 = Cell(5)

cell3 = cell1 + cell2
cell4 = cell1 - cell2
cell5 = cell1 * cell2
cell6 = cell1 / cell2

print(cell3.num_of_cells)
print(cell4.num_of_cells)
print(cell5.num_of_cells)
print(cell6.num_of_cells)
