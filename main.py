from datetime import datetime, timedelta

def main():
    users = [{"name": "Btuto", "birthday": "1996-08-01"},
            {"name": "Paulo", "birthday": "2000-07-29"},
            {"name": "Alo", "birthday": "2008-07-31"},
            {"name": "ASd", "birthday": "2007-08-27"},
            {"name": "Folia", "birthday": "2005-07-28"},
            {"name": "Tom", "birthday": "2008-07-30"},
            {"name": "Brivki", "birthday": "2011-07-26"}]

    DICT_DAYS = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday"
    }
    Mon = []
    Tue = []
    Wed = []
    Thu = []
    Fri = []

    DICT = {
        0:Mon,
        1:Tue,
        2:Wed,
        3:Thu,
        4:Fri
    }


    c_d = datetime.now()
    # print(c_d.date())
    # print(c_d.weekday())

    count = 0
    for i in range(7):
        
        one_day = timedelta(days = count)
        for user in users:
            # print(user)
            # print(datetime.strptime(user["birthday"], '%Y-%m-%d').date())
            user_date_of_birth = datetime.strptime(user["birthday"], '%Y-%m-%d').date()
            main_date = c_d.date() + one_day
            # print(c_d.date() + one_day)
            # print("===")
            # print(user_date_of_birth.day)
            # print(main_date.day)
            if main_date.day == user_date_of_birth.day and main_date.month == user_date_of_birth.month:
                # print(main_date.weekday())
                if main_date.weekday() > 4:
                    DICT[0].append(user["name"])
                else:
                    DICT.get(main_date.weekday()).append(user["name"])
        #     print("++++++++++++")
        # print("---------------------------------")
        count+=1
    # print(Mon,Tue,Wed,Thu,Fri,sep="\n")
    for i in range(5):
        if DICT[i] != []:
            print(DICT_DAYS[i]+":",", ".join(DICT[i]))
    # print("Monday:",", ".join(Mon))
    # print("Tuesday:",", ".join(Tue))
    # print("Wednesday:",", ".join(Wed))
    # print("Thursday:",", ".join(Thu))
    # print("Friday:",", ".join(Fri))
    
if __name__ == '__main__':
    main()