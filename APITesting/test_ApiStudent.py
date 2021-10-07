import requests
import json
import jsonpath

def test_post_Student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails"
    fileData = open('C:/Users/Angsuman/PycharmProjects/APITesting/RequestJson.json','r')
    json_request = json.loads(fileData.read())
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    API_URM = "http://thetestingworldapi.com/api/studentsDetails/461705"
    response = requests.get(API_URM)
    #print(response.text)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 461705

def test_put_student_data():
    API_URL= "http://thetestingworldapi.com/api/studentsDetails/461705"
    fileData = open('C://Users//Angsuman//PycharmProjects//APITesting//RequestJsonPut.json','r')
    jsonrequest = json.loads(fileData.read())
    response = requests.put(API_URL,jsonrequest)
    print(response.text)
    
def test_gettestforPut_student_data():
    API_URM = "http://thetestingworldapi.com/api/studentsDetails/461705"
    response = requests.get(API_URM)
    json_response = response.json()
    print(json_response)