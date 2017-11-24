import csv
import random

userid = 1
#20 character
character_list = ['IsMale','IsYoung','IsPretty','IsWorking','IsRetired','IsFoolish','IsPoor',
                'HasBought','IsRich','HasChild','IsMarried','IsGood','IsBad','IsUgly','IsFit','IsTall',
                'IsShort','IsOld','HasSaving','CanSwim']
value_list = ['Yes','No']
print("Start")
with open('sample.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    while (userid <= 100000):
        print(userid)
        character_number = 0
        while (character_number <= 19):
            spamwriter.writerow(['User' + str(userid)] + [character_list[character_number]] + [value_list[random.randint(0,1)]] )
            character_number = character_number + 1        
        userid = userid + 1