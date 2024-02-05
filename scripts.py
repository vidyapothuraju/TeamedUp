def sportsmen_shower(data):
    return {
        "Date of birthday" : data[0],
        "Country":data[1],
        "Instagram":data[2],
        "English skill":data[3],
        "Languages":data[4],
        'Sport':data[5],
        "Position":data[6],
        'Pay or not for sport':data[7],
        'Highlights link':data[8],
        'Hand':data[9],
        'User flag':data[10],
        'Telegram':data[11],
        'ACT':data[12],
        "Additional class":data[13],
        "Additional courses":data[14],
        #"Agree to private rule":data[15],
        "English class":data[16],
        'Height cm':data[17],
        'Height inch':data[18],
        'IELTS':data[19],
        'Live stream link':data[20],
        'Math class':data[21],
        'Natural science class':data[22],
        'SAT':data[23],
        'Scholarship':data[24],
        'Social science':data[25],
        'Stats link':data[26],
        'TOEFL':data[27],
        'University or club':data[28],
        'Weight kg':data[29],
        'Weight pound':data[30],
        'Bio_check':data[31],
        'League resolution':data[32],
        'Sport check':data[33],
        'Letter':data[34],
        'Sport org link':data[35],
        'Sport org name':data[36],
        'First name':data[37],
        'Last name':data[38],
        'National teem':data[39],
        'Experience':data[40],
        'Main achivment':data[41],
    }
'''
def sort_sport_data(id,cur):
    answer={
        # Bio
        'id': '',
        'First name': '',
        'Last name': '',
        "Date of birthday": '',
        "Email": '',
        "Country": '',
        "Instagram": '',
        'Telegram':'' ,
        #"Agree to private rule": data[16],
        # Academy
        "English skill": '',
        "Languages": '',
        'Scholarship':'' ,
        "English class": '',
        'Math class': '',
        'Natural science class': '',
        "Additional class": '',
        'Social science': '',
        'Additional courses':'',
        'SAT': '',
        'ACT': '',
        'TOEFL': '',
        'IELTS': '',
        # Sport
        'Sport': '',
        'Experience': '',
        "Position": '',
        'Sport org name': '',
        'Sport org link': '',
        'Highlights link': '',
        'Stats link': '',
        'Live stream link': '',
        'Pay or not for sport': '',
        'Hand': '',
        'Height inch': '',
        'Height cm': '',
        'Weight pound': '',
        'Weight kg': '',
        'League resolution': '',
        'University or club': '',
        'National teem': '',
        'Main achivment': '',
    }
    temp = [
        "id",
        'first_name',
        'last_name',
        'birth_date',
        'email',
        'country',
        'insta',
        'telega',
        'eng_skill',
        'languages',
        'scholarship',
        'eng_class',
        'math_class',
        'natural_science_class',
        'additional_class',
        'social_science',
        'additional_courses',
        'sat',
        'act',
        'toefl',
        'ielts',
        'sport',
        'ex',
        'position',
        'sport_org_name',
        'sport_org_link',
        'highlights_link',
        'stats_link',
        'live_stream_link',
        'pay_or_not',
        'hand',
        'height_inch',
        'height_cm',
        'weight_pound',
        'weight_kg',
        'league_resolution',
        'university_or_club',
        'national_teem',
        'main_achivment'
    ]

    keys = list(answer.keys())


    for i in range(0,len(temp)):
        try:
            print(cur.execute("SELECT * FROM TeamedUp_profile"))
            print(cur.fetchall())
            print(cur.execute("SELECT ? FROM TeamedUp_profile WHERE id = ?", (i,id, )).fetchall())
            answer[keys[i]]=cur.execute("SELECT ? FROM TeamedUp_profile WHERE id = ?", (temp[i],id, )).fetchone()
        except:
            pass
    return answer
'''

def sort_sport_data(data):
    print(data)
    return {
        # Bio
        'First name': data[3],
        'Last name': data[4],
        "Date of birthday": data[5],
        "Email": data[6],
        "Country": data[7],
        "Instagram": data[8],
        'Telegram': data[9],
        #"Agree to private rule": data[16],
        # Academy
        "English skill": data[12],
        "Languages": data[13],
        'Scholarship': data[14 ],
        "English class": data[15],
        'Math class': data[16],
        'Natural science class': data[17],
        "Additional class": data[18],
        'Social science': data[19],
        'Additional courses':data[20],
        'SAT': data[21],
        'ACT': data[22],
        'TOEFL': data[23],
        'IELTS': data[24],
        # Sport
        'Sport': data[25],
        'Experience': data[26],
        "Position": data[27],
        'Sport org name': data[28],
        'Sport org link': data[29],
        'Highlights link': data[30],
        'Stats link': data[31],
        'Live stream link': data[32],
        'Pay or not for sport': data[33],
        'Hand': data[34],
        'Height inch': data[35],
        'Height cm': data[36],
        'Weight pound': data[37],
        'Weight kg': data[38],
        'League resolution': data[39],
        'University or club': data[40],
        'National teem': data[41],
        'Main achivment': data[42],
    }


def string_maker(data):
    temp = list(data.keys())
    s=''
    for i in temp:
        if i=='First name':
            s+="<b>Bio</b>\n\n"
        if i == "English skill":
            s+='\n<b>Academy</b>\n\n'
        if i == "Sport":
            s+= "\n<b>Sport</b>\n\n"
        s+=i+" : "+str(data[i])+'\n'
    return s
