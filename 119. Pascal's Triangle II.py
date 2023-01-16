class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]

        curr_row = [1, 1]
        for i in range(1, rowIndex):
            next_row = [1]
            for i in range(len(curr_row) - 1):
                next_row.append(curr_row[i] + curr_row[i + 1])
            next_row.append(1)

            curr_row = next_row

        return curr_row