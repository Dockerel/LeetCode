class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        elif x<10: return True
        l=list(str(x))
        
        l1=l[:((len(l)-1)//2)+1]
        l2=l[len(l)//2:]
        
        lenl=len(l1)
        n=0
        while n<lenl:
            if(l1[n]!=l2[lenl-1-n]):
                return False
            n+=1
        return True