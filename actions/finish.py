from requests import post


def finish(headers, score_id, account, student_id, distance):
    data = post('https://tiyun.yzhiee.com/run/finish',
                json={
                    "scoreId": score_id,
                    "code": account,
                    "studentId": student_id,
                    "distance": distance
                }, headers=headers).json()
    return data['message'] == 'success'
