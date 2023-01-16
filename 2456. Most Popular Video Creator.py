from collections import defaultdict
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        # { name: [views, (most_popular_views, id)] }
        # iterate through all the creators, ids, and views. Update dictionary accordingly.
        creators_views = defaultdict(lambda: [0, (-1, "")])
        for i in range(len(creators)):
            curr_views = creators_views[creators[i]][0]
            curr_most_popular_video = creators_views[creators[i]][1]

            creators_views[creators[i]][0] = curr_views + views[i]
            creators_views[creators[i]][1] = (views[i], ids[i]) if curr_most_popular_video[0] < views[i] or (curr_most_popular_video[0] == views[i] and ids[i] < curr_most_popular_video[1]) else curr_most_popular_video

        # convert dictionary into a sortable list - TC: O(n)
        creators_views_list = list(map(lambda creator_views_key: (creators_views[creator_views_key][0], creator_views_key, creators_views[creator_views_key][1][1]), creators_views))

        # sort list - TC: O(n * log n)
        creators_views_list.sort(reverse=True)

        # extract answers - TC: O(n)
        i, ans = 0, []
        while i < len(creators_views_list) and creators_views_list[0][0] == creators_views_list[i][0]:
            ans.append([creators_views_list[i][1], creators_views_list[i][2]])
            i += 1

        return ans