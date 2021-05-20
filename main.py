import pandas as pd

def ageAnon():
    data = pd.read_csv('fakeData.csv')
    name = data.Name.to_list()
    sex = data.Sex.to_list()
    age = data.Age.to_list()
    zip = data.Zip.to_list()
    condition = data.Condition.to_list()
    for i in range(200):
        if(age[i] == 'Age'):
            return
        if int(age[i]) > 20 and int(age[i]) < 30:
            age[i] = '>=20 and <30'
        elif int(age[i]) >= 30 and int(age[i]) < 40:
            age[i] = '>=30 and <40'
        elif int(age[i]) >= 40 and int(age[i]) < 50:
            age[i] = '>=40 and <50'
        elif int(age[i]) >= 50 and int(age[i]) < 60:
            age[i] = '>=50 and <60'
        elif int(age[i]) >= 60:
            age[i] = '>=60'
        else:
            return
    csvFile = []
    csvFile.append(name)
    csvFile.append(sex)
    csvFile.append(age)
    csvFile.append(zip)
    csvFile.append(condition)
    df = pd.DataFrame(csvFile)
    df = df.T
    df.to_csv('ageData.csv', index=False, header=False)

def zipAnon():
    data = pd.read_csv('fakeData.csv')
    name = data.Name.to_list()
    sex = data.Sex.to_list()
    age = data.Age.to_list()
    zip = data.Zip.to_list()
    condition = data.Condition.to_list()
    for i in range(200):
        if (zip[i] == 'Zip'):
            return
        if int(zip[i]) > 11111 and int(zip[i]) < 20000:
            zip[i] = '1xxxx'
        elif int(zip[i]) >= 20000 and int(zip[i]) < 30000:
            zip[i] = '2xxxx'
        elif int(zip[i]) >= 30000 and int(zip[i]) < 40000:
            zip[i] = '3xxxx'
        elif int(zip[i]) >= 40000 and int(zip[i]) < 50000:
            zip[i] = '4xxxx'
        elif int(zip[i]) >= 40000 and int(zip[i]) < 60000:
            zip[i] = '5xxxx'
        elif int(zip[i]) >= 40000 and int(zip[i]) < 70000:
            zip[i] = '6xxxx'
        elif int(zip[i]) >= 40000 and int(zip[i]) < 80000:
            zip[i] = '7xxxx'
        elif int(zip[i]) >= 40000 and int(zip[i]) < 90000:
            zip[i] = '8xxxx'
        elif int(zip[i]) >= 90000:
            zip[i] = '9xxxx'
        else:
            return
    csvFile = []
    csvFile.append(name)
    csvFile.append(sex)
    csvFile.append(age)
    csvFile.append(zip)
    csvFile.append(condition)
    df = pd.DataFrame(csvFile)
    df = df.T
    df.to_csv('zipData.csv', index=False, header=False)

def sexAnon():
    data = pd.read_csv('fakeData.csv')
    name = data.Name.to_list()
    sex = data.Sex.to_list()
    age = data.Age.to_list()
    zip = data.Zip.to_list()
    condition = data.Condition.to_list()
    for i in range(200):
        if (sex[i] == 'Sex'):
            return
        else:
            sex[i] = 'M/F'
    csvFile = []
    csvFile.append(name)
    csvFile.append(sex)
    csvFile.append(age)
    csvFile.append(zip)
    csvFile.append(condition)
    df = pd.DataFrame(csvFile)
    df = df.T
    df.to_csv('sexData.csv', index=False, header=False)

def conditionAnon():
    data = pd.read_csv('fakeData.csv')
    name = data.Name.to_list()
    sex = data.Sex.to_list()
    age = data.Age.to_list()
    zip = data.Zip.to_list()
    condition = data.Condition.to_list()

    for i in range(200):
        if(condition[i] == 'Condition'):
            return
        elif (condition[i] == 'Coronary atherosclerosis' or condition[i] == 'Hyperlipidemia' or condition[i] == 'Hypertension'):
            condition[i] = 'Cardiovascular Condition'
        elif ('Acute' in condition[i] or 'Allergic' in condition[i] or condition[i] == 'Asthma'):
            condition[i] = 'Respiratory Condition'
        else:
            condition[i] = 'Other'

    csvFile = []
    csvFile.append(name)
    csvFile.append(sex)
    csvFile.append(age)
    csvFile.append(zip)
    csvFile.append(condition)
    df = pd.DataFrame(csvFile)
    df = df.T
    df.to_csv('conditionData.csv', index=False, header=False)

ageAnon()
sexAnon()
zipAnon()
conditionAnon()


