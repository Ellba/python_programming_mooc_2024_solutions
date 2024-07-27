# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    result = True 

    if len(pic) != 11 :
        result = False

    if pic[6] == '+':
        year = '18'
    elif pic[6] == '-':
        year = '19'
    elif pic[6] == 'A':
        year = '20'

    format = "%d%m%Y"
    date = pic[:6]
    id = pic[7:10]
    birthdate = pic[:4] + year+pic[4:6]

    try:
        x = datetime.strptime(birthdate, format)
    except:
        result = False

    control = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    d = round((int(date+id) % 31))
    
    if control[d] != pic[-1]:
        result = False

    return result


if __name__ == "__main__":
    is_it_valid("110986+713J")