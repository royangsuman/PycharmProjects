import requests
import json
import jsonpath
from conftest import ValueStorage

def test_AddStudent():
    global idv
    student_api = "http://thetestingworldapi.com/api/studentsDetails"
    readStdDatFile = open('C://Users//Angsuman//PycharmProjects//APITesting//stdReq.json','r')
    json_req = json.loads(readStdDatFile.read())
    response = requests.post(student_api,json_req)
    idv = jsonpath.jsonpath(response.json(),'id')
       
def test_AddTech():
    tech_api = "http://thetestingworldapi.com/api/technicalskills"
    readTechData = open('C://Users//Angsuman//PycharmProjects//APITesting//techReq.json','r')
    json_request = json.loads(readTechData.read())    
    json_request['id'] = idv[0]
    json_request['st_id'] = idv[0]
    requests.post(tech_api,json_request)
    

def test_address():
    address_api = "http://thetestingworldapi.com/api/addresses"
    readAddressData = open('C://Users//Angsuman//PycharmProjects//APITesting//addressReq.json','r')
    json_request = json.loads(readAddressData.read())
    requests.post(address_api,json_request)

def test_finalURL():
    FINAL_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/520870"
    response = requests.get(FINAL_URL)
    print(response.text)
