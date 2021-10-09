import requests
import json

from requests.models import Response
import jsonpath

def test_add_new_std():
   STUDENT_API_URL= "http://thetestingworldapi.com/api/studentsDetails"
   fileStd = open('C://Users//Angsuman//PycharmProjects//APITesting//RequestJson.json','r')
   json_request = json.loads(fileStd.read())
   response = requests.post(STUDENT_API_URL,json_request)
   id = jsonpath.jsonpath(response.json(),'id')
   print(id[0])

   TECH_API_URL = "http://thetestingworldapi.com/api/technicalskills"
   fileTech = open('C://Users//Angsuman//PycharmProjects//APITesting//requestAPITect.json','r')
   json_request = json.loads(fileTech.read())
   json_request['id'] = int(id[0])
   json_request['st_id'] = id[0]
   response = requests.post(TECH_API_URL,json_request)
   
   ADDRESS_API_URL = "http://thetestingworldapi.com/api/addresses"
   fileAddress = open('C://Users//Angsuman//PycharmProjects//APITesting//RequestAddress.json','r')
   json_request = json.loads(fileAddress.read())
   response = requests.post(ADDRESS_API_URL, json_request)
   
   FINAL_URL = "http://thetestingworldapi.com/api/FinalStudentDetails/520627"
   response = requests.get(FINAL_URL)
   print(response.text)
   #json_response = json.loads(response.text)

