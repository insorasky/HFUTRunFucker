from requests import get


def get_task(headers):
    data = get('https://tiyun.yzhiee.com/run/task', headers=headers).json()

    class Task:
        def __init__(self, task_data):
            self.raw_data = task_data
            self.name = task_data['data']['name']
            self.id = task_data['data']['id']
            self.done = task_data['data']['doneDistance']
    return Task(data)
