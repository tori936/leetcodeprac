class Solution:
    def isPalindrome(self, s: str) -> bool:
        print("s=",s)
        for i in range(len(s)):
            if s[i].isalpha():
                for j in range(len(s)-1,i-1,-1):
                    if s[j].isalpha():
                        print("s[i]=",s[i],"s[j]=",s[j])
                        if s[i].lower()==s[j].lower():
                            return self.isPalindrome(s[i+1:j:1])
                        print("ending")
                        return False
        return True
s="A man, a plan, a canal: Panama"
testor = Solution()
print(testor.isPalindrome(s))
