from datetime import datetime
import argparse

def get_weeks(last_period, discover_weeks):
    last_period_date = datetime.strptime(last_period, '%m/%d/%Y')
    date_to_discover_weeks = datetime.strptime(discover_weeks, '%m/%d/%Y')
    days = (date_to_discover_weeks - last_period_date).days

    """If 1 day is equal to 0,142857143 weeks"""
    weeks = (days * 0.142857143)
    w = str(weeks).split('.')[0]
    r_w = str(weeks).split('.')[1]
    r_w = "0."+r_w

    """If 1 week is equal to 7 days"""
    r_w = round((float(r_w) * 7),1)

    s = int(w)
    d = int(r_w)

    if d > 6:
        x = d - 6
        s = s+1
        d = x

    print("In date "+discover_weeks+" you were with "+str(s)+" weeks and "+str(d)+" days.")
    return str(s)+'w_'+str(d)+'d'

if __name__ == "__main__":
    # read command line arguments
    parser = argparse.ArgumentParser(description='Calculates the number of\
                                                  weeks of pregnancy for some\
                                                  specific date in MM/DD/YYYY format..')
    parser.add_argument('last_period', help='The date of the first day of your\
                                             last menstruation in MM/DD/YYYY format.')
    parser.add_argument('discover_weeks', help='The date you want to find how many\
                                                weeks you are/were/will be in\
                                                MM/DD/YYYY format.')

    args = parser.parse_args()

    get_weeks(args.last_period, args.discover_weeks)

