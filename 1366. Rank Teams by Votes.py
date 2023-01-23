class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        keys = {team: [0] * len(votes[0]) + [-ord(team)] for team in votes[0]}
        
        for vote in votes:
            for i, team in enumerate(vote):
                keys[team][i] += 1
        
        return "".join( sorted(votes[0], key = keys.get, reverse = True) )