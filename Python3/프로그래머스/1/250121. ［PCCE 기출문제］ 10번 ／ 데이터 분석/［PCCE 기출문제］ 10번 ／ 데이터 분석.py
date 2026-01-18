def solution(data, ext, val_ext, sort_by):
    index = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    target = index[ext]
    sort = index[sort_by]
    answer = []
    for i in data:
        if i[target] < val_ext:
            answer.append(i)
    answer.sort(key=lambda x: x[sort])
    return answer