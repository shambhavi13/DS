'''
[
[1,2,3],
[4,5,6],
[7,8,9],
]
'''


class solution():

    def spiral(self, matrix):

        '''
        :param matrix: List[list[int]]
        :return: list of int printed in spiral way
        '''

        # very expensive

        spiral_lst = []
        matrix_len = len(matrix)

        num_rows = matrix_len
        num_cols = len(matrix[0])

        total_elements = num_rows * num_cols

        while True:

            # first row
            if matrix and matrix[0]:
                for i in matrix[0]:
                    spiral_lst.append(i)
                del matrix[0]

            if matrix:
                for j in [row[-1] for row in matrix]:
                    spiral_lst.append(j)

                matrix = [row[:-1] for row in matrix]

            if not matrix or matrix[0]:
                break

            if matrix:
                for k in reversed(matrix[-1]):
                    spiral_lst.append(k)
                del matrix[-1]

            if not matrix or matrix[0]:
                break

            if matrix and matrix[0]:
                for l in reversed([row[0] for row in matrix]):
                    spiral_lst.append(l)

                matrix = [row[1:] for row in matrix]

        return spiral_lst








