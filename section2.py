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

    def __str__(self):
        return "\n".join(" ".join(f"{num:{self.digits}d}" for num in row) for row in self.matrix)


def main():
    for n in range(21):
        print(f"Spiral matrix of size {n}:")
        print(SpiralMatrix(n))
        print()


if __name__ == "__main__":
    main()