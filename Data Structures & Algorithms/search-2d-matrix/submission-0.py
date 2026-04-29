class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_outer, r_outer = 0, len(matrix) - 1

        while l_outer <= r_outer:
            m_outer = (l_outer + r_outer) // 2

            if target >= matrix[m_outer][0] and target <= matrix[m_outer][-1]:
                l_inner, r_inner = 0, len(matrix[m_outer]) - 1

                while l_inner <= r_inner:
                    m_inner = (l_inner + r_inner) // 2

                    if matrix[m_outer][m_inner] == target:
                        return True
                    elif matrix[m_outer][m_inner] > target:
                        r_inner = m_inner - 1
                    else:
                        l_inner = m_inner + 1
                return False

            elif matrix[m_outer][0] > target:
                r_outer = m_outer - 1
            else:
                l_outer = m_outer + 1
        return False