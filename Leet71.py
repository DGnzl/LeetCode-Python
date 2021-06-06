class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for x in path.split("/"):
            if x == "..":
                if len(stack):
                    stack.pop()
            elif x == "." or not x:
                pass
            else:
                stack.append(x)
        return "/" + "/".join(stack)

print(Solution.simplifyPath(Solution, "/a/./b/../../c/"))
print(Solution.simplifyPath(Solution, "/home//foo/"))
print(Solution.simplifyPath(Solution, "/../"))
print(Solution.simplifyPath(Solution, "/home/"))