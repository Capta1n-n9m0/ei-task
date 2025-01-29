from functools import cached_property


def generate_spiral_matrix(n):
    if n == 0: return []

    matrix = [[0] * n for _ in range(n)]
    c = (n - 1) // 2
    matrix[c][c] = 1

    if n == 1: return matrix

    current_num = 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    current_dir = 0  # start with right direction
    steps_in_current_dir = 1
    row, col = c, c

    while current_num <= n * n:
        dr, dc = directions[current_dir]
        for _ in range(steps_in_current_dir):
            row += dr
            col += dc
            if 0 <= row < n and 0 <= col < n:
                matrix[row][col] = current_num
                current_num += 1
            else:
                # Once we step out, the remaining numbers can't be placed, so break
                break
        # Change direction
        current_dir = (current_dir + 1) % 4
        # Increase steps every two directions (when direction is even: 0 or 2)
        if current_dir % 2 == 0:
            steps_in_current_dir += 1
    return matrix


class SpiralMatrix:
    n: int
    digits: int

    def __init__(self, n: int):
        self.n = n
        self.digits = len(str(n * n))
        self.matrix = generate_spiral_matrix(n)

    @cached_property
    def trace_primary_diagonal(self):
        return sum(self.matrix[i][i] for i in range(self.n))

    @cached_property
    def trace_secondary_diagonal(self):
        return sum(self.matrix[i][self.n - i - 1] for i in range(self.n))

    def __str__(self):
        return "\n".join(" ".join(f"{num:{self.digits}d}" for num in row) for row in self.matrix)

    def __repr__(self):
        return f"SpiralMatrix({self.n})"

    def __eq__(self, other):
        return self.n == other.n and self.matrix == other.matrix

def primary_diagonal_sum_formula(n):
    return (n**3 + 2*n) // 3

def secondary_diagonal_sum_formula(n):
    return (2*n**3 + 3*n**2 + 4*n - 3*(n%2)) // 6

def main():
    for n in range(21):
        print(f"Spiral matrix of size {n}:")
        matrix = SpiralMatrix(n)
        p1 = matrix.trace_primary_diagonal
        s1 = matrix.trace_secondary_diagonal
        p2 = primary_diagonal_sum_formula(n)
        s2 = secondary_diagonal_sum_formula(n)
        print(matrix)
        print(f"Primary diagonal sum: {p1} | Formula: {p2} | Equal: {p1 == p2}")
        print(f"Secondary diagonal sum: {s2} | Formula: {s2} | Equal: {s1 == s2}")
        print()


if __name__ == "__main__":
    main()