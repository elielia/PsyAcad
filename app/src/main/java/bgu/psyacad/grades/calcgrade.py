
    def float(num):
    return num

    def scale(num):
        return num

    def form_valid(simulationNum, english_answers,quantitative_answers,verbal_answers):
        #simulation = form.save(commit=False)
        #simulation.date = timezone.now()
        #simulation.author = request.user
        #simulation.english_answers = simulation.english_grade
        #simulation.quantitative_answers = simulation.quantitative_grade
        #simulation.verbal_answers = simulation.verbal_grade


        # check if Simulation is before change, for manipulating the table
        if simulationNum < 19:
            if simulationNum == 18:
                quantitative_grade = scale(float(quantitative_answers) / 40 * 50)
                english_grade = scale(float(english_answers) / 48 * 58)
                verbal_grade = scale(float(verbal_answers) / 46 * 60)
            elif simulationNum == 14 or simulationNum == 13:
                quantitative_grade = scale(float(quantitative_answers)/40*50)
                english_grade = scale(float(english_answers)/44*58)
                verbal_grade = scale(float(verbal_answers)/46*60)
            elif simulationNum == 12:
                quantitative_grade = scale(float(quantitative_answers) / 40 * 50)
                english_grade = scale(float(english_answers) / 44 * 54)
                verbal_grade = scale(float(verbal_answers) / 45 * 60)
            elif simulationNum == 7:
                quantitative_grade = scale(float(quantitative_answers) / 40 * 49)
                english_grade = scale(float(english_answers) / 44 * 54)
                verbal_grade = scale(float(verbal_answers) / 46 * 60)
            else:
                quantitative_grade = scale(float(quantitative_answers) / 40 * 50)
                english_grade = scale(float(english_answers) / 44 * 54)
                verbal_grade = scale(float(verbal_answers) / 46 * 60)

        # get the correct table for this simulation.
        #t = Grades_table(number=simulation.num)
        #t.table = []
        #t.setSim()
        t = setSim(simulationNum)
       
        # calc grade calculate and update all grades.
        # calculate grades according to the table.
        grade = calc_grade(t,english_answers,quantitative_answers,verbal_answers,quantitative_grade,english_grade,verbal_grade)
        return grade

        ##simulation.save()
        ##return redirect(simulation)

    def essay_grade(language_grade, content_grade):
        if language_grade+content_grade == 2:
            return 50
        elif language_grade+content_grade == 3:
            return 55.20
        elif language_grade+content_grade == 4:
            return 64.40
        elif language_grade+content_grade == 5:
            return 73.60
        elif language_grade+content_grade == 6:
            return 84.20
        elif language_grade+content_grade == 7:
            return 95.00
        elif language_grade+content_grade == 8:
            return 105.80
        elif language_grade+content_grade == 9:
            return 116.40
        elif language_grade+content_grade == 10:
            return 127.40
        elif language_grade+content_grade == 11:
            return 137.80
        elif language_grade+content_grade == 12:
            return 150

    def calc_grade(table,english_answers,quantitative_answers,verbal_answers,quantitative_grade,english_grade,verbal_grade,language_grade,content_grade):
        index = 0
        e = 0
        q = 0
        v = 0

        #exampt = False

        for i in table:
            if index == english_grade:
                e = i[0]
                if e >= 134:
                    exampt = True
                else:
                    exampt = False
            if index == quantitative_grade:
                q = i[1]
            if index == verbal_grade:
                v = i[2]
            index += 1

        english_grade = e
        quantitative_grade = q
        if language_grade + content_grade < 2:
            verbal_grade = v;
        else:
            verbal_grade = scale((v * 0.75) + (essay_grade() * 0.25))

        # finalize grade methods, before matching last table.
        general_grade = (english_grade+(2*quantitative_grade)+(2*verbal_grade)) / 5.0
        if general_grade < 144:
            general_grade = scale((general_grade * 5.66-65.3))
        else:
            general_grade = scale((general_grade * 8.5-475)+0.5)
        v_grade = (english_grade + quantitative_grade + (3 * verbal_grade)) / 5.0
        if v_grade < 144:
            v_grade = scale((v_grade * 5.66 - 65.3))
        else:
            v_grade = scale((v_grade * 8.5 - 475) + 0.5)
        q_grade = (english_grade + (3*quantitative_grade) + verbal_grade) / 5.0
        if q_grade < 144:
            q_grade = scale((q_grade * 5.66 - 65.3))
        else:
            q_grade = scale((q_grade * 8.5 - 475) + 0.5)
        return

    def setSim(number):

        t = []
        # simulation 6 set table - 12/2009
        if number == 6:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([56, 56, 55])
            # 6
            t.append([58, 58, 56])
            # 7
            t.append([60, 59, 57])
            # 8
            t.append([62, 60, 58])
            # 9
            t.append([64, 62, 59])
            # 10
            t.append([66, 63, 60])
            # 11
            t.append([68, 65, 61])
            # 12
            t.append([70, 67, 62])
            # 13
            t.append([71, 68, 63])
            # 14
            t.append([73, 70, 64])
            # 15
            t.append([75, 72, 66])
            # 16
            t.append([77, 74, 67])
            # 17
            t.append([79, 76, 68])
            # 18
            t.append([80, 77, 70])
            # 19
            t.append([82, 79, 71])
            # 20
            t.append([84, 81, 72])
            # 21
            t.append([86, 83, 74])
            # 22
            t.append([88, 85, 76])
            # 23
            t.append([89, 88, 77])
            # 24
            t.append([91, 90, 79])
            # 25
            t.append([93, 92, 81])
            # 26
            t.append([95, 94, 83])
            # 27
            t.append([97, 96, 85])
            # 28
            t.append([98, 98, 87])
            # 29
            t.append([100, 100, 89])
            # 30
            t.append([102, 102, 91])
            # 31
            t.append([104, 104, 93])
            # 32
            t.append([106, 106, 95])
            # 33
            t.append([107, 109, 96])
            # 34
            t.append([109, 111, 98])
            # 35
            t.append([111, 113, 100])
            # 36
            t.append([113, 115, 102])
            # 37
            t.append([115, 117, 104])
            # 38
            t.append([116, 119, 106])
            # 39
            t.append([118, 121, 107])
            # 40
            t.append([120, 123, 109])
            # 41
            t.append([122, 125, 111])
            # 42
            t.append([124, 127, 113])
            # 43
            t.append([125, 129, 115])
            # 44
            t.append([127, 131, 116])
            # 45
            t.append([129, 133, 118])
            # 46
            t.append([131, 136, 120])
            # 47
            t.append([133, 139, 122])
            # 48
            t.append([135, 142, 123])
            # 49
            t.append([137, 146, 125])
            # 50
            t.append([139, 150, 127])
            # 51
            t.append([141, None, 129])
            # 52
            t.append([144, None, 131])
            # 53
            t.append([147, None, 132])
            # 54
            t.append([150, None, 134])
            # 55
            t.append([None, None, 136])
            # 56
            t.append([None, None, 138])
            # 57
            t.append([None, None, 141])
            # 58
            t.append([None, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 7 set table - 02/2010
        if number == 7:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([56, 57, 55])
            # 6
            t.append([58, 59, 56])
            # 7
            t.append([60, 61, 57])
            # 8
            t.append([62, 62, 58])
            # 9
            t.append([64, 64, 59])
            # 10
            t.append([66, 66, 60])
            # 11
            t.append([68, 68, 61])
            # 12
            t.append([70, 70, 62])
            # 13
            t.append([71, 72, 63])
            # 14
            t.append([73, 74, 64])
            # 15
            t.append([75, 76, 65])
            # 16
            t.append([77, 78, 66])
            # 17
            t.append([79, 80, 67])
            # 18
            t.append([80, 83, 69])
            # 19
            t.append([82, 85, 70])
            # 20
            t.append([84, 87, 71])
            # 21
            t.append([86, 89, 73])
            # 22
            t.append([88, 91, 75])
            # 23
            t.append([89, 94, 76])
            # 24
            t.append([91, 96, 78])
            # 25
            t.append([93, 98, 80])
            # 26
            t.append([95, 100, 82])
            # 27
            t.append([97, 102, 84])
            # 28
            t.append([98, 104, 85])
            # 29
            t.append([100, 106, 87])
            # 30
            t.append([102, 108, 89])
            # 31
            t.append([104, 110, 91])
            # 32
            t.append([106, 112, 93])
            # 33
            t.append([107, 115, 94])
            # 34
            t.append([109, 117, 96])
            # 35
            t.append([111, 119, 98])
            # 36
            t.append([113, 121, 100])
            # 37
            t.append([115, 123, 102])
            # 38
            t.append([116, 126, 103])
            # 39
            t.append([118, 128, 105])
            # 40
            t.append([120, 130, 107])
            # 41
            t.append([122, 132, 109])
            # 42
            t.append([124, 134, 111])
            # 43
            t.append([125, 137, 112])
            # 44
            t.append([127, 139, 114])
            # 45
            t.append([129, 141, 116])
            # 46
            t.append([131, 143, 118])
            # 47
            t.append([133, 146, 120])
            # 48
            t.append([135, 148, 121])
            # 49
            t.append([137, 150, 123])
            # 50
            t.append([139, None, 125])
            # 51
            t.append([141, None, 127])
            # 52
            t.append([144, None, 129])
            # 53
            t.append([147, None, 131])
            # 54
            t.append([150, None, 133])
            # 55
            t.append([None, None, 135])
            # 56
            t.append([None, None, 138])
            # 57
            t.append([None, None, 141])
            # 58
            t.append([None, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 8 set table - 04/2010
        if number == 8:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([55, 57, 55])
            # 6
            t.append([57, 59, 56])
            # 7
            t.append([58, 61, 57])
            # 8
            t.append([59, 62, 58])
            # 9
            t.append([60, 64, 59])
            # 10
            t.append([61, 66, 60])
            # 11
            t.append([62, 68, 61])
            # 12
            t.append([63, 70, 62])
            # 13
            t.append([65, 72, 64])
            # 14
            t.append([66, 74, 65])
            # 15
            t.append([67, 76, 66])
            # 16
            t.append([69, 78, 68])
            # 17
            t.append([71, 80, 69])
            # 18
            t.append([73, 82, 71])
            # 19
            t.append([75, 84, 72])
            # 20
            t.append([77, 86, 74])
            # 21
            t.append([79, 88, 76])
            # 22
            t.append([81, 90, 78])
            # 23
            t.append([83, 92, 79])
            # 24
            t.append([85, 94, 81])
            # 25
            t.append([87, 96, 83])
            # 26
            t.append([89, 98, 85])
            # 27
            t.append([91, 100, 87])
            # 28
            t.append([93, 103, 88])
            # 29
            t.append([95, 105, 90])
            # 30
            t.append([97, 107, 92])
            # 31
            t.append([99, 109, 94])
            # 32
            t.append([101, 111, 96])
            # 33
            t.append([103, 113, 97])
            # 34
            t.append([105, 115, 99])
            # 35
            t.append([107, 117, 101])
            # 36
            t.append([109, 119, 103])
            # 37
            t.append([111, 121, 105])
            # 38
            t.append([113, 124, 106])
            # 39
            t.append([115, 126, 108])
            # 40
            t.append([117, 128, 110])
            # 41
            t.append([119, 130, 112])
            # 42
            t.append([121, 132, 114])
            # 43
            t.append([124, 135, 115])
            # 44
            t.append([126, 137, 117])
            # 45
            t.append([128, 139, 119])
            # 46
            t.append([130, 141, 121])
            # 47
            t.append([132, 143, 123])
            # 48
            t.append([134, 145, 124])
            # 49
            t.append([136, 147, 126])
            # 50
            t.append([138, 150, 128])
            # 51
            t.append([141, None, 130])
            # 52
            t.append([144, None, 132])
            # 53
            t.append([147, None, 134])
            # 54
            t.append([150, None, 136])
            # 55
            t.append([None, None, 138])
            # 56
            t.append([None, None, 140])
            # 57
            t.append([None, None, 142])
            # 58
            t.append([None, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 9 set table - 07/2010
        if number == 9:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([55, 54, 54])
            # 5
            t.append([56, 55, 55])
            # 6
            t.append([58, 57, 56])
            # 7
            t.append([59, 58, 57])
            # 8
            t.append([61, 60, 58])
            # 9
            t.append([63, 61, 59])
            # 10
            t.append([64, 63, 60])
            # 11
            t.append([66, 65, 61])
            # 12
            t.append([67, 67, 62])
            # 13
            t.append([60, 68, 63])
            # 14
            t.append([70, 70, 64])
            # 15
            t.append([72, 72, 65])
            # 16
            t.append([74, 74, 66])
            # 17
            t.append([76, 76, 67])
            # 18
            t.append([77, 79, 68])
            # 19
            t.append([79, 81, 69])
            # 20
            t.append([81, 83, 70])
            # 21
            t.append([83, 85, 72])
            # 22
            t.append([85, 87, 74])
            # 23
            t.append([87, 90, 75])
            # 24
            t.append([89, 92, 77])
            # 25
            t.append([91, 94, 79])
            # 26
            t.append([93, 96, 81])
            # 27
            t.append([95, 98, 83])
            # 28
            t.append([96, 101, 85])
            # 29
            t.append([98, 103, 87])
            # 30
            t.append([100, 105, 89])
            # 31
            t.append([101, 107, 91])
            # 32
            t.append([103, 109, 93])
            # 33
            t.append([105, 112, 95])
            # 34
            t.append([107, 114, 97])
            # 35
            t.append([108, 116, 99])
            # 36
            t.append([110, 118, 101])
            # 37
            t.append([112, 120, 103])
            # 38
            t.append([114, 123, 104])
            # 39
            t.append([116, 125, 106])
            # 40
            t.append([118, 127, 108])
            # 41
            t.append([120, 129, 110])
            # 42
            t.append([122, 131, 112])
            # 43
            t.append([123, 134, 114])
            # 44
            t.append([125, 136, 116])
            # 45
            t.append([127, 138, 118])
            # 46
            t.append([129, 140, 120])
            # 47
            t.append([131, 142, 122])
            # 48
            t.append([132, 144, 124])
            # 49
            t.append([134, 147, 126])
            # 50
            t.append([136, 150, 128])
            # 51
            t.append([139, None, 130])
            # 52
            t.append([142, None, 132])
            # 53
            t.append([146, None, 134])
            # 54
            t.append([150, None, 136])
            # 55
            t.append([None, None, 138])
            # 56
            t.append([None, None, 140])
            # 57
            t.append([None, None, 142])
            # 58
            t.append([None, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 10 set table - 10/2010
        if number == 10:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([55, 57, 55])
            # 6
            t.append([57, 59, 56])
            # 7
            t.append([59, 61, 57])
            # 8
            t.append([61, 63, 58])
            # 9
            t.append([63, 65, 59])
            # 10
            t.append([65, 67, 60])
            # 11
            t.append([67, 68, 61])
            # 12
            t.append([69, 71, 62])
            # 13
            t.append([70, 72, 64])
            # 14
            t.append([72, 74, 65])
            # 15
            t.append([74, 76, 66])
            # 16
            t.append([76, 78, 68])
            # 17
            t.append([77, 80, 69])
            # 18
            t.append([79, 82, 71])
            # 19
            t.append([80, 84, 72])
            # 20
            t.append([82, 86, 74])
            # 21
            t.append([84, 88, 76])
            # 22
            t.append([85, 90, 78])
            # 23
            t.append([87, 92, 79])
            # 24
            t.append([88, 94, 81])
            # 25
            t.append([90, 96, 83])
            # 26
            t.append([92, 98, 85])
            # 27
            t.append([94, 100, 87])
            # 28
            t.append([95, 102, 88])
            # 29
            t.append([97, 104, 90])
            # 30
            t.append([99, 106, 92])
            # 31
            t.append([101, 108, 94])
            # 32
            t.append([102, 110, 96])
            # 33
            t.append([104, 112, 97])
            # 34
            t.append([105, 114, 99])
            # 35
            t.append([107, 116, 101])
            # 36
            t.append([109, 118, 103])
            # 37
            t.append([111, 120, 105])
            # 38
            t.append([112, 122, 106])
            # 39
            t.append([114, 124, 108])
            # 40
            t.append([116, 126, 110])
            # 41
            t.append([118, 128, 112])
            # 42
            t.append([119, 130, 113])
            # 43
            t.append([121, 132, 115])
            # 44
            t.append([122, 134, 116])
            # 45
            t.append([124, 136, 118])
            # 46
            t.append([126, 138, 120])
            # 47
            t.append([128, 141, 122])
            # 48
            t.append([130, 144, 123])
            # 49
            t.append([132, 147, 125])
            # 50
            t.append([134, 150, 127])
            # 51
            t.append([138, None, 129])
            # 52
            t.append([142, None, 131])
            # 53
            t.append([146, None, 132])
            # 54
            t.append([150, None, 134])
            # 55
            t.append([None, None, 136])
            # 56
            t.append([None, None, 138])
            # 57
            t.append([None, None, 141])
            # 58
            t.append([None, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 11 set table - 12/2010
        elif number == 11:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 54, 54])
            # 5
            t.append([55, 55, 55])
            # 6
            t.append([57, 57, 56])
            # 7
            t.append([59, 59, 57])
            # 8
            t.append([61, 61, 58])
            # 9
            t.append([63, 63, 59])
            # 10
            t.append([65, 65, 60])
            # 11
            t.append([67, 67, 61])
            # 12
            t.append([69, 68, 62])
            # 13
            t.append([70, 70, 63])
            # 14
            t.append([72, 71, 64])
            # 15
            t.append([74, 73, 65])
            # 16
            t.append([76, 75, 67])
            # 17
            t.append([78, 77, 68])
            # 18
            t.append([79, 78, 70])
            # 19
            t.append([81, 80, 71])
            # 20
            t.append([83, 82, 73])
            # 21
            t.append([85, 84, 75])
            # 22
            t.append([87, 86, 77])
            # 23
            t.append([88, 89, 79])
            # 24
            t.append([90, 91, 81])
            # 25
            t.append([92, 93, 83])
            # 26
            t.append([94, 95, 85])
            # 27
            t.append([96, 97, 87])
            # 28
            t.append([97, 99, 88])
            # 29
            t.append([99, 101, 90])
            # 30
            t.append([101, 103, 92])
            # 31
            t.append([103, 105, 94])
            # 32
            t.append([105, 107, 96])
            # 33
            t.append([107, 109, 97])
            # 34
            t.append([109, 111, 99])
            # 35
            t.append([111, 113, 101])
            # 36
            t.append([113, 115, 103])
            # 37
            t.append([114, 117, 105])
            # 38
            t.append([116, 120, 107])
            # 39
            t.append([117, 122, 109])
            # 40
            t.append([119, 124, 111])
            # 41
            t.append([121, 126, 113])
            # 42
            t.append([123, 128, 115])
            # 43
            t.append([125, 130, 116])
            # 44
            t.append([127, 132, 118])
            # 45
            t.append([129, 134, 120])
            # 46
            t.append([131, 137, 122])
            # 47
            t.append([133, 140, 124])
            # 48
            t.append([135, 143, 126])
            # 49
            t.append([137, 146, 128])
            # 50
            t.append([139, 150, 130])
            # 51
            t.append([141, None, 132])
            # 52
            t.append([144, None, 134])
            # 53
            t.append([147, None, 135])
            # 54
            t.append([150, None, 137])
            # 55
            t.append([None, None, 139])
            # 56
            t.append([None, None, 141])
            # 57
            t.append([None, None, 143])
            # 58
            t.append([None, None, 145])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 12 set table - 02/2011
        elif number == 12:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 54, 54])
            # 5
            t.append([56, 55, 55])
            # 6
            t.append([58, 57, 56])
            # 7
            t.append([60, 59, 57])
            # 8
            t.append([62, 61, 58])
            # 9
            t.append([64, 63, 59])
            # 10
            t.append([66, 65, 60])
            # 11
            t.append([68, 67, 61])
            # 12
            t.append([70, 68, 62])
            # 13
            t.append([72, 70, 63])
            # 14
            t.append([74, 71, 64])
            # 15
            t.append([76, 73, 65])
            # 16
            t.append([78, 75, 66])
            # 17
            t.append([80, 77, 67])
            # 18
            t.append([81, 79, 69])
            # 19
            t.append([83, 80, 70])
            # 20
            t.append([85, 83, 71])
            # 21
            t.append([87, 85, 73])
            # 22
            t.append([89, 87, 75])
            # 23
            t.append([90, 90, 76])
            # 24
            t.append([92, 92, 78])
            # 25
            t.append([94, 94, 80])
            # 26
            t.append([96, 96, 82])
            # 27
            t.append([98, 98, 84])
            # 28
            t.append([100, 101, 87])
            # 29
            t.append([102, 103, 89])
            # 30
            t.append([104, 105, 91])
            # 31
            t.append([106, 107, 93])
            # 32
            t.append([108, 109, 95])
            # 33
            t.append([109, 112, 97])
            # 34
            t.append([111, 114, 99])
            # 35
            t.append([113, 116, 101])
            # 36
            t.append([115, 118, 103])
            # 37
            t.append([117, 120, 105])
            # 38
            t.append([118, 123, 108])
            # 39
            t.append([120, 125, 110])
            # 40
            t.append([122, 127, 112])
            # 41
            t.append([124, 129, 114])
            # 42
            t.append([126, 131, 116])
            # 43
            t.append([128, 134, 118])
            # 44
            t.append([130, 136, 120])
            # 45
            t.append([132, 138, 122])
            # 46
            t.append([134, 130, 124])
            # 47
            t.append([136, 143, 126])
            # 48
            t.append([137, 145, 129])
            # 49
            t.append([139, 148, 131])
            # 50
            t.append([141, 150, 133])
            # 51
            t.append([143, None, 135])
            # 52
            t.append([145, None, 137])
            # 53
            t.append([147, None, 138])
            # 54
            t.append([150, None, 140])
            # 55
            t.append([None, None, 142])
            # 56
            t.append([None, None, 144])
            # 57
            t.append([None, None, 148])
            # 58
            t.append([None, None, 147])
            # 59
            t.append([None, None, 148])
            # 60
            t.append([None, None, 150])
        # simulation 13 set table - 04/2011
        elif number == 13:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([55, 57, 55])
            # 6
            t.append([56, 59, 56])
            # 7
            t.append([57, 61, 57])
            # 8
            t.append([58, 63, 58])
            # 9
            t.append([59, 65, 59])
            # 10
            t.append([60, 67, 60])
            # 11
            t.append([61, 69, 61])
            # 12
            t.append([62, 71, 62])
            # 13
            t.append([63, 73, 63])
            # 14
            t.append([64, 75, 64])
            # 15
            t.append([66, 77, 66])
            # 16
            t.append([67, 79, 67])
            # 17
            t.append([69, 81, 69])
            # 18
            t.append([70, 83, 70])
            # 19
            t.append([72, 85, 72])
            # 20
            t.append([73, 87, 73])
            # 21
            t.append([75, 89, 75])
            # 22
            t.append([76, 91, 77])
            # 23
            t.append([78, 93, 79])
            # 24
            t.append([79, 95, 81])
            # 25
            t.append([81, 97, 83])
            # 26
            t.append([83, 99, 85])
            # 27
            t.append([85, 101, 87])
            # 28
            t.append([86, 104, 88])
            # 29
            t.append([88, 106, 90])
            # 30
            t.append([90, 108, 92])
            # 31
            t.append([92, 110, 94])
            # 32
            t.append([93, 112, 96])
            # 33
            t.append([95, 114, 97])
            # 34
            t.append([96, 116, 99])
            # 35
            t.append([98, 118, 101])
            # 36
            t.append([100, 120, 103])
            # 37
            t.append([101, 122, 105])
            # 38
            t.append([103, 124, 107])
            # 39
            t.append([104, 126, 109])
            # 40
            t.append([106, 128, 111])
            # 41
            t.append([108, 130, 113])
            # 42
            t.append([109, 132, 115])
            # 43
            t.append([111, 134, 116])
            # 44
            t.append([112, 136, 118])
            # 45
            t.append([114, 138, 120])
            # 46
            t.append([116, 140, 122])
            # 47
            t.append([117, 142, 124])
            # 48
            t.append([119, 144, 126])
            # 49
            t.append([120, 147, 128])
            # 50
            t.append([122, 150, 130])
            # 51
            t.append([124, None, 132])
            # 52
            t.append([126, None, 134])
            # 53
            t.append([128, None, 135])
            # 54
            t.append([131, None, 137])
            # 55
            t.append([134, None, 139])
            # 56
            t.append([139, None, 141])
            # 57
            t.append([145, None, 143])
            # 58
            t.append([150, None, 145])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 14 set table - 07/2011
        elif number == 14:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 54, 53])
            # 4
            t.append([54, 56, 54])
            # 5
            t.append([55, 58, 55])
            # 6
            t.append([56, 60, 56])
            # 7
            t.append([57, 62, 57])
            # 8
            t.append([58, 64, 58])
            # 9
            t.append([59, 66, 59])
            # 10
            t.append([60, 68, 60])
            # 11
            t.append([61, 70, 61])
            # 12
            t.append([62, 72, 62])
            # 13
            t.append([63, 75, 63])
            # 14
            t.append([64, 77, 64])
            # 15
            t.append([66, 79, 65])
            # 16
            t.append([68, 81, 66])
            # 17
            t.append([69, 83, 67])
            # 18
            t.append([71, 85, 69])
            # 19
            t.append([72, 87, 70])
            # 20
            t.append([74, 89, 72])
            # 21
            t.append([76, 91, 74])
            # 22
            t.append([77, 93, 76])
            # 23
            t.append([79, 95, 77])
            # 24
            t.append([80, 97, 79])
            # 25
            t.append([82, 99, 81])
            # 26
            t.append([84, 101, 83])
            # 27
            t.append([85, 103, 85])
            # 28
            t.append([87, 106, 86])
            # 29
            t.append([88, 108, 88])
            # 30
            t.append([90, 110, 90])
            # 31
            t.append([92, 112, 92])
            # 32
            t.append([94, 114, 94])
            # 33
            t.append([95, 115, 95])
            # 34
            t.append([97, 117, 97])
            # 35
            t.append([99, 119, 99])
            # 36
            t.append([101, 121, 101])
            # 37
            t.append([102, 123, 103])
            # 38
            t.append([104, 126, 104])
            # 39
            t.append([105, 128, 106])
            # 40
            t.append([107, 130, 108])
            # 41
            t.append([109, 132, 110])
            # 42
            t.append([110, 134, 112])
            # 43
            t.append([112, 136, 114])
            # 44
            t.append([113, 138, 116])
            # 45
            t.append([115, 140, 118])
            # 46
            t.append([117, 142, 120])
            # 47
            t.append([119, 144, 122])
            # 48
            t.append([120, 146, 123])
            # 49
            t.append([122, 148, 125])
            # 50
            t.append([124, 150, 127])
            # 51
            t.append([126, None, 129])
            # 52
            t.append([129, None, 131])
            # 53
            t.append([132, None, 132])
            # 54
            t.append([135, None, 134])
            # 55
            t.append([138, None, 136])
            # 56
            t.append([142, None, 138])
            # 57
            t.append([146, None, 141])
            # 58
            t.append([150, None, 144])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 15 set table - 10/2011
        elif number == 15:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 55, 54])
            # 5
            t.append([55, 57, 55])
            # 6
            t.append([56, 59, 56])
            # 7
            t.append([57, 61, 57])
            # 8
            t.append([59, 63, 58])
            # 9
            t.append([61, 65, 59])
            # 10
            t.append([63, 67, 60])
            # 11
            t.append([65, 69, 61])
            # 12
            t.append([67, 71, 62])
            # 13
            t.append([68, 72, 63])
            # 14
            t.append([70, 74, 64])
            # 15
            t.append([72, 76, 65])
            # 16
            t.append([74, 78, 66])
            # 17
            t.append([76, 80, 68])
            # 18
            t.append([77, 83, 69])
            # 19
            t.append([79, 85, 71])
            # 20
            t.append([81, 87, 72])
            # 21
            t.append([83, 89, 74])
            # 22
            t.append([85, 91, 76])
            # 23
            t.append([87, 93, 78])
            # 24
            t.append([89, 95, 80])
            # 25
            t.append([91, 97, 82])
            # 26
            t.append([93, 99, 84])
            # 27
            t.append([95, 101, 86])
            # 28
            t.append([97, 104, 88])
            # 29
            t.append([99, 106, 90])
            # 30
            t.append([101, 108, 92])
            # 31
            t.append([103, 110, 94])
            # 32
            t.append([105, 112, 96])
            # 33
            t.append([107, 114, 97])
            # 34
            t.append([109, 116, 99])
            # 35
            t.append([111, 118, 101])
            # 36
            t.append([113, 120, 103])
            # 37
            t.append([115, 122, 105])
            # 38
            t.append([116, 125, 106])
            # 39
            t.append([118, 127, 108])
            # 40
            t.append([120, 129, 110])
            # 41
            t.append([122, 131, 112])
            # 42
            t.append([124, 133, 114])
            # 43
            t.append([125, 135, 115])
            # 44
            t.append([127, 137, 117])
            # 45
            t.append([129, 139, 119])
            # 46
            t.append([131, 141, 121])
            # 47
            t.append([133, 144, 123])
            # 48
            t.append([135, 147, 125])
            # 49
            t.append([137, 148, 127])
            # 50
            t.append([139, 150, 129])
            # 51
            t.append([141, None, 131])
            # 52
            t.append([144, None, 133])
            # 53
            t.append([147, None, 134])
            # 54
            t.append([150, None, 136])
            # 55
            t.append([None, None, 138])
            # 56
            t.append([None, None, 140])
            # 57
            t.append([None, None, 142])
            # 58
            t.append([None, None, 145])
            # 59
            t.append([None, None, 147])
            # 60
            t.append([None, None, 150])
        # simulation 16 set table - 12/2011
        elif number == 16:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 54, 54])
            # 5
            t.append([55, 56, 55])
            # 6
            t.append([57, 58, 56])
            # 7
            t.append([59, 60, 57])
            # 8
            t.append([61, 62, 58])
            # 9
            t.append([63, 64, 59])
            # 10
            t.append([65, 66, 61])
            # 11
            t.append([67, 68, 62])
            # 12
            t.append([69, 70, 63])
            # 13
            t.append([71, 71, 65])
            # 14
            t.append([73, 73, 67])
            # 15
            t.append([75, 75, 69])
            # 16
            t.append([77, 77, 71])
            # 17
            t.append([79, 79, 72])
            # 18
            t.append([80, 82, 74])
            # 19
            t.append([82, 84, 75])
            # 20
            t.append([84, 86, 77])
            # 21
            t.append([86, 88, 79])
            # 22
            t.append([88, 90, 81])
            # 23
            t.append([89, 93, 82])
            # 24
            t.append([91, 95, 84])
            # 25
            t.append([93, 97, 86])
            # 26
            t.append([95, 99, 88])
            # 27
            t.append([97, 102, 90])
            # 28
            t.append([99, 104, 91])
            # 29
            t.append([101, 107, 93])
            # 30
            t.append([103, 109, 95])
            # 31
            t.append([105, 111, 97])
            # 32
            t.append([107, 113, 99])
            # 33
            t.append([108, 115, 100])
            # 34
            t.append([110, 117, 102])
            # 35
            t.append([112, 119, 104])
            # 36
            t.append([114, 121, 106])
            # 37
            t.append([116, 123, 108])
            # 38
            t.append([117, 126, 110])
            # 39
            t.append([119, 128, 112])
            # 40
            t.append([121, 130, 114])
            # 41
            t.append([123, 132, 116])
            # 42
            t.append([125, 134, 118])
            # 43
            t.append([127, 136, 119])
            # 44
            t.append([129, 138, 121])
            # 45
            t.append([131, 140, 123])
            # 46
            t.append([133, 142, 125])
            # 47
            t.append([135, 144, 127])
            # 48
            t.append([137, 146, 128])
            # 49
            t.append([139, 148, 130])
            # 50
            t.append([141, 150, 132])
            # 51
            t.append([143, None, 134])
            # 52
            t.append([145, None, 136])
            # 53
            t.append([147, None, 137])
            # 54
            t.append([150, None, 139])
            # 55
            t.append([None, None, 141])
            # 56
            t.append([None, None, 143])
            # 57
            t.append([None, None, 144])
            # 58
            t.append([None, None, 146])
            # 59
            t.append([None, None, 148])
            # 60
            t.append([None, None, 150])
        # simulation 17 set table - 02/2012
        elif number == 17:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([53, 54, 52])
            # 3
            t.append([55, 56, 53])
            # 4
            t.append([57, 58, 54])
            # 5
            t.append([59, 60, 55])
            # 6
            t.append([61, 62, 56])
            # 7
            t.append([63, 65, 57])
            # 8
            t.append([65, 68, 58])
            # 9
            t.append([67, 71, 59])
            # 10
            t.append([69, 74, 60])
            # 11
            t.append([71, 76, 61])
            # 12
            t.append([72, 78, 63])
            # 13
            t.append([74, 81, 65])
            # 14
            t.append([75, 83, 67])
            # 15
            t.append([77, 85, 69])
            # 16
            t.append([79, 87, 71])
            # 17
            t.append([81, 89, 72])
            # 18
            t.append([82, 90, 74])
            # 19
            t.append([84, 92, 75])
            # 20
            t.append([86, 94, 77])
            # 21
            t.append([88, 96, 79])
            # 22
            t.append([89, 98, 80])
            # 23
            t.append([91, 99, 82])
            # 24
            t.append([92, 101, 83])
            # 25
            t.append([94, 103, 85])
            # 26
            t.append([96, 105, 87])
            # 27
            t.append([97, 106, 89])
            # 28
            t.append([99, 108, 90])
            # 29
            t.append([100, 109, 92])
            # 30
            t.append([102, 111, 94])
            # 31
            t.append([104, 113, 96])
            # 32
            t.append([106, 115, 98])
            # 33
            t.append([107, 116, 99])
            # 34
            t.append([109, 118, 101])
            # 35
            t.append([111, 120, 103])
            # 36
            t.append([113, 122, 105])
            # 37
            t.append([114, 124, 107])
            # 38
            t.append([116, 125, 109])
            # 39
            t.append([117, 127, 111])
            # 40
            t.append([119, 129, 113])
            # 41
            t.append([121, 131, 115])
            # 42
            t.append([122, 133, 117])
            # 43
            t.append([124, 134, 118])
            # 44
            t.append([125, 136, 120])
            # 45
            t.append([127, 138, 122])
            # 46
            t.append([129, 140, 124])
            # 47
            t.append([131, 142, 126])
            # 48
            t.append([133, 144, 127])
            # 49
            t.append([135, 147, 129])
            # 50
            t.append([138, 150, 131])
            # 51
            t.append([141, None, 133])
            # 52
            t.append([144, None, 135])
            # 53
            t.append([147, None, 136])
            # 54
            t.append([150, None, 138])
            # 55
            t.append([None, None, 140])
            # 56
            t.append([None, None, 142])
            # 57
            t.append([None, None, 144])
            # 58
            t.append([None, None, 146])
            # 59
            t.append([None, None, 148])
            # 60
            t.append([None, None, 150])
        # simulation 18 set table - 04/2012
        elif number == 18:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([54, 54, 54])
            # 5
            t.append([55, 55, 55])
            # 6
            t.append([56, 56, 56])
            # 7
            t.append([57, 58, 57])
            # 8
            t.append([58, 60, 58])
            # 9
            t.append([59, 62, 59])
            # 10
            t.append([60, 64, 60])
            # 11
            t.append([61, 66, 61])
            # 12
            t.append([62, 68, 62])
            # 13
            t.append([63, 69, 63])
            # 14
            t.append([64, 71, 64])
            # 15
            t.append([65, 73, 66])
            # 16
            t.append([66, 75, 68])
            # 17
            t.append([67, 77, 69])
            # 18
            t.append([68, 80, 71])
            # 19
            t.append([69, 82, 72])
            # 20
            t.append([70, 84, 74])
            # 21
            t.append([72, 86, 76])
            # 22
            t.append([73, 88, 78])
            # 23
            t.append([75, 91, 80])
            # 24
            t.append([76, 93, 82])
            # 25
            t.append([78, 95, 84])
            # 26
            t.append([80, 97, 86])
            # 27
            t.append([82, 99, 88])
            # 28
            t.append([83, 102, 89])
            # 29
            t.append([85, 104, 91])
            # 30
            t.append([87, 106, 93])
            # 31
            t.append([89, 108, 95])
            # 32
            t.append([91, 111, 97])
            # 33
            t.append([92, 113, 98])
            # 34
            t.append([94, 116, 100])
            # 35
            t.append([96, 118, 102])
            # 36
            t.append([98, 120, 104])
            # 37
            t.append([100, 122, 106])
            # 38
            t.append([101, 125, 107])
            # 39
            t.append([103, 127, 109])
            # 40
            t.append([105, 129, 111])
            # 41
            t.append([107, 131, 113])
            # 42
            t.append([109, 133, 115])
            # 43
            t.append([110, 136, 117])
            # 44
            t.append([112, 138, 119])
            # 45
            t.append([114, 140, 121])
            # 46
            t.append([116, 142, 123])
            # 47
            t.append([117, 144, 125])
            # 48
            t.append([119, 146, 126])
            # 49
            t.append([121, 148, 128])
            # 50
            t.append([123, 150, 130])
            # 51
            t.append([126, None, 132])
            # 52
            t.append([129, None, 134])
            # 53
            t.append([131, None, 136])
            # 54
            t.append([133, None, 138])
            # 55
            t.append([137, None, 140])
            # 56
            t.append([141, None, 142])
            # 57
            t.append([145, None, 144])
            # 58
            t.append([150, None, 146])
            # 59
            t.append([None, None, 148])
            # 60
            t.append([None, None, 150])
        # NEW GRADING SYSTEM
        # simulation 19 set table - 02/2013
        elif number == 19:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 56, 53])
            # 4
            t.append([54, 58, 54])
            # 5
            t.append([55, 60, 55])
            # 6
            t.append([57, 62, 56])
            # 7
            t.append([59, 65, 58])
            # 8
            t.append([61, 67, 60])
            # 9
            t.append([63, 70, 62])
            # 10
            t.append([65, 72, 64])
            # 11
            t.append([67, 74, 66])
            # 12
            t.append([69, 77, 68])
            # 13
            t.append([71, 79, 70])
            # 14
            t.append([73, 82, 72])
            # 15
            t.append([75, 84, 74])
            # 16
            t.append([77, 87, 77])
            # 17
            t.append([79, 90, 79])
            # 18
            t.append([82, 92, 82])
            # 19
            t.append([84, 95, 84])
            # 20
            t.append([86, 98, 87])
            # 21
            t.append([88, 101, 90])
            # 22
            t.append([90, 103, 92])
            # 23
            t.append([93, 106, 95])
            # 24
            t.append([95, 108, 97])
            # 25
            t.append([97, 111, 100])
            # 26
            t.append([99, 114, 103])
            # 27
            t.append([101, 116, 105])
            # 28
            t.append([104, 119, 108])
            # 29
            t.append([106, 121, 110])
            # 30
            t.append([108, 124, 113])
            # 31
            t.append([110, 127, 115])
            # 32
            t.append([112, 130, 118])
            # 33
            t.append([115, 132, 120])
            # 34
            t.append([117, 135, 123])
            # 35
            t.append([119, 138, 125])
            # 36
            t.append([122, 140, 128])
            # 37
            t.append([125, 143, 130])
            # 38
            t.append([128, 145, 132])
            # 39
            t.append([131, 148, 135])
            # 40
            t.append([134, 150, 138])
            # 41
            t.append([137, None, 140])
            # 42
            t.append([141, None, 142])
            # 43
            t.append([145, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 20 set table - 04/2013
        elif number == 20:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([52, 52, 51])
            # 2
            t.append([54, 55, 52])
            # 3
            t.append([56, 57, 53])
            # 4
            t.append([58, 60, 54])
            # 5
            t.append([61, 62, 55])
            # 6
            t.append([63, 65, 57])
            # 7
            t.append([65, 67, 59])
            # 8
            t.append([67, 70, 61])
            # 9
            t.append([69, 73, 63])
            # 10
            t.append([71, 76, 65])
            # 11
            t.append([73, 79, 67])
            # 12
            t.append([75, 81, 69])
            # 13
            t.append([77, 84, 72])
            # 14
            t.append([79, 86, 74])
            # 15
            t.append([81, 89, 76])
            # 16
            t.append([83, 91, 78])
            # 17
            t.append([85, 94, 80])
            # 18
            t.append([87, 96, 83])
            # 19
            t.append([89, 99, 85])
            # 20
            t.append([91, 101, 87])
            # 21
            t.append([93, 104, 89])
            # 22
            t.append([95, 107, 92])
            # 23
            t.append([97, 109, 94])
            # 24
            t.append([99, 112, 97])
            # 25
            t.append([101, 115, 99])
            # 26
            t.append([103, 117, 101])
            # 27
            t.append([105, 120, 104])
            # 28
            t.append([106, 122, 106])
            # 29
            t.append([108, 125, 109])
            # 30
            t.append([110, 127, 111])
            # 31
            t.append([112, 129, 113])
            # 32
            t.append([114, 131, 116])
            # 33
            t.append([116, 134, 118])
            # 34
            t.append([118, 136, 121])
            # 35
            t.append([120, 138, 123])
            # 36
            t.append([122, 141, 125])
            # 37
            t.append([124, 143, 128])
            # 38
            t.append([126, 145, 130])
            # 39
            t.append([128, 148, 133])
            # 40
            t.append([130, 150, 135])
            # 41
            t.append([134, None, 137])
            # 42
            t.append([139, None, 140])
            # 43
            t.append([144, None, 142])
            # 44
            t.append([150, None, 145])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        # simulation 21 set table - 07/2013
        elif number == 21:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([52, 52, 51])
            # 2
            t.append([54, 54, 52])
            # 3
            t.append([56, 56, 53])
            # 4
            t.append([58, 58, 54])
            # 5
            t.append([61, 60, 56])
            # 6
            t.append([63, 62, 58])
            # 7
            t.append([65, 64, 59])
            # 8
            t.append([68, 67, 61])
            # 9
            t.append([70, 69, 62])
            # 10
            t.append([72, 71, 64])
            # 11
            t.append([74, 74, 66])
            # 12
            t.append([76, 77, 68])
            # 13
            t.append([78, 79, 71])
            # 14
            t.append([80, 82, 73])
            # 15
            t.append([82, 85, 75])
            # 16
            t.append([84, 87, 77])
            # 17
            t.append([86, 90, 80])
            # 18
            t.append([87, 92, 82])
            # 19
            t.append([89, 95, 85])
            # 20
            t.append([91, 97, 87])
            # 21
            t.append([93, 100, 89])
            # 22
            t.append([95, 102, 92])
            # 23
            t.append([98, 105, 94])
            # 24
            t.append([100, 107, 97])
            # 25
            t.append([102, 110, 99])
            # 26
            t.append([104, 113, 101])
            # 27
            t.append([106, 116, 104])
            # 28
            t.append([107, 118, 106])
            # 29
            t.append([109, 121, 109])
            # 30
            t.append([111, 124, 111])
            # 31
            t.append([113, 127, 113])
            # 32
            t.append([115, 129, 116])
            # 33
            t.append([117, 132, 118])
            # 34
            t.append([119, 134, 121])
            # 35
            t.append([121, 137, 123])
            # 36
            t.append([124, 139, 125])
            # 37
            t.append([126, 142, 128])
            # 38
            t.append([129, 144, 130])
            # 39
            t.append([131, 147, 133])
            # 40
            t.append([134, 150, 135])
            # 41
            t.append([138, None, 137])
            # 42
            t.append([142, None, 140])
            # 43
            t.append([146, None, 142])
            # 44
            t.append([150, None, 145])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        # simulation 22 set table - 10/2013
        elif number == 22:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 55, 52])
            # 3
            t.append([53, 58, 53])
            # 4
            t.append([55, 61, 54])
            # 5
            t.append([57, 64, 56])
            # 6
            t.append([59, 67, 57])
            # 7
            t.append([61, 70, 58])
            # 8
            t.append([62, 72, 60])
            # 9
            t.append([64, 75, 62])
            # 10
            t.append([66, 78, 64])
            # 11
            t.append([68, 80, 66])
            # 12
            t.append([71, 83, 68])
            # 13
            t.append([73, 85, 70])
            # 14
            t.append([76, 88, 72])
            # 15
            t.append([78, 90, 74])
            # 16
            t.append([80, 92, 77])
            # 17
            t.append([83, 95, 79])
            # 18
            t.append([85, 97, 82])
            # 19
            t.append([88, 100, 84])
            # 20
            t.append([90, 102, 87])
            # 21
            t.append([92, 104, 90])
            # 22
            t.append([95, 107, 92])
            # 23
            t.append([97, 109, 95])
            # 24
            t.append([100, 112, 97])
            # 25
            t.append([102, 114, 100])
            # 26
            t.append([104, 116, 102])
            # 27
            t.append([107, 119, 105])
            # 28
            t.append([109, 121, 107])
            # 29
            t.append([112, 124, 110])
            # 30
            t.append([114, 126, 112])
            # 31
            t.append([116, 128, 115])
            # 32
            t.append([118, 131, 118])
            # 33
            t.append([121, 133, 120])
            # 34
            t.append([123, 136, 123])
            # 35
            t.append([125, 138, 125])
            # 36
            t.append([127, 140, 128])
            # 37
            t.append([130, 143, 130])
            # 38
            t.append([132, 145, 132])
            # 39
            t.append([135, 148, 135])
            # 40
            t.append([137, 150, 138])
            # 41
            t.append([140, None, 140])
            # 42
            t.append([143, None, 142])
            # 43
            t.append([146, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 23 set table - 12/2013
        elif number == 23:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 56, 53])
            # 4
            t.append([55, 58, 55])
            # 5
            t.append([57, 61, 57])
            # 6
            t.append([58, 63, 59])
            # 7
            t.append([60, 66, 61])
            # 8
            t.append([61, 68, 63])
            # 9
            t.append([63, 71, 65])
            # 10
            t.append([64, 73, 67])
            # 11
            t.append([66, 75, 69])
            # 12
            t.append([68, 78, 71])
            # 13
            t.append([71, 80, 74])
            # 14
            t.append([73, 83, 76])
            # 15
            t.append([75, 85, 78])
            # 16
            t.append([77, 88, 81])
            # 17
            t.append([80, 91, 83])
            # 18
            t.append([82, 93, 86])
            # 19
            t.append([85, 96, 88])
            # 20
            t.append([87, 99, 91])
            # 21
            t.append([89, 102, 93])
            # 22
            t.append([92, 104, 95])
            # 23
            t.append([94, 107, 98])
            # 24
            t.append([97, 109, 100])
            # 25
            t.append([99, 112, 102])
            # 26
            t.append([101, 115, 105])
            # 27
            t.append([103, 117, 107])
            # 28
            t.append([106, 120, 110])
            # 29
            t.append([108, 122, 112])
            # 30
            t.append([110, 125, 115])
            # 31
            t.append([112, 128, 117])
            # 32
            t.append([114, 130, 119])
            # 33
            t.append([117, 133, 122])
            # 34
            t.append([119, 135, 124])
            # 35
            t.append([121, 138, 126])
            # 36
            t.append([124, 140, 129])
            # 37
            t.append([127, 143, 131])
            # 38
            t.append([129, 145, 134])
            # 39
            t.append([132, 148, 136])
            # 40
            t.append([135, 150, 138])
            # 41
            t.append([138, None, 140])
            # 42
            t.append([142, None, 142])
            # 43
            t.append([146, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 24 set table - 02/2014
        elif number == 24:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([52, 52, 51])
            # 2
            t.append([54, 54, 52])
            # 3
            t.append([56, 56, 53])
            # 4
            t.append([58, 58, 54])
            # 5
            t.append([60, 60, 56])
            # 6
            t.append([62, 62, 57])
            # 7
            t.append([64, 64, 58])
            # 8
            t.append([65, 66, 60])
            # 9
            t.append([67, 68, 62])
            # 10
            t.append([69, 71, 64])
            # 11
            t.append([71, 74, 66])
            # 12
            t.append([73, 76, 68])
            # 13
            t.append([75, 79, 70])
            # 14
            t.append([78, 81, 72])
            # 15
            t.append([80, 84, 74])
            # 16
            t.append([82, 87, 77])
            # 17
            t.append([84, 90, 79])
            # 18
            t.append([86, 92, 82])
            # 19
            t.append([88, 95, 84])
            # 20
            t.append([90, 98, 86])
            # 21
            t.append([92, 101, 89])
            # 22
            t.append([94, 104, 91])
            # 23
            t.append([96, 107, 94])
            # 24
            t.append([98, 110, 97])
            # 25
            t.append([100, 113, 99])
            # 26
            t.append([102, 116, 102])
            # 27
            t.append([104, 119, 105])
            # 28
            t.append([106, 121, 107])
            # 29
            t.append([108, 124, 110])
            # 30
            t.append([110, 127, 112])
            # 31
            t.append([112, 130, 115])
            # 32
            t.append([114, 132, 118])
            # 33
            t.append([116, 135, 120])
            # 34
            t.append([118, 137, 123])
            # 35
            t.append([120, 140, 125])
            # 36
            t.append([122, 142, 128])
            # 37
            t.append([124, 144, 130])
            # 38
            t.append([126, 146, 132])
            # 39
            t.append([129, 148, 135])
            # 40
            t.append([132, 150, 138])
            # 41
            t.append([136, None, 140])
            # 42
            t.append([140, None, 142])
            # 43
            t.append([145, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 25 set table - 04/2014
        elif number == 25:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([52, 52, 51])
            # 2
            t.append([55, 55, 52])
            # 3
            t.append([57, 57, 53])
            # 4
            t.append([60, 60, 55])
            # 5
            t.append([62, 62, 57])
            # 6
            t.append([64, 65, 59])
            # 7
            t.append([66, 67, 61])
            # 8
            t.append([69, 70, 63])
            # 9
            t.append([71, 72, 65])
            # 10
            t.append([73, 75, 67])
            # 11
            t.append([75, 78, 69])
            # 12
            t.append([77, 80, 71])
            # 13
            t.append([79, 83, 73])
            # 14
            t.append([81, 85, 75])
            # 15
            t.append([83, 88, 77])
            # 16
            t.append([85, 91, 79])
            # 17
            t.append([87, 93, 82])
            # 18
            t.append([88, 96, 84])
            # 19
            t.append([90, 98, 87])
            # 20
            t.append([92, 101, 89])
            # 21
            t.append([94, 104, 91])
            # 22
            t.append([96, 106, 93])
            # 23
            t.append([98, 109, 96])
            # 24
            t.append([100, 111, 98])
            # 25
            t.append([102, 114, 100])
            # 26
            t.append([104, 117, 102])
            # 27
            t.append([106, 119, 105])
            # 28
            t.append([108, 122, 107])
            # 29
            t.append([110, 124, 110])
            # 30
            t.append([112, 127, 112])
            # 31
            t.append([114, 129, 114])
            # 32
            t.append([116, 132, 116])
            # 33
            t.append([118, 134, 119])
            # 34
            t.append([120, 137, 121])
            # 35
            t.append([122, 139, 123])
            # 36
            t.append([124, 141, 125])
            # 37
            t.append([126, 144, 128])
            # 38
            t.append([128, 146, 130])
            # 39
            t.append([130, 148, 133])
            # 40
            t.append([133, 150, 135])
            # 41
            t.append([136, None, 137])
            # 42
            t.append([140, None, 140])
            # 43
            t.append([145, None, 142])
            # 44
            t.append([150, None, 145])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        # simulation 26 set table - 10/2014
        elif number == 26:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 56, 53])
            # 4
            t.append([54, 58, 54])
            # 5
            t.append([55, 60, 55])
            # 6
            t.append([56, 62, 56])
            # 7
            t.append([57, 65, 58])
            # 8
            t.append([58, 67, 60])
            # 9
            t.append([60, 70, 62])
            # 10
            t.append([62, 72, 64])
            # 11
            t.append([64, 74, 66])
            # 12
            t.append([66, 77, 68])
            # 13
            t.append([69, 79, 70])
            # 14
            t.append([71, 82, 72])
            # 15
            t.append([73, 84, 74])
            # 16
            t.append([75, 86, 77])
            # 17
            t.append([78, 89, 79])
            # 18
            t.append([80, 91, 82])
            # 19
            t.append([83, 94, 84])
            # 20
            t.append([85, 96, 87])
            # 21
            t.append([87, 98, 90])
            # 22
            t.append([89, 101, 93])
            # 23
            t.append([92, 103, 95])
            # 24
            t.append([94, 106, 98])
            # 25
            t.append([96, 108, 101])
            # 26
            t.append([98, 111, 104])
            # 27
            t.append([101, 113, 106])
            # 28
            t.append([103, 116, 109])
            # 29
            t.append([106, 118, 111])
            # 30
            t.append([108, 121, 114])
            # 31
            t.append([110, 124, 117])
            # 32
            t.append([113, 126, 119])
            # 33
            t.append([115, 129, 122])
            # 34
            t.append([118, 131, 124])
            # 35
            t.append([120, 134, 127])
            # 36
            t.append([122, 137, 130])
            # 37
            t.append([125, 140, 133])
            # 38
            t.append([128, 143, 135])
            # 39
            t.append([131, 146, 138])
            # 40
            t.append([134, 150, 141])
            # 41
            t.append([138, None, 143])
            # 42
            t.append([142, None, 144])
            # 43
            t.append([146, None, 146])
            # 44
            t.append([150, None, 147])
            # 45
            t.append([None, None, 149])
            # 46
            t.append([None, None, 150])
        # simulation 27 set table - 12/2014
        elif number == 27:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 57, 53])
            # 4
            t.append([54, 59, 54])
            # 5
            t.append([55, 62, 56])
            # 6
            t.append([56, 64, 58])
            # 7
            t.append([58, 67, 60])
            # 8
            t.append([60, 69, 62])
            # 9
            t.append([62, 72, 64])
            # 10
            t.append([64, 74, 66])
            # 11
            t.append([66, 77, 68])
            # 12
            t.append([68, 79, 70])
            # 13
            t.append([70, 82, 73])
            # 14
            t.append([72, 84, 75])
            # 15
            t.append([74, 87, 77])
            # 16
            t.append([77, 90, 79])
            # 17
            t.append([79, 92, 82])
            # 18
            t.append([82, 95, 84])
            # 19
            t.append([84, 97, 87])
            # 20
            t.append([87, 100, 89])
            # 21
            t.append([90, 103, 91])
            # 22
            t.append([92, 105, 94])
            # 23
            t.append([95, 108, 96])
            # 24
            t.append([98, 110, 99])
            # 25
            t.append([100, 113, 101])
            # 26
            t.append([103, 115, 104])
            # 27
            t.append([105, 118, 106])
            # 28
            t.append([108, 120, 109])
            # 29
            t.append([110, 123, 111])
            # 30
            t.append([113, 125, 114])
            # 31
            t.append([116, 128, 116])
            # 32
            t.append([118, 130, 119])
            # 33
            t.append([121, 133, 121])
            # 34
            t.append([123, 135, 124])
            # 35
            t.append([126, 138, 126])
            # 36
            t.append([129, 140, 128])
            # 37
            t.append([131, 143, 131])
            # 38
            t.append([134, 145, 133])
            # 39
            t.append([136, 148, 136])
            # 40
            t.append([139, 150, 138])
            # 41
            t.append([142, None, 140])
            # 42
            t.append([144, None, 142])
            # 43
            t.append([147, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 28 set table - 02/2015
        elif number == 28:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 57, 53])
            # 4
            t.append([54, 60, 54])
            # 5
            t.append([55, 63, 55])
            # 6
            t.append([56, 66, 57])
            # 7
            t.append([57, 69, 59])
            # 8
            t.append([59, 72, 61])
            # 9
            t.append([61, 75, 63])
            # 10
            t.append([63, 78, 65])
            # 11
            t.append([65, 80, 67])
            # 12
            t.append([68, 83, 69])
            # 13
            t.append([70, 85, 70])
            # 14
            t.append([73, 88, 72])
            # 15
            t.append([75, 90, 74])
            # 16
            t.append([77, 92, 77])
            # 17
            t.append([80, 95, 79])
            # 18
            t.append([82, 97, 82])
            # 19
            t.append([85, 100, 84])
            # 20
            t.append([87, 102, 87])
            # 21
            t.append([89, 104, 89])
            # 22
            t.append([92, 106, 92])
            # 23
            t.append([94, 109, 94])
            # 24
            t.append([97, 111, 97])
            # 25
            t.append([99, 113, 99])
            # 26
            t.append([101, 115, 101])
            # 27
            t.append([104, 118, 104])
            # 28
            t.append([106, 120, 106])
            # 29
            t.append([109, 123, 109])
            # 30
            t.append([111, 125, 111])
            # 31
            t.append([113, 127, 113])
            # 32
            t.append([116, 129, 116])
            # 33
            t.append([118, 132, 118])
            # 34
            t.append([121, 134, 121])
            # 35
            t.append([123, 136, 123])
            # 36
            t.append([125, 139, 125])
            # 37
            t.append([128, 142, 128])
            # 38
            t.append([130, 145, 130])
            # 39
            t.append([133, 148, 133])
            # 40
            t.append([135, 150, 135])
            # 41
            t.append([138, None, 137])
            # 42
            t.append([142, None, 140])
            # 43
            t.append([146, None, 142])
            # 44
            t.append([150, None, 145])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        # simulation 29 set table - 07/2015
        elif number == 29:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([53, 53, 53])
            # 4
            t.append([55, 55, 54])
            # 5
            t.append([57, 57, 55])
            # 6
            t.append([59, 59, 56])
            # 7
            t.append([60, 61, 57])
            # 8
            t.append([62, 63, 58])
            # 9
            t.append([63, 65, 60])
            # 10
            t.append([65, 67, 62])
            # 11
            t.append([67, 70, 64])
            # 12
            t.append([70, 73, 66])
            # 13
            t.append([72, 76, 68])
            # 14
            t.append([75, 79, 70])
            # 15
            t.append([77, 82, 72])
            # 16
            t.append([79, 85, 75])
            # 17
            t.append([81, 88, 77])
            # 18
            t.append([83, 91, 80])
            # 19
            t.append([85, 94, 82])
            # 20
            t.append([87, 97, 85])
            # 21
            t.append([89, 100, 88])
            # 22
            t.append([92, 103, 90])
            # 23
            t.append([94, 106, 93])
            # 24
            t.append([97, 109, 95])
            # 25
            t.append([99, 112, 98])
            # 26
            t.append([101, 115, 101])
            # 27
            t.append([103, 118, 103])
            # 28
            t.append([105, 121, 106])
            # 29
            t.append([107, 124, 108])
            # 30
            t.append([109, 127, 111])
            # 31
            t.append([111, 130, 114])
            # 32
            t.append([113, 133, 116])
            # 33
            t.append([116, 135, 119])
            # 34
            t.append([118, 138, 121])
            # 35
            t.append([120, 140, 124])
            # 36
            t.append([123, 142, 127])
            # 37
            t.append([125, 144, 129])
            # 38
            t.append([128, 146, 132])
            # 39
            t.append([131, 148, 135])
            # 40
            t.append([135, 150, 138])
            # 41
            t.append([139, None, 140])
            # 42
            t.append([142, None, 142])
            # 43
            t.append([146, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 30 set table - 10/2015
        elif number == 30:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 56, 53])
            # 4
            t.append([54, 58, 55])
            # 5
            t.append([55, 60, 57])
            # 6
            t.append([56, 62, 59])
            # 7
            t.append([58, 65, 60])
            # 8
            t.append([60, 68, 62])
            # 9
            t.append([62, 71, 63])
            # 10
            t.append([64, 74, 65])
            # 11
            t.append([66, 76, 67])
            # 12
            t.append([68, 79, 69])
            # 13
            t.append([70, 81, 71])
            # 14
            t.append([72, 84, 73])
            # 15
            t.append([74, 86, 75])
            # 16
            t.append([77, 89, 77])
            # 17
            t.append([79, 91, 80])
            # 18
            t.append([82, 94, 82])
            # 19
            t.append([84, 96, 85])
            # 20
            t.append([87, 99, 87])
            # 21
            t.append([90, 101, 90])
            # 22
            t.append([92, 104, 92])
            # 23
            t.append([95, 106, 95])
            # 24
            t.append([97, 109, 97])
            # 25
            t.append([100, 111, 100])
            # 26
            t.append([103, 113, 102])
            # 27
            t.append([106, 116, 105])
            # 28
            t.append([108, 118, 107])
            # 29
            t.append([111, 121, 110])
            # 30
            t.append([114, 123, 112])
            # 31
            t.append([117, 125, 115])
            # 32
            t.append([119, 128, 117])
            # 33
            t.append([122, 130, 120])
            # 34
            t.append([124, 133, 122])
            # 35
            t.append([127, 135, 125])
            # 36
            t.append([130, 138, 127])
            # 37
            t.append([132, 141, 130])
            # 38
            t.append([135, 144, 132])
            # 39
            t.append([137, 147, 135])
            # 40
            t.append([140, 150, 137])
            # 41
            t.append([142, None, 140])
            # 42
            t.append([145, None, 142])
            # 43
            t.append([147, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 31 set table - 02/2016
        elif number == 31:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 55, 52])
            # 3
            t.append([53, 58, 53])
            # 4
            t.append([54, 60, 54])
            # 5
            t.append([55, 63, 56])
            # 6
            t.append([56, 66, 58])
            # 7
            t.append([57, 68, 60])
            # 8
            t.append([59, 71, 62])
            # 9
            t.append([61, 74, 64])
            # 10
            t.append([63, 77, 66])
            # 11
            t.append([65, 80, 68])
            # 12
            t.append([67, 82, 70])
            # 13
            t.append([68, 85, 72])
            # 14
            t.append([70, 87, 74])
            # 15
            t.append([72, 90, 76])
            # 16
            t.append([74, 92, 78])
            # 17
            t.append([76, 95, 81])
            # 18
            t.append([78, 97, 83])
            # 19
            t.append([80, 100, 86])
            # 20
            t.append([82, 102, 88])
            # 21
            t.append([85, 104, 91])
            # 22
            t.append([87, 107, 93])
            # 23
            t.append([90, 109, 96])
            # 24
            t.append([92, 112, 98])
            # 25
            t.append([95, 114, 101])
            # 26
            t.append([98, 116, 103])
            # 27
            t.append([101, 119, 106])
            # 28
            t.append([103, 121, 108])
            # 29
            t.append([106, 124, 111])
            # 30
            t.append([109, 126, 113])
            # 31
            t.append([112, 129, 115])
            # 32
            t.append([114, 131, 118])
            # 33
            t.append([117, 134, 120])
            # 34
            t.append([119, 136, 123])
            # 35
            t.append([122, 139, 125])
            # 36
            t.append([125, 141, 128])
            # 37
            t.append([128, 143, 130])
            # 38
            t.append([130, 145, 133])
            # 39
            t.append([133, 148, 135])
            # 40
            t.append([136, 150, 138])
            # 41
            t.append([139, None, 140])
            # 42
            t.append([142, None, 142])
            # 43
            t.append([146, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 32 set table - 04/2016 - to complete
        elif number == 32:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 54, 52])
            # 3
            t.append([53, 56, 53])
            # 4
            t.append([54, 58, 54])
            # 5
            t.append([55, 60, 56])
            # 6
            t.append([56, 62, 58])
            # 7
            t.append([57, 64, 60])
            # 8
            t.append([59, 67, 62])
            # 9
            t.append([61, 69, 64])
            # 10
            t.append([63, 71, 66])
            # 11
            t.append([65, 74, 68])
            # 12
            t.append([67, 76, 70])
            # 13
            t.append([68, 79, 73])
            # 14
            t.append([70, 81, 75])
            # 15
            t.append([72, 84, 77])
            # 16
            t.append([75, 87, 79])
            # 17
            t.append([77, 89, 81])
            # 18
            t.append([80, 92, 84])
            # 19
            t.append([82, 94, 86])
            # 20
            t.append([85, 97, 88])
            # 21
            t.append([87, 99, 90])
            # 22
            t.append([89, 102, 93])
            # 23
            t.append([92, 104, 95])
            # 24
            t.append([94, 107, 98])
            # 25
            t.append([96, 109, 100])
            # 26
            t.append([99, 112, 102])
            # 27
            t.append([101, 115, 105])
            # 28
            t.append([104, 117, 107])
            # 29
            t.append([106, 120, 110])
            # 30
            t.append([109, 123, 112])
            # 31
            t.append([111, 125, 114])
            # 32
            t.append([114, 128, 117])
            # 33
            t.append([116, 130, 119])
            # 34
            t.append([119, 133, 122])
            # 35
            t.append([121, 135, 124])
            # 36
            t.append([124, 138, 126])
            # 37
            t.append([127, 141, 129])
            # 38
            t.append([129, 144, 131])
            # 39
            t.append([132, 147, 134])
            # 40
            t.append([135, 150, 136])
            # 41
            t.append([138, None, 139])
            # 42
            t.append([142, None, 141])
            # 43
            t.append([146, None, 144])
            # 44
            t.append([150, None, 146])
            # 45
            t.append([None, None, 148])
            # 46
            t.append([None, None, 150])
        # simulation 33 set table - 09/2016
        elif number == 33:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 51, 51])
            # 2
            t.append([52, 52, 52])
            # 3
            t.append([54, 54, 53])
            # 4
            t.append([56, 56, 55])
            # 5
            t.append([58, 58, 57])
            # 6
            t.append([60, 60, 59])
            # 7
            t.append([62, 62, 60])
            # 8
            t.append([63, 64, 62])
            # 9
            t.append([65, 66, 64])
            # 10
            t.append([67, 68, 66])
            # 11
            t.append([69, 71, 68])
            # 12
            t.append([71, 74, 70])
            # 13
            t.append([74, 76, 72])
            # 14
            t.append([76, 79, 75])
            # 15
            t.append([78, 82, 77])
            # 16
            t.append([80, 85, 79])
            # 17
            t.append([82, 88, 81])
            # 18
            t.append([85, 90, 84])
            # 19
            t.append([87, 93, 86])
            # 20
            t.append([89, 96, 88])
            # 21
            t.append([91, 99, 90])
            # 22
            t.append([93, 102, 93])
            # 23
            t.append([96, 104, 95])
            # 24
            t.append([98, 107, 98])
            # 25
            t.append([100, 110, 100])
            # 26
            t.append([102, 113, 102])
            # 27
            t.append([105, 116, 105])
            # 28
            t.append([107, 118, 107])
            # 29
            t.append([110, 121, 110])
            # 30
            t.append([112, 124, 112])
            # 31
            t.append([114, 127, 114])
            # 32
            t.append([116, 130, 116])
            # 33
            t.append([118, 132, 119])
            # 34
            t.append([120, 135, 121])
            # 35
            t.append([122, 138, 123])
            # 36
            t.append([125, 140, 125])
            # 37
            t.append([127, 143, 128])
            # 38
            t.append([130, 145, 130])
            # 39
            t.append([132, 148, 133])
            # 40
            t.append([135, 150, 135])
            # 41
            t.append([138, None, 137])
            # 42
            t.append([142, None, 140])
            # 43
            t.append([146, None, 142])
            # 44
            t.append([150, None, 144])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        # simulation 34 set table - 12/2016
        elif number == 34:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([52, 52, 51])
            # 2
            t.append([54, 54, 52])
            # 3
            t.append([57, 56, 53])
            # 4
            t.append([60, 58, 54])
            # 5
            t.append([63, 60, 55])
            # 6
            t.append([66, 62, 56])
            # 7
            t.append([68, 65, 58])
            # 8
            t.append([71, 67, 60])
            # 9
            t.append([73, 70, 62])
            # 10
            t.append([75, 72, 64])
            # 11
            t.append([78, 75, 66])
            # 12
            t.append([80, 77, 68])
            # 13
            t.append([81, 80, 70])
            # 14
            t.append([83, 82, 72])
            # 15
            t.append([85, 85, 74])
            # 16
            t.append([87, 88, 76])
            # 17
            t.append([89, 90, 79])
            # 18
            t.append([91, 93, 81])
            # 19
            t.append([93, 95, 84])
            # 20
            t.append([95, 98, 86])
            # 21
            t.append([97, 101, 89])
            # 22
            t.append([99, 103, 92])
            # 23
            t.append([100, 106, 94])
            # 24
            t.append([102, 108, 97])
            # 25
            t.append([104, 110, 100])
            # 26
            t.append([106, 113, 103])
            # 27
            t.append([108, 116, 106])
            # 28
            t.append([110, 118, 108])
            # 29
            t.append([112, 121, 111])
            # 30
            t.append([114, 124, 114])
            # 31
            t.append([116, 127, 117])
            # 32
            t.append([118, 129, 120])
            # 33
            t.append([120, 132, 122])
            # 34
            t.append([122, 134, 125])
            # 35
            t.append([124, 137, 127])
            # 36
            t.append([126, 140, 130])
            # 37
            t.append([128, 142, 133])
            # 38
            t.append([131, 145, 135])
            # 39
            t.append([133, 147, 138])
            # 40
            t.append([136, 150, 141])
            # 41
            t.append([140, None, 142])
            # 42
            t.append([145, None, 144])
            # 43
            t.append([150, None, 146])
            # 44
            t.append([None, None, 147])
            # 45
            t.append([None, None, 149])
            # 46
            t.append([None, None, 150])
        # simulation 35 set table - 02/2017
        elif number == 35:
            # 0
            t.append([50, 50, 50])
            # 1
            t.append([51, 52, 51])
            # 2
            t.append([52, 55, 52])
            # 3
            t.append([53, 58, 53])
            # 4
            t.append([54, 60, 54])
            # 5
            t.append([55, 63, 56])
            # 6
            t.append([57, 66, 58])
            # 7
            t.append([59, 68, 60])
            # 8
            t.append([61, 71, 62])
            # 9
            t.append([63, 74, 64])
            # 10
            t.append([65, 76, 66])
            # 11
            t.append([67, 78, 68])
            # 12
            t.append([69, 81, 70])
            # 13
            t.append([72, 83, 72])
            # 14
            t.append([74, 86, 74])
            # 15
            t.append([76, 88, 76])
            # 16
            t.append([78, 90, 78])
            # 17
            t.append([80, 93, 80])
            # 18
            t.append([83, 95, 83])
            # 19
            t.append([85, 98, 85])
            # 20
            t.append([87, 100, 87])
            # 21
            t.append([89, 103, 89])
            # 22
            t.append([91, 105, 92])
            # 23
            t.append([94, 108, 94])
            # 24
            t.append([96, 110, 97])
            # 25
            t.append([98, 113, 99])
            # 26
            t.append([100, 115, 101])
            # 27
            t.append([102, 117, 103])
            # 28
            t.append([105, 120, 106])
            # 29
            t.append([107, 122, 108])
            # 30
            t.append([109, 124, 110])
            # 31
            t.append([111, 126, 112])
            # 32
            t.append([113, 129, 115])
            # 33
            t.append([116, 131, 117])
            # 34
            t.append([118, 134, 120])
            # 35
            t.append([120, 136, 122])
            # 36
            t.append([123, 139, 124])
            # 37
            t.append([126, 141, 127])
            # 38
            t.append([129, 144, 129])
            # 39
            t.append([132, 147, 132])
            # 40
            t.append([135, 150, 134])
            # 41
            t.append([138, None, 137])
            # 42
            t.append([141, None, 139])
            # 43
            t.append([145, None, 142])
            # 44
            t.append([150, None, 144])
            # 45
            t.append([None, None, 147])
            # 46
            t.append([None, None, 150])
        return