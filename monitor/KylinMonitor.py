# -*- coding:utf-8 -*-
import requests
import json

RootUrl = "http://xx.xx.xx.xx:7070/"

headers = {
    "Authorization": "Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "Content-Type": "application/json;charset=UTF-8"
}


# 获取kylin列表
def getKylinList():
    # 获取所有列表
    # url = RootUrl + "/kylin/api/jobs?jobSearchMode=ALL&limit=15&offset=0&timeFilter=1"
    # 获取所有错误列表
    url = RootUrl + "/kylin/api/jobs?jobSearchMode=ALL&limit=15&offset=0&status=8&timeFilter=1"

    req = requests.get(url, headers=headers).content.decode("UTF8")
    reqJsonList = json.loads(req)

    ids = []
    for index in range(len(reqJsonList)):
        data = reqJsonList[index]
        uuid = data.get("uuid")
        relatedCube = data.get("related_cube")
        dict = {"uuid": uuid, 'relatedCube': relatedCube}
        ids.append(dict)

    return ids


# 移除kylin任务
def dropKylinJob(job_id):
    # 移除接口
    url = RootUrl + "/kylin/api/jobs/{}/drop".format(job_id)

    req = requests.delete(url, headers=headers).content.decode("UTF8")
    data = json.loads(req)
    print(data)


# 刷新kylin任务,时间为UTC的毫秒值，
def refreshKylinJob(cube, start_time, end_time):
    # refresh接口
    url = RootUrl + "/kylin/api/cubes/{}/rebuild".format(cube)
    data = {"buildType": "REFRESH", "startTime": start_time, "endTime": end_time,
            "forceMergeEmptySegment": "false"}
    req = requests.put(url, data=data, headers=headers).content.decode("UTF8")
    data = json.loads(req)
    print(data)


# 获取Cube的详细信息
def getCube(cube_name):
    # 获取Cube接口
    url = RootUrl + "/kylin/api/cubes?cubeName={}&limit=15&offset=0".format(cube_name)
    req = requests.get(url, headers=headers).content.decode("UTF8")
    cube = json.loads(req)
    print(cube)


# 跟踪Cube任务状态
def kylinJobStatus(job_id):
    # 跟踪Cube接口
    url = RootUrl + "/kylin/api/jobs/{}".format(job_id)
    req = requests.get(url, headers=headers).content.decode("UTF8")
    cube = json.loads(req)
    print(cube)


# 重新开始Cube任务
def kylinResumeJob(job_id):
    # 重新开始Cube接口
    url = RootUrl + "/kylin/api/jobs/{}/resume".format(job_id)
    req = requests.get(url, headers=headers).content.decode("UTF8")
    cube = json.loads(req)
    print(cube)


if __name__ == '__main__':
    # ids = getKylinList()
    # for id in ids:
    #     dropKylinJob(id)
    getCube("realtime_pay_cube_v1")
