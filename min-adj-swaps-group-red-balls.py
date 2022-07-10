from collections import Counter
def min_swaps(s: str) -> int:
    count = 0
    left,right = 0, len(s)-1
    
    while left < right:
        if s[left] == s[right] == 'R':
            c = Counter(s[left:right+1])
            count += c['W']
            if count > 10000000000:
                return -1
            left+=1
            right-=1
        if s[left] != 'R':
            left+=1
        if s[right] != 'R':
            right-=1
            
    return count 
        

if __name__ == '__main__':
    s = input()
    res = min_swaps(s)
    print(res)
