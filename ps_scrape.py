# create comments explaining the code
# use the requests library to get the html from the website
import requests
from bs4 import BeautifulSoup
import datetime
import re
import json
x = datetime.datetime.now()

cookies = {
    'visid_incap_2308460': 'H60IL0EuQJus3qK3Ff7quzrlm2MAAAAAQUIPAAAAAACRzMmF8X5I+9TM/RKiZFu2',
    'visid_incap_2714889': 'W4dtPhFiRzSl+JQU2e2F5j3lm2MAAAAAQUIPAAAAAABMebxN+gFcP7ebgPwnhX90',
    'uiStateNav': 'expanded',
    'uiStateCont': 'null',
    'lastHref': 'https%3A%2F%2Fvcsnet.powerschool.com%2Fguardian%2Fscores.html%3Ffrn%3D0312280514%26fg%3DS1%26schoolid%3D1',
    'visid_incap_959634': 'cwv7pbNsR+S78Z73KNLbSSS6xGMAAAAAQUIPAAAAAAChYX/u0tj6+wPbSCbRQF/I',
    '_ga_56L8QEKYTV': 'GS1.1.1673837122.1.0.1673837124.58.0.0',
    '_ga': 'GA1.2.17602198.1673837123',
    '_ga_Y7JCS86CG7': 'GS1.1.1673837122.1.0.1673837124.0.0.0',
    '_biz_uid': 'ef8f84b91a444718f2a64f53b22b474c',
    '_biz_nA': '1',
    '_biz_pendingA': '%5B%22m%2Fipv%3F_biz_r%3Dhttps%253A%252F%252Fwww.powerschool.com%252Fpost-sitemap.xml%26_biz_h%3D-59412256%26_biz_u%3Def8f84b91a444718f2a64f53b22b474c%26_biz_s%3D8af608%26_biz_l%3Dhttps%253A%252F%252Fwww.powerschool.com%252Fblog%252F5-ways-to-improve-kindergarten-roundup-with-online-enrollment%252F%26_biz_t%3D1673837122745%26_biz_i%3D5%2520Ways%2520to%2520Improve%2520Kindergarten%2520Roundup%2520with%2520Online%2520Enrollment%2520%257C%2520PowerSchool%26_biz_n%3D0%26rnd%3D208335%22%5D',
    '_uetvid': 'd2a56000954711edbb784b044e8e937d',
    '_vwo_uuid_v2': 'DF29CF3A63078953319C18D1D841D9057|f87e2724d2c7138e48d4bab21458f86e',
    'JSESSIONID': 'E0E2800C90A9D60C2920090F4D022B6E',
    'BIGipServervcsnet_pool': '2206209452.20480.0000',
    'incap_ses_568_2308460': '1+12MC/J9gjxSqzaxfHhBzTaxmMAAAAAtIr36bnKMgbPiEi9vj4UqQ==',
    'psaid': '<-V2->173/7644983/1925338946aOgaBeG0LPZV7lIL8TRh5Aj4yHPlEfv8<-V2->',
    'currentSchool': '1',
    'nlbi_2714889': '/DbrGVHUdDReyCZmQHnVQQAAAAA42LFHwlQifwyoDalVtpXS',
    'incap_ses_568_2714889': 'D/iKMmXs2nSII7faxfHhBzzkxmMAAAAAN+g6MBeGpTwokJUlUczmCQ==',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://vcsnet.powerschool.com/guardian/scores.html?frn=0312280514&fg=S1&schoolid=1',
    'Origin': 'https://vcsnet.powerschool.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'visid_incap_2308460=H60IL0EuQJus3qK3Ff7quzrlm2MAAAAAQUIPAAAAAACRzMmF8X5I+9TM/RKiZFu2; visid_incap_2714889=W4dtPhFiRzSl+JQU2e2F5j3lm2MAAAAAQUIPAAAAAABMebxN+gFcP7ebgPwnhX90; uiStateNav=expanded; uiStateCont=null; lastHref=https%3A%2F%2Fvcsnet.powerschool.com%2Fguardian%2Fscores.html%3Ffrn%3D0312280514%26fg%3DS1%26schoolid%3D1; visid_incap_959634=cwv7pbNsR+S78Z73KNLbSSS6xGMAAAAAQUIPAAAAAAChYX/u0tj6+wPbSCbRQF/I; _ga_56L8QEKYTV=GS1.1.1673837122.1.0.1673837124.58.0.0; _ga=GA1.2.17602198.1673837123; _ga_Y7JCS86CG7=GS1.1.1673837122.1.0.1673837124.0.0.0; _biz_uid=ef8f84b91a444718f2a64f53b22b474c; _biz_nA=1; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3Dhttps%253A%252F%252Fwww.powerschool.com%252Fpost-sitemap.xml%26_biz_h%3D-59412256%26_biz_u%3Def8f84b91a444718f2a64f53b22b474c%26_biz_s%3D8af608%26_biz_l%3Dhttps%253A%252F%252Fwww.powerschool.com%252Fblog%252F5-ways-to-improve-kindergarten-roundup-with-online-enrollment%252F%26_biz_t%3D1673837122745%26_biz_i%3D5%2520Ways%2520to%2520Improve%2520Kindergarten%2520Roundup%2520with%2520Online%2520Enrollment%2520%257C%2520PowerSchool%26_biz_n%3D0%26rnd%3D208335%22%5D; _uetvid=d2a56000954711edbb784b044e8e937d; _vwo_uuid_v2=DF29CF3A63078953319C18D1D841D9057|f87e2724d2c7138e48d4bab21458f86e; JSESSIONID=E0E2800C90A9D60C2920090F4D022B6E; BIGipServervcsnet_pool=2206209452.20480.0000; incap_ses_568_2308460=1+12MC/J9gjxSqzaxfHhBzTaxmMAAAAAtIr36bnKMgbPiEi9vj4UqQ==; psaid=<-V2->173/7644983/1925338946aOgaBeG0LPZV7lIL8TRh5Aj4yHPlEfv8<-V2->; currentSchool=1; nlbi_2714889=/DbrGVHUdDReyCZmQHnVQQAAAAA42LFHwlQifwyoDalVtpXS; incap_ses_568_2714889=D/iKMmXs2nSII7faxfHhBzzkxmMAAAAAN+g6MBeGpTwokJUlUczmCQ==',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    'Content-Type': 'application/json;charset=utf-8',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}


# def all(pw, act):

# import reques
url = "https://vcsnet.powerschool.com/guardian/home.html"

student = {
    'classes': {

    }
}

global payload

session = requests.Session()

global result


def get_cgrades(sid, stuid, sem):

    json_data = {
        'section_ids': [
            sid,
        ],
        'student_ids': [
            stuid,
        ],
        'store_codes': [
            sem,
        ],
    }
    response = session.post(
        'https://vcsnet.powerschool.com/ws/xte/assignment/lookup',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    dictGrade = json.loads(response.text)
    # print(response.text)
    # print(dictGrade[2]['_assignmentsections'][0]['name'])
    grades = {}
    n = 0
    cats = []
    for i in dictGrade:
        n += 1
        cats.append([i['_assignmentsections'][0]['_assignmentcategoryassociations']
                    [0]['_teachercategory']['name']])
        grades[i['_assignmentsections'][0]
               ['_assignmentcategoryassociations'][0]['_teachercategory']['name']+"Avaliable"] = 0
        grades[i['_assignmentsections'][0]
               ['_assignmentcategoryassociations'][0]['_teachercategory']['name']+"Score"] = 0
        try:
            if (not i['_assignmentsections'][0]['_assignmentscores'][0]["isexempt"]):
                grades[n] = {
                    'name': i['_assignmentsections'][0]['name'],
                    'ddaate': i['_assignmentsections'][0]['duedate'],
                    'ingrade': not i['_assignmentsections'][0]['iscountedinfinalgrade'],
                    'score': (i['_assignmentsections'][0]['_assignmentscores'][0]["scorepoints"]),
                    'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                    'category': i['_assignmentsections'][0]['_assignmentcategoryassociations'][0]['_teachercategory']['name'],
                    'late': i['_assignmentsections'][0]['_assignmentscores'][0]["islate"],
                    'exempt': i['_assignmentsections'][0]['_assignmentscores'][0]["isexempt"],
                    'absent': i['_assignmentsections'][0]['_assignmentscores'][0]["isabsent"],
                    'missing': i['_assignmentsections'][0]['_assignmentscores'][0]["ismissing"],
                    'modified': i['_assignmentsections'][0]['_assignmentscores'][0]["scoreentrydate"],

                }
            else:
                grades[n] = {
                    'name': i['_assignmentsections'][0]['name'],
                    'ddaate': i['_assignmentsections'][0]['duedate'],
                    'ingrade': not i['_assignmentsections'][0]['iscountedinfinalgrade'],
                    'score': 'Exempt',
                    'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                    'category': i['_assignmentsections'][0]['_assignmentcategoryassociations'][0]['_teachercategory']['name'],
                    'late': i['_assignmentsections'][0]['_assignmentscores'][0]["islate"],
                    'exempt': i['_assignmentsections'][0]['_assignmentscores'][0]["isexempt"],
                    'absent': i['_assignmentsections'][0]['_assignmentscores'][0]["isabsent"],
                    'missing': i['_assignmentsections'][0]['_assignmentscores'][0]["ismissing"],
                    'modified': i['_assignmentsections'][0]['_assignmentscores'][0]["scoreentrydate"],

                }
        except:
            grades[n] = {
                'name': i['_assignmentsections'][0]['name'],
                'ddaate': i['_assignmentsections'][0]['duedate'],
                'ingrade': not i['_assignmentsections'][0]['iscountedinfinalgrade'],
                'score': 'n/e',
                'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                'category': i['_assignmentsections'][0]['_assignmentcategoryassociations'][0]['_teachercategory']['name'],
                'late': 'n/e',
                'exempt': 'n/e',
                'absent': 'n/e',
                'missing': 'n/e',
                'modified': 'n/e',

            }

            # print(i['_assignmentsections'][0]['name'] + "  "+str(i['_assignmentsections'][0]['iscountedinfinalgrade'])+" " +
            #       str(i['_assignmentsections'][0]['_assignmentscores'][0]["scorepoints"])+"/"+str(i['_assignmentsections'][0]['totalpointvalue']))
    cats = [i for n, i in enumerate(cats) if i not in cats[:n]]
    grades['categories'] = cats

    for i in grades:
        # see if i is an int
        if type(i) == int and grades[i]["score"] != "Exempt" and grades[i]["score"] != "n/e":
            tp = grades[grades[i]["category"]+"Avaliable"]+grades[i]["totalp"]
            grades[grades[i]["category"]+"Avaliable"] = tp
            tp = grades[grades[i]["category"]+"Score"]+grades[i]["score"]
            grades[grades[i]["category"]+"Score"] = tp

        # if type(i) = int
        # tp = (i["category"])  # [((i["category"]))+"Avaliable"]
    # grades[str(i["category"])+"Avaliable"] = tp
    return (grades)


def getids():
    idfound = False

    for i in student['classes']:
        if (student['classes'][i]['s1'] != "n/a"):
            uu = ("https://vcsnet.powerschool.com/guardian/" +
                  student['classes'][i]['s2link'])
            r = session.get(uu)
            s = BeautifulSoup(r.text, 'html.parser')
            for id in s.find_all('div'):

                if (id.get('data-ng-init') != None and not idfound):
                    # print(id.get('data-ng-init').split("'")[1][3:])
                    student['id'] = id.get('data-ng-init').split("'")[1][3:]
                    idfound = True

                if (id.get('data-sectionid') != None):
                    # print(id.get('data-ng-init').split("'")[1][3:])
                    student['classes'][i]['sid'] = id.get('data-sectionid')


def updateClassGrades():
    getids()
    for i in student['classes']:
        if (student['classes'][i]['s1'] != "n/a"):
            # try:
            if (student['classes'][i]['s1'] != "i"):
                student['classes'][i]['S1G'] = get_cgrades(
                    student['classes'][i]['sid'], student['id'], 'S1')

            # except:
            #     print("S1", student['classes'][i])
            #     break
            # try:
            if (student['classes'][i]['s2'] != "i"):
                student['classes'][i]['S2G'] = get_cgrades(
                    student['classes'][i]['sid'], student['id'], 'S2')


def updateGradesDict():
    r = session.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    grades = s.find_all("tr")
    for i in grades:
        linksoup = BeautifulSoup(str(i), 'html.parser')
        classLinks = []
        for link in linksoup.find_all('a'):
            classLinks.append(link.get('href'))
        period = (i.text.split())
        modperiod = period.copy()

        if (period[0][0].isdigit()):

            for i in period:
                if (i.find("Not") != -1 or i.find("avaliable") != -1 or i.find(".") != -1 or i.find("]") != -1 or i.find("[") != -1):
                    modperiod.remove(i)
                elif (i == 'available'):
                    modperiod.remove(i)
            # print(modperiod)
            rtchr = session.get(
                "https://vcsnet.powerschool.com/guardian/"+classLinks[0])
            tchr = BeautifulSoup(rtchr.text, 'html.parser')
            tchrarr = tchr.text.split("\n")
            tchrarr.pop(0)
            tchrarr.pop(0)
            tchrarr.pop(0)
            tchrarr.pop(len(tchrarr)-1)
            tchrarr.pop(len(tchrarr)-1)
            # print(tchrarr)
            modperiod += tchrarr
            sorted = re.split("Email: | Email |,| - Rm:| Name: ",
                              (' '.join(modperiod)))
            # print(sorted)
            sorted.pop(1)
            perclass = sorted[0].split(" ", 1)
            sorted.pop(0)
            sorted = perclass+sorted
            sorted.pop(2)

            # print(sorted)
            if (sorted[1] == "Open Period"):
                student['classes'][sorted[0]] = {
                    'class': sorted[1],
                    'teacher': "n/a",
                    'email': "n/a",
                    'rooom': "n/a",
                    's1': "n/a",
                    's2': "n/a",
                    'abs': "n/a",
                    'tardy': "n/a",
                    's1link': "n/a",
                    's2link': "n/a", }

            else:
                stuff = sorted[2].split(" ")
                stuff.pop(0)
                sorted = sorted+stuff
                sorted.pop(2)
                # print(stuff)
                # print(sorted)

                student['classes'][sorted[0]] = {
                    'class': sorted[1],
                    'teacher': sorted[2],
                    'email': sorted[3],
                    'rooom': sorted[4],
                    's1': sorted[5],
                    's2': sorted[6],
                    'abs': sorted[7],
                    'tardy': sorted[8],
                    's1link': classLinks[2],
                    's2link': classLinks[3], }
    updateClassGrades()


def getSchedule():
    dateurl = "https://vcsnet.powerschool.com/guardian/alerts/bellschedulealert.html?selectedDate=" + str(x.month)+"/"+str(x.day)+"/"+str(x.year) + \
        "&dayDisplay=inline&_=1673838736964"
    r = session.get(dateurl)
    datepage = BeautifulSoup(r.text, 'html.parser')
    times = (' '.join(datepage.text.strip().split('\n')).split("  "))
    # print(times)
    for i in range(4):
        times.pop(2)

    for i in times:
        print(i)


# updateGradesDict()
def aall(pw, act):
    payload = {'account': act,
               'pw': pw,
               }
    result = session.post(url, data=payload)

    updateGradesDict()
    return (student)


# Data to be written
