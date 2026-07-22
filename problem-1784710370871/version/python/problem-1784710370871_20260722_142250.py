# Last updated: 7/22/2026, 2:22:50 PM
1class Solution:
2    def reorganizeString(self, s: str) -> str:
3        count=Counter(s)
4        MaxHeap=[]
5        for char,cnt in count.items():
6            MaxHeap.append([-cnt,char])
7        heapq.heapify(MaxHeap)
8        prev=None
9        res=""
10        while MaxHeap or prev:
11            if prev and not MaxHeap:
12                return ""
13            cnt,char=heapq.heappop(MaxHeap)
14            res+=char
15            cnt+=1
16
17            if prev:
18                heapq.heappush(MaxHeap,prev)
19                prev=None
20            if cnt!=0:
21                prev=[cnt,char]
22        return res
23