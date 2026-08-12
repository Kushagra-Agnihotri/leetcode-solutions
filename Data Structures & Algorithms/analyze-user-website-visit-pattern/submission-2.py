class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        packed_data = sorted(zip(timestamp, username, website))
        hs = defaultdict(list)
        for t, u, w in packed_data:
            hs[u].append(w)
        print(hs)
        patterns_count = Counter()
        for k , v in hs.items():
            user_patterns  = set(combinations(v, 3))
            for p in user_patterns:
                patterns_count[p] +=1
        

        result = sorted(patterns_count.items(), key=lambda x: (-x[1], x[0]))
        return list(result[0][0])
            