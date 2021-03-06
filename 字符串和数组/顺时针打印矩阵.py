'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res
        l, r, u, d = 0, len(matrix[0])-1, 0, len(matrix)-1
        i = 0
        while True:
            for a in range(l,r+1): res.append(matrix[u][a])
            u += 1
            if u > d: break
            for b in range(u,d+1): res.append(matrix[b][r])
            r -= 1
            if r < l: break
            for c in range(r, l-1, -1): res.append(matrix[d][c])
            d -= 1
            if d < u : break
            for w in range(d, u-1, -1): res.append(matrix[w][l])
            l += 1
            if l > r : break
        return res

 #将矩阵第一行的元素添加到 res 列表里，删除第一行（也就是 matrix 中的第一个列表），然后逆时针旋转（这里通过转置+倒序实现），新的 matrix 的第一行即为接下来要打印的元素。
    #    while matrix:
    #        res += matrix.pop(0)
    #        matrix = list(zip(*matrix))[::-1]
    #    return res