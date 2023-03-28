# create comments explaining the code
# use the requests library to get the html from the website
import requests
from bs4 import BeautifulSoup
import datetime
import traceback
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
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0',
    # 'Accept': 'application/json, text/plain, */*',
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
def represents_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

url = "https://vcsnet.powerschool.com/guardian/home.html"

student = {
    'classes': {
        's1': {},
        's2': {},
    }
}
c2 = {}
# global payload

# global session
# session = requests.Session()
# global result


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
    z = 0
    cats = []
    for i in dictGrade.copy():
        z += 1
        n = str(z)
        cc = i['_assignmentsections'][0]['_assignmentcategoryassociations'][0]['_teachercategory']['name']
        if (cc == ("Master Assessment")):
            cc = "Mastery Assessments"

        cats.append(cc)
        grades[cc+"Avaliable"] = 0
        grades[cc+"Score"] = 0

        try:
            if (not i['_assignmentsections'][0]['_assignmentscores'][0]["isexempt"]):
                grades[n] = {
                    'name': i['_assignmentsections'][0]['name'],
                    'ddaate': i['_assignmentsections'][0]['duedate'],
                    'ingrade':  i['_assignmentsections'][0]['iscountedinfinalgrade'],
                    'score': (i['_assignmentsections'][0]['_assignmentscores'][0]["scorepoints"]),
                    'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                    'category': cc,
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
                    'ingrade':  i['_assignmentsections'][0]['iscountedinfinalgrade'],
                    'score': 'Exempt',
                    'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                    'category': cc,
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
                'ingrade': i['_assignmentsections'][0]['iscountedinfinalgrade'],
                'score': 'n/e',
                'totalp': i['_assignmentsections'][0]['totalpointvalue'],
                'category': cc,
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

    for i in grades.copy():
        # see if i is an int
        if i.isnumeric() and grades[i]["score"] != "Exempt" and grades[i]["score"] != "n/e" and grades[i]["ingrade"] == True:
            # if (grades[i]["category"].find("/")):
            #     cat = str(grades[i]["category"]).replace("/", ",")
            # else:
            cat = grades[i]["category"]
            tp = grades[cat+"Avaliable"]+grades[i]["totalp"]
            grades[cat+"Avaliable"] = tp
            tp = grades[cat+"Score"]+grades[i]["score"]
            grades[cat+"Score"] = tp
        # for i in grades:cd powe
    #     if str(i)!=i
        # if type(i) = int
        # tp = (i["category"])  # [((i["category"]))+"Avaliable"]
    # grades[str(i["category"])+"Avaliable"] = tp
    return (grades)


def getids():
    idfound = False

    for i in student['classes']['s1'].copy():
        if (student['classes']['s1'][i]['abs'] != "n/a"):
            uu = ("https://vcsnet.powerschool.com/guardian/" +
                  student['classes']['s1'][i]['glink'])
            r = session.get(uu)
            s = BeautifulSoup(r.text, 'html.parser')
            for id in s.find_all('div'):

                if (id.get('data-ng-init') != None and not idfound):
                    # print(id.get('data-ng-init').split("'")[1][3:])
                    student['id'] = id.get('data-ng-init').split("'")[1][3:]
                    idfound = True

                if (id.get('data-sectionid') != None):
                    # print(id.get('data-ng-init').split("'")[1][3:])
                    student['classes']['s1'][i]['sid'] = id.get(
                        'data-sectionid')
                    student['classes']['s1'][i]['GrList'] = get_cgrades(
                        student['classes']['s1'][i]['sid'], student['id'], 'S1')
                    break
    for i in student['classes']['s2'].copy():
        if (student['classes']['s2'][i]['abs'] != "n/a"):
            uu = ("https://vcsnet.powerschool.com/guardian/" +
                  student['classes']['s2'][i]['glink'])
            r = session.get(uu)
            s = BeautifulSoup(r.text, 'html.parser')
            for id in s.find_all('div'):

                if (id.get('data-sectionid') != None):
                    # print(id.get('data-ng-init').split("'")[1][3:])
                    student['classes']['s2'][i]['sid'] = id.get(
                        'data-sectionid')
                    student['classes']['s2'][i]['GrList'] = get_cgrades(
                        student['classes']['s2'][i]['sid'], student['id'], 'S2')
                    break


def updateClassGrades():
    for i in student['classes']['s1'].copy():
        if (student['classes']['s1'][i]['abs'] != "n/a"):
            try:
                # if (student['classes']['s1'][i]['grade'] != "[ i ]"):
                student['classes']['s1'][i]['GrList'] = get_cgrades(
                    student['classes']['s1'][i]['sid'], student['id'], 'S1')
            except:
                traceback.print_exc()
                # with open("grades.json", "w") as outfile:
                #     json.dump(student, outfile)
                # print(i)
                return
    for i in student['classes']['s2']:
        if (student['classes']['s2'][i]['abs'] != "n/a"):
            try:
                if (student['classes']['s2'][i]['grade'] != "[ i ]"):
                    student['classes']['s2'][i]['GrList'] = get_cgrades(
                        student['classes']['s2'][i]['sid'], student['id'], 'S2')
            except:
                traceback.print_exc()
                # with open("grades.json", "w") as outfile:
                #     json.dump(student, outfile)
                # print(i)

                return


def upClass():
    r = session.get(url)
    s = BeautifulSoup(r.text, 'html.parser')
    grades = s.find_all("tr")
    # print(grades)
    for z in grades:
        linksoup = BeautifulSoup(str(z), 'html.parser')
        classLinks = []
        for link in linksoup.find_all('a'):
            classLinks.append(link.get('href'))

        period = (z.text.split())

        # if (period[0][0].isdigit()):
        if (period[0][0].isdigit()):

            dd = ((z.find_all("td")))
            xy = []
            for y in dd:
                # print(y.text.strip()+"\"")
                xy += (y.text.strip().split("\xa0"))

            rem = ["", " ", ".", "-", "Not available", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "Email",'\xa0']

            res = [i for i in xy if i not in rem]
            rtchr = session.get(
                "https://vcsnet.powerschool.com/guardian/"+classLinks[0])
            # print(rtchr)
            if (rtchr.status_code != 200):
                classLinks.pop(0)
                rtchr = session.get(
                    "https://vcsnet.powerschool.com/guardian/"+classLinks[0])
            tchr = BeautifulSoup(rtchr.text, 'html.parser')
            tchrarr = tchr.text.split("\n")
            tchrarr = [i for i in tchrarr if i not in rem]

            # print(tchrarr,)
            # res += tchrarr
         
            #         # res.append(i[6:])
            # res.append(tchrarr[0][6:])
            # res.append(tchrarr[1][7:])
            res+=tchrarr
            res += classLinks


            res2=[]
            res2+=res
            res=[]
            resrem=["begdate","mailto","teacherinfo","attendancedates"]
       
            for elem in res2:
                contains_substring = False
                for substring in resrem:
                    if substring in elem:
                        contains_substring = True
                        break
                if not contains_substring:
                    res.append(elem)    
            if(not represents_int(res[6])):
               res.pop(6)       
            if (c2.__contains__(period[0][0:4]+" S")):
                c2[period[0][0:4]+" S1"] = c2[period[0][0:4]+" S"]
                c2.pop(period[0][0:4]+" S")
                c2[period[0][0:4]+" S2"] = res
            else:
                c2[period[0][0:4]+" S"] = res
        # else:
        #     print(period);


def classDict():
    # print
    for i in c2.copy():
        # print(i)
        c = i.split(" ")
        # print(c)
        if (c[1] == "S"):
            if (c2[i][1] == "Open Period"):
                student['classes']['s1'][i] = {
                    'class': c2[i][1],
                    'teacher': "n/a",
                    'email': "n/a",
                    'rooom': "n/a",
                    'grade': "n/a",
                    'abs': "n/a",
                    'tardy': "n/a",
                    'glink': "n/a",
                }
                student['classes']['s2'][i] = {
                    'class': c2[i][1],
                    'teacher': "n/a",
                    'email': "n/a",
                    'rooom': "n/a",
                    'grade': "n/a",
                    'abs': "n/a",
                    'tardy': "n/a",
                    'glink': "n/a",
                }
            else:
                student['classes']['s1'][i] = {
                    'class': c2[i][1],
                    'teacher': c2[i][8],
                    'email': c2[i][9],
                    'rooom': c2[i][3],
                    'grade': c2[i][4],
                    'abs': c2[i][6],
                    'tardy': c2[i][7],
                    'glink': c2[i][10],
                }
                student['classes']['s2'][i] = {
                    'class': c2[i][1],
                    'teacher': c2[i][8],
                    'email': c2[i][9],
                    'rooom': c2[i][3],
                    'grade': c2[i][5],
                    'abs': c2[i][6],
                    'tardy': c2[i][7],
                    'glink': c2[i][11],
                }
        elif (c[1] == "S1"):
            student['classes']['s1'][i] = {
                'class': c2[i][1],
                'teacher': c2[i][7],
                'email': c2[i][8],
                'rooom': c2[i][3],
                'grade': c2[i][4],
                'abs': c2[i][5],
                'tardy': c2[i][6],
                'glink': c2[i][9],

            }
        elif (c[1] == "S2"):
            student['classes']['s2'][i] = {
                'class': c2[i][1],
                'teacher': c2[i][8],
                'email': c2[i][9],
                'rooom': c2[i][3],
                'grade': c2[i][4],
                'abs': c2[i][1],
                'tardy': c2[i][6],
                'glink': c2[i][10],
            }


def clr():
    # for i in student['classes']:
    student.clear()
    student['classes'] = {
        's1': {},
        's2': {},

    }
    c2.clear()


def getSchedule(pw, act):
    clr()
    payload = {'account': act,
               'pw': pw,
               }

    global session
    session = requests.Session()
    print(session)
    # session.cookies.clear()
    session.post(url, data=payload)
    dateurl = "https://vcsnet.powerschool.com/guardian/alerts/bellschedulealert.html?selectedDate=" + str(x.month)+"/"+str(x.day)+"/"+str(x.year) + \
        "&dayDisplay=inline&_=1673838736964"
    r = session.get(dateurl)
    datepage = BeautifulSoup(r.text, 'html.parser')
    times = (' '.join(datepage.text.strip().split('\n')).split("  "))
    # print(times)
    for i in range(4):
        times.pop(2)
    if (len(times) > 10):
        return "I"
    return times


def aall(pw, act):
    clr()
    payload = {'account': act,
               'pw': pw,
               }

    global session
    session = requests.Session()
    print(session)
    # session.cookies.clear()
    session.post(url, data=payload)

    upClass()
    # # print("\n".join(c2))
    classDict()
    getids()
    # updateClassGrades()
    # # pprint.pprint(student)
    # with open("grades.json", "w") as outfile:
    #     json.dump(student, outfile)
    return ((student))


# Data to be written