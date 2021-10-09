import requests
import json
import jsonpath

def test_postStd():
    global data
    api_url = "http://thetestingworldapi.com/api/studentsDetails"
    student_api = "http://thetestingworldapi.com/api/studentsDetails"
    readStdDatFile = open('C://Users//Angsuman//PycharmProjects//APITesting//stdReq.json','r')
    json_req = json.loads(readStdDatFile.read())
    response = requests.post(student_api,json_req)
    data = jsonpath.jsonpath(response.json(),'id')


def test_getStd():
    print(data[0])
    api_u = "http://thetestingworldapi.com/api/studentsDetails/"+str(data[0])
    resp = requests.get(api_u)
    print(resp.text)
