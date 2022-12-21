import re
import requests
from time import sleep
import json
import os
if __name__=="__main__":
    data={
  "courses": [
    {
      "courseName": "思想道德与法治",#
      "courseCode": "MT10101",#
      "courseId": "10000014084",#
      "courseCategory": "公共基础课程",#
      "selectionArea": "主修专业课程",#
      "programType": "主修",#
      "courseNature": "必修",#
      "studyNature": "初修",#
      "classes": [
        {
          "classIds": [
            "554087"#

          ],
          "fakeClassTypeList": []
        }
      ],
      "selectedFakeClass": False
    }
  ],
  "selectionSource": "主修",#
  "reservation": False
}
    data1={
        "courses": [
            {
                "courseName": "思想道德与法治实践",  #
                "courseCode": "MT13101",  #
                "courseId": "10000014090",  #
                "courseCategory": "实践环节",  #
                "selectionArea": "主修专业课程",  #
                "programType": "主修",  #
                "courseNature": "必修",  #
                "studyNature": "初修",  #
                "classes": [
                    {
                        "classIds": [
                            #"554087"  #
                            "554839"
                        ],
                        "fakeClassTypeList": []
                    }
                ],
                "selectedFakeClass": False
            }
        ],
        "selectionSource": "主修",  #
        "reservation": False
    }
    headers = {
        "Accept": "application/json, text/plain, */*",
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57",
        "Host": "my.cqu.edu.cn",
        "Referer": "https://my.cqu.edu.cn/enroll/CourseStuSelectionList",
        "Accept - Encoding": "gzip, deflate, br",
    "Accept - Language": "zh - CN, zh;"
    "q = 0.9, en;"
    "q = 0.8, en - GB;"
    "q = 0.7, en - US;"
    "q = 0.6, zh - TW;"
    "q = 0.5",
    "Authorization": "Bearer eyJpapapapapapapapaapapappanVzZXJfbpapiwiYXV0aG9yaXRpZXMiOlsi5a2m55SfJktSX1NNUyJdLCJqdGkiOiIwYWE2NDg1MC1iNGI5LTRlZGEtOWMzMi01MzYzZWIyYjY4NmMiLCJjbGllbnRfaWQiOiJlbnJvbGwtcHJvZCIsInNjb3BlIjpbImFsbCJdfQ.XG7TEVBkAXcLgoKXXbezO8CC7kVow5LzXSUkW1UlwdQ",

    "Connection": "keep - alive",
    "Content - Type": "application / json"
    }
    url="https://my.cqu.edu.cn/api/enrollment/enrollment/student/select"
    #while 1:
     #   res = requests.post(url=url, headers=headers, json=data1)
      #  print(res)
       # sleep(0.2)
    res=requests.post(url=url,headers=headers,json=data1)
    print(res)
    #data = res.json()