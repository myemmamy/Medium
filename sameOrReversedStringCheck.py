# this function is used to find the same or reversed substring in one string. and return the numbers of the substrings you find
# for example: if string str1 is 'abcbb', you will have below pairs of strings
# for 'b, b', it's (str1[1] and str1[3]) or (str1[1] and str1[1] and str1[4]) or (str1[3] and str1[4])
# for 'bc,cb', it's str1[1:3] and str1[2:4]
# so tatal 4 pairs



def sameOrReversedStringCheck(s):
    map={}
    s=s.strip()
    for i in range(1,len(s)):
        for j in range(len(s)-i+1):
            s1=s[j:j+i]
            for x in range(j+1,len(s)-i+1):
                s2=s[x:x+i]
                if s1==''.join(s2[::-1]) or s1 == s2:
                    map[s1] = map.get(s1,0) + 1
    num=0
    for tmp_str in map:
        num += map[tmp_str]
    return num

if __name__ == '__main__':
    print(sameOrReversedStringCheck('ifailuhkqq'))
