# this function is used to find the same or reversed substring in one string. and return the numbers of the substrings you find
# for example: if string str1 is 'abcbb', you will have below pairs of strings
# for 'b, b', it's (str1[1] and str1[3]) or (str1[1] and str1[1] and str1[4]) or (str1[3] and str1[4])
# for 'bc,cb', it's str1[1:3] and str1[2:4]
# so tatal 4 pairs



def sameOrReversedStringCheck(s):
    map={}
    s=s.strip()
    # i is the length of the substring, starting from 1 and ending at len(s)
    for i in range(1,len(s)):
        #j is the position of the substring, starting from 0 and ending at len(s)
        for j in range(len(s)-i+1):
            #get the substring for checking
            s1=s[j:j+i]
            #get each of other substring you want to compare with the current s1. you don't compare backwords, just compare forward. so starting at j+1
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
