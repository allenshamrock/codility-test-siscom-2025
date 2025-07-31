"""
**SUBSTRING WITH CONCATENATION OF ALL WORDS**

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

"""

"#Solution"


from typing import List
from collections import Counter



def findSubstring(s:str, words:List[str])-> List[int]:
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_l = len(words[0])
        word_c = len(words)
        words_length = word_l*word_c

        if len(s)< words_length:
                return []
        word_counter = Counter(words)
        # start = 0
        result = []

        for i in range(len(s)-words_length  + 1):
                window = s[i:i+words_length]
                words_length_counter = Counter()

                for j in range(0,words_length,word_l):
                        word = window[j:j+ word_l]
                        words_length_counter[word] +=1

                if word_counter == words_length_counter:
                        result.append(i)
        return result


print(findSubstring('barfoofoobarthefoobarman'))   