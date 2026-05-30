class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = self.clean(s)

        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True

    def clean(self, s: str) -> str:
        lowered = s.lower()

        return re.sub(r'[^a-z0-9]', '', lowered)