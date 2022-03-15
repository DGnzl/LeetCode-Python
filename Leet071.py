import unittest
# Medium
# Stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        #Create stack to keep track of the full path
        stack = []
        # Iterate through each part of the input, divided by /
        for x in path.split("/"):
            # If the stack has elements, remove the last element (per '..')
            if x == "..":
                if stack:
                    stack.pop()
            # Else if x is not empty or null and x does not equal '.' add element to stack
            elif x and x != ".":
                stack.append(x)
        # Return a '/' plus all the elements in the stack combined by '/'
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