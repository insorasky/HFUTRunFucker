from requests import get


def get_rank(headers):
    data = get('https://tiyun.yzhiee.com/run/getRank', headers=headers, verify=False).json()

    class Rank:
        def __init__(self, rank_data):
            self.distance = rank_data['data']['distance']
            self.rank = rank_data['data']['rank']
            self.raw_data = rank_data
    return Rank(data)
