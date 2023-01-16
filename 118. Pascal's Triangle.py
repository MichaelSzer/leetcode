class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]

        pascal_triangle = [[1], [1, 1]]
        for num_row in range(2, numRows):
            new_row = [1]
            for i in range(1, num_row):
                new_row.append(pascal_triangle[num_row - 1][i] + pascal_triangle[num_row - 1][i - 1])

            new_row.append(1)
            pascal_triangle.append(new_row)

        return pascal_triangle