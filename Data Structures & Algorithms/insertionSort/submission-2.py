# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs)==0:
            return []
        outputs = []
        tmp = []
        # for p in pairs:
        #     #print(p.key,p.value)
        #     tup = (p.key,p.value)
        #     #print(tup)
        #     tmp.append(tup)
        outputs.append(pairs[:])
        #print(outputs)
        for i in range(1 , len(pairs)):
            #print(pairs)
            j = i -1
            while j >= 0 and pairs[j].key >pairs[j+1].key:
                tmp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = tmp
                j -=1
            #outputs.append(pairs)
            # tmp = []
            # for p in pairs:
            # #print(p.key,p.value)
            #     tup = (p.key,p.value)
            #     #print(tup)
            #     tmp.append(tup)
            outputs.append(pairs[:])
        #print(outputs)
        return outputs