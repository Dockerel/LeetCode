import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = "".join(s.split())
        str2 = re.sub(r"[^a-zA-Z0-9]", "", str1)
        str3=str2.lower()
        list1=list(str3.lower())
        list2=list(reversed(str3))
        if list1 == list2:
            return True
        else:
            return False