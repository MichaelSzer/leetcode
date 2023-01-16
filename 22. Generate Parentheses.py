class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(i, available_parentheses, close_parentheses = 0, combination = ""):
            nonlocal ans, n

            if i == 0:
                ans.append(combination)

            if n - available_parentheses > close_parentheses:
                dfs(i - 1, available_parentheses, close_parentheses + 1, combination + ")")
            
            if available_parentheses > 0:
                dfs(i - 1, available_parentheses - 1, close_parentheses, combination + "(")

        dfs(n * 2, n)
        return ans