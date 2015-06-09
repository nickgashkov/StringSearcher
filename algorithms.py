# -*- coding: utf-8 -*-

"""Module for string searching algorithms

implemented algorithms:
Naive string search algorithm
Boyer-Moore string search algorithm
Boyer-Moore-Horspool string search algorithm
Rabin-Karp string search algorithm
Knuth-Morris-Pratt string search algorithm

"""

from tkinter import *

import time

def naive(haystack, needle):
    """Searching string using naive string search algorithm

    keyword arguments:
    haystack -- text to be searched
    needle -- pattern to search

    """
    naiveResult = StringVar()
    t = time.perf_counter()
    for i in range(len(haystack) - len(needle) + 1):
        match = True
        for j in range(len(needle)):
            if needle[j] != haystack[i+j]:
                match = False
                break
        if match:
            result = "pos: %i"%i, "time: %f"%(time.perf_counter() - t)
            naiveResult.set(result)
            return(naiveResult)

def generate_bad_char_shift(term):
    skipList = {}
    for i in range(0, len(term) - 1):
        skipList[term[i]] = len(term) - i - 1
    return skipList

def find_suffix_position(badChar, suffix, fullTerm):
    for offset in range(1, len(fullTerm) + 1)[::-1]:
        match = True
        for suffixIndex in range(0, len(suffix)):
            termIndex = offset - len(suffix) - 1 + suffixIndex
            if termIndex < 0 or suffix[suffixIndex] == fullTerm[termIndex]:
                pass
            else:
                match = False
        termIndex = offset - len(suffix) - 1
        if match and (termIndex <= 0 or fullTerm[termIndex-1] != badChar):
            return len(fullTerm) - offset + 1

def generate_suffix_shift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = find_suffix_position(key[len(key)-1-i], buffer, key)
        buffer = key[len(key)-1-i] + buffer
    return skipList

def boyer_moore(haystack, needle):
    """Searching string using Boyer-Moore string search algorithm

    keyword arguments:
    haystack -- text to be searched
    needle -- pattern to search

    """
    bmResult = StringVar()
    t = time.perf_counter()
    goodSuffix = generate_suffix_shift(needle)
    badChar = generate_bad_char_shift(needle)
    i = 0
    while i < len(haystack) - len(needle) + 1:
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
            result = "pos: %i"%i, "time: %f"%(time.perf_counter() - t)
            bmResult.set(result)
            return(bmResult)

def boyer_moore_horspool(haystack, needle):
    """Searching string using Boyer-Moore-Horspool string search algorithm

    keyword arguments:
    haystack -- text to be searched
    needle -- pattern to search

    """
    bmhResult = StringVar()
    t = time.perf_counter()
    n = len(haystack)
    m = len(needle)
    skip = []
    for k in range(256):
        skip.append(m)
    for k in range(m - 1):
        skip[ord(needle[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and haystack[i] == needle[j]:
            j -= 1
            i -= 1
        if j == -1:
            result = "pos: %i"%(i+1), "time: %f"%(time.perf_counter() - t)
            bmhResult.set(result)
            return(bmhResult)
        k += skip[ord(haystack[k])]

def rabin_karp(haystack, needle, d, q):
    """Searching string using Rabin-Karp string search algorithm

    keyword arguments:
    haystack -- text to be searched
    needle -- pattern to search

    """
    rkResult = StringVar()
    t = time.perf_counter()
    n = len(haystack)
    m = len(needle)
    h = pow(d, m-1)%q
    p = 0
    w = 0
    output = []
    for i in range(m):
        p = (d * p + ord(needle[i]))%q
        w = (d * w + ord(haystack[i]))%q
    for s in range(n - m + 1):
        if p == w:
            match = True
            for i in range(m):
                if needle[i] != haystack[s+i]:
                    match = False
                    break
            if match:
                output = output + [s]
        if s < n - m:
            w = (w - h * ord(haystack[s]))%q
            w = (w * d + ord(haystack[s+m]))%q
            w = (w + q)%q
    result = "pos: %i"%output[0], "time: %f"%(time.perf_counter() - t)
    rkResult.set(result)
    return(rkResult)

def knuth_morris_pratt(haystack, needle):
    """Searching string using Knuth-Morris-Pratt string search algorithm

    keyword arguments:
    haystack -- text to be searched
    needle -- pattern to search

    """
    kmpResult = StringVar()
    t = time.perf_counter()
    lsp = [0]
    for c in needle[1:]:
        j = lsp[-1]
        while j > 0 and c != needle[j]:
            j = lsp[j-1]
        if c == needle[j]:
            j += 1
        lsp.append(j)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = lsp[j-1]
        if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
                result = "pos: %i"%(i - (j - 1)), "time: %f"%(time.perf_counter() - t)
                kmpResult.set(result)
                return(kmpResult)
