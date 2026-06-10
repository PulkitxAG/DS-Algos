class Solution:
    def integerReplacement(self, n: int) -> int:
        op=0
        while n>1:
            if n%2==0:
                n=int(n/2)
                op+=1
            else:
                if n%4==1:
                    n=n-1
                elif n==3:
                    n-=1
                elif n%4==3:
                    n+=1
                op+=1
        return op