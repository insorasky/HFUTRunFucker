from requests import post


def start(headers, task_id, student_id):
    data = post('https://tiyun.yzhiee.com/run/start',
                json={
                    'taskId': task_id,
                    'relationId': student_id
                }, headers=headers).json()
    return data['data']['id'] if data['message'] == 'success' else False
