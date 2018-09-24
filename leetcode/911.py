class TopVotedCandidate(object):
    '''
    init: O(N)
    q: O(logN)
    space: O(N)
    注意binary search的边界
    '''
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        votes = [0] * len(persons)
        maxVote = -1
        self.times = times
        self.toLeader = {}
        for i in range(len(persons)):
            votes[persons[i]] += 1
            maxVote = max(persons[i], maxVote, key=lambda x: votes[x])
            self.toLeader[times[i]] = maxVote
        

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t in self.toLeader:
            return self.toLeader[t]
        start = 0
        end = len(self.times)
        while start < end-1:
            m = (start+end) // 2
            if self.times[m] <= t:
                start = m
            else:
                end = m
        return self.toLeader[self.times[start]]
