import csv
def get_animals():
    try:
        request= input("Please choose an animal type (cats/dogs) to display: ")
        check_csv(request)
    except:
        request = input("Sorry we dont have any of these, please try again")
        get_animals()

def check_csv(request):    
    with open(f'data/{request}.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
        animals = list(spamreader)
        animals.pop(0)
        for row in animals :
            print(f"{row[0]} is a{row[1]} year old{row[2]}")

get_animals()