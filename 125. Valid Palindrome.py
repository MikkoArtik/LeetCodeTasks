

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            left_sym = s[i]
            if not (left_sym.isalpha() or left_sym.isdigit()):
                i += 1
                continue

            right_sym = s[j]
            if not (right_sym.isalpha() or right_sym.isdigit()):
                j -= 1
                continue

            if left_sym.lower() == right_sym.lower():
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s))