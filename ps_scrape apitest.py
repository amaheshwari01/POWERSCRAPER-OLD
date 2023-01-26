
import requests
import pprint
import json

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


json_data = {
    'section_ids': [
        48666,
    ],
    'student_ids': [
        19068,
    ],
    'store_codes': [
        'S2',
    ],
}
payload = {'account': 'act',
           'pw': 'pw',
           }

session = requests.Session()
url = "https://vcsnet.powerschool.com/guardian/home.html"

result = session.post(url, data=payload)


# # def get_cgrades(sid, stuid, sem):
response = session.post(
    'https://vcsnet.powerschool.com/ws/xte/assignment/lookup',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
# dictGrade = json.loads(response.text)
# print(response.text)


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

        grades[n] = {
            'name': i['_assignmentsections'][0]['name'],
            'ddaate': i['_assignmentsections'][0]['duedate'],
            'ingrade': not i['_assignmentsections'][0]['iscountedinfinalgrade'],
            'score': i['_assignmentsections'][0]['_assignmentscores'][0]["scorepoints"],
            'totalp': i['_assignmentsections'][0]['totalpointvalue'],
            'category': i['_assignmentsections'][0]['_assignmentcategoryassociations'][0]['_teachercategory']['name'],
            'late': i['_assignmentsections'][0]['_assignmentscores'][0]["islate"],
            'exempt': i['_assignmentsections'][0]['_assignmentscores'][0]["isexempt"],
            'absent': i['_assignmentsections'][0]['_assignmentscores'][0]["isabsent"],
            'missing': i['_assignmentsections'][0]['_assignmentscores'][0]["ismissing"],
            'modified': i['_assignmentsections'][0]['_assignmentscores'][0]["scoreentrydate"],

        }

        # print(i['_assignmentsections'][0]['name'] + "  "+str(i['_assignmentsections'][0]['iscountedinfinalgrade'])+" " +
        #       str(i['_assignmentsections'][0]['_assignmentscores'][0]["scorepoints"])+"/"+str(i['_assignmentsections'][0]['totalpointvalue']))
    cats = [i for n, i in enumerate(cats) if i not in cats[:n]]
    grades['categories'] = cats

    for i in grades:
        # see if i is an int
        if type(i) == int:
            tp = grades[grades[i]["category"]+"Avaliable"]+grades[i]["totalp"]
            grades[grades[i]["category"]+"Avaliable"] = tp
            tp = grades[grades[i]["category"]+"Score"]+grades[i]["score"]
            grades[grades[i]["category"]+"Score"] = tp

        # if type(i) = int
        # tp = (i["category"])  # [((i["category"]))+"Avaliable"]
    # grades[str(i["category"])+"Avaliable"] = tp
    return (grades)


# pprint.pprint(get_cgrades(48666, 19068, 'S2'))
