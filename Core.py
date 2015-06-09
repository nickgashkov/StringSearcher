import time

####################
# Primitive Search #
#####################

def Primitive(haystack, needle):
    t = time.perf_counter()
    index = -1
    for i in range(len(haystack)-len(needle)+1):
        success = True
        for j in range(len(needle)):
            if needle[j] != haystack[i+j]:
                success = False
                break
        if success:
            print('Pattern «' + needle + '» found at position',i,'%f'%(time.perf_counter() - t))
            break

######################
# Boyer-Moore Search #
######################       

def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term)-1):
        skipList[term[i]] = len(term)-i-1
    return skipList
 
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term)+1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset-len(suffix)-1+suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset-len(suffix)-1
        if flag and (term_index <= 0 or full_term[term_index-1] != badchar):
            return len(full_term)-offset+1
 
def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList
    
def BoyerMoore(haystack, needle):
    t = time.perf_counter()
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    while i < len(haystack)-len(needle)+1:
        j = len(needle)
        while j > 0 and needle[j-1] == haystack[i+j-1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i+j-1], len(needle))
            goodSuffixShift = goodSuffix[len(needle)-j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            print('Pattern «' + needle + '» found at position',i,'%f'%(time.perf_counter() - t))
            break

###############################
# Boyer-Moore-Horspool Search #
###############################

def BoyerMooreHorspool(haystack, needle):
    t = time.perf_counter()
    n = len(haystack)
    m = len(needle)
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(needle[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and haystack[i] == needle[j]:
            j -= 1; i -= 1
        if j == -1: print('Pattern «' + needle + '» found at position',i + 1,'%f'%(time.perf_counter() - t))
        k += skip[ord(haystack[k])]

##############
# Rabin-Karp #
##############

def RabinKarp(haystack, needle, d, q):
    t = time.perf_counter()
    n = len(haystack)
    m = len(needle)
    h = pow(d, m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = (d*p+ord(needle[i]))%q
        t = (d*t+ord(haystack[i]))%q
    for s in range(n-m+1):
        if p == t:
            match = True
            for i in range(m):
                if needle[i] != haystack[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(haystack[s]))%q
            t = (t*d+ord(haystack[s+m]))%q
            t = (t+q)%q
    print('Pattern «' + needle + '» found at position',result[0],'%f'%(time.perf_counter() - t))

######################
# Knuth-Morris-Pratt #
######################

def KnuthMorrisPratt(haystack, needle):
    t = time.perf_counter()
    if needle == "":
        return 0

    lsp = [0]
    for c in needle[1 : ]:
        j = lsp[-1]
        while j > 0 and c != needle[j]:
            j = lsp[j - 1]
        if c == needle[j]:
            j += 1
        lsp.append(j)

    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = lsp[j - 1]
        if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
                print('Pattern «' + needle + '» found at position',i - (j - 1),'%f'%(time.perf_counter() - t))
    return None

#########
# Whole #
#########

def Whole(haystack, needle):
    Primitive(haystack, needle)
    BoyerMoore(haystack, needle)
    BoyerMooreHorspool(haystack, needle)
    RabinKarp(haystack, needle, 1, 1)
    KnuthMorrisPratt(haystack, needle)
