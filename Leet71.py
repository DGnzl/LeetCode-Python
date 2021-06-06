import unittest
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

class Testing(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution.simplifyPath(Solution, "/a/./b/../../c/"), "/c")
    def test2(self):
        self.assertEqual(Solution.simplifyPath(Solution, "/home//foo/"), "/home/foo")
    def test3(self):
        self.assertEqual(Solution.simplifyPath(Solution, "/../"), "/")
    def test4(self):
        self.assertEqual(Solution.simplifyPath(Solution, "/home/"), "/home")

if __name__ == "__main__":
    unittest.main()