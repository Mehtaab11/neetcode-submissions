class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        d, e, f = 0 , 0 , 0

        for t in triplets:
            if not (t[0] <= a and t[1] <= b and t[2] <= c):
                continue 
            d = max(d, t[0])
            e = max(e, t[1])
            f = max(f, t[2])

        return (a , b, c )==( d , e,f)