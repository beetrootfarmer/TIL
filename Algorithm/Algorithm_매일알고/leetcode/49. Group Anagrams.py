from collections import Counter

def groupAnagrams(strs):
    result = []
    result.append([strs[0]])
    sMap = []
    c = Counter(list(strs[0]))
    sMap.append(dict(c))


    for s in strs[1:]:
        sCnt = dict(Counter(list(s)))
        r = 0
        angrm = False
        for m in range(len(sMap)):
            if sCnt == sMap[m]:
                angrm = True
                r = m
                break
        if angrm:
            result[r].append(s)
        else:
            result.append([s])
            sMap.append(sCnt)
    return result


a = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(a)


def groupAnagrams(strs):
    strs_table = {}

    for string in strs:
        sorted_string = ''.join(sorted(string))

        if sorted_string not in strs_table:
            strs_table[sorted_string] = []

        strs_table[sorted_string].append(string)

    return list(strs_table.values())