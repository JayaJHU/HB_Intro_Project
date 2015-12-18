# Which month has the `most number of cars?
# Which week has the most number of cars?
# Which day has the most number of cars?
# Which hour has the most number of cars?
# Which direction (237 Westbound or 237 Eastbound) has the most number of cars?
"""
parses main express lane traffic data into traffic totals by day, week, month &
east/west directions
"""


import csv
import datetime

# Open the csv file

def date_to_day(dateTime):
     """converts date string into days of the week"""
     date = dateTime.split()[0]
     monthlist = date.split("/")
     monthlist[1] = monthlist[1] + ", "

     if monthlist[0] == '1':
          monthlist[0] = "January "
     if monthlist[0] == "2":
          monthlist[0] = "February "
     if monthlist[0] == '3':
          monthlist[0] = "March "
     if monthlist[0] == '4':
          monthlist[0] = "April "
     if monthlist[0] == '5':
          monthlist[0] = "May "
     if monthlist[0] == '6':
          monthlist[0] = "June "
     if monthlist[0] == '7':
          monthlist[0] = "July "
     if monthlist[0] == '8':
          monthlist[0] = "August "
     if monthlist[0] == '9':
          monthlist[0] =  "September "
     if monthlist[0] == '10':
          monthlist[0] = "October "
     if monthlist[0] == '11':
          monthlist[0] = "November "
     if monthlist[0] == '12':
          monthlist[0] = "December "
     date_string = "".join(monthlist)
     weekday = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%A')
     return weekday

def date_to_week(dateTime):
    # dateTime = row[0]  ### (date and time together)
    date = dateTime.split()[0] ### (splitting date and time. Showing date only, 1/1/2014 format)
    monthlist = date.split("/")  ### (splitting date into list, i.e.(['1','1','2014'])
    monthlist[1] = monthlist[1] + ", "    ### (concatenate i.e. 1,)
          
    if monthlist[0] == '1':
         monthlist[0] = "January "
    if monthlist[0] == "2":
         monthlist[0] = "February "
    if monthlist[0] == '3':
         monthlist[0] = "March "
    if monthlist[0] == '4':
         monthlist[0] = "April "
    if monthlist[0] == '5':
         monthlist[0] = "May "
    if monthlist[0] == '6':
         monthlist[0] = "June "
    if monthlist[0] == '7':
        monthlist[0] = "July "
    if monthlist[0] == '8':
        monthlist[0] = "August "
    if monthlist[0] == '9':
         monthlist[0] =  "September "
    if monthlist[0] == '10':
         monthlist[0] = "October "
    if monthlist[0] == '11':
         monthlist[0] = "November "
    if monthlist[0] == '12':
         monthlist[0] = "December "
    date_string = "".join(monthlist)  ### (prints January 1, 2014 format)
    weekday = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%A')   ### (prints day only, i.e Monday)
    week = datetime.datetime.strptime(date_string, '%B %d, %Y').strftime('%W')
    
    return week

def time_to_hour(dateTime):
     # dateTime = row[0]
     # time = dateTime.split()[1] ### (splitting date and time. Showing time only, 05:00 format)
     #dateTime = row[0]
     #date = row[0].split(" ")
     #date_str = date[0]
     time = dateTime[1]
     hour = time.split(':')[0]
     return hour

def total_2014():
     total_traffic = 0
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()
          for row in trafficDataRaw:
               row[3] = int(row[3])
               total_traffic += row[3]
     return total_traffic
          

def month_traffic():
     traffic_month = {"jan": 0, "feb": 0, "mar": 0, "apr":0, "may":0, "june":0, "july":0, "aug":0, "sept":0, "oct":0, "nov": 0, "dec": 0}
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()
          for row in trafficDataRaw:
               date = row[0].split(" ")
               date_str = date[0]
               row[3] = int(row[3])
               month = date_str.split("/")[0]
               # Number of cars in a month
               if month == "1":
                    traffic_month['jan'] +=row[3]         
               elif month == "2":
                    traffic_month['feb'] +=row[3] 
               elif month == "3":
                    traffic_month['mar'] +=row[3] 
               elif month == "4":
                    traffic_month['apr'] +=row[3] 
               elif month == "5":
                    traffic_month['may'] +=row[3] 
               elif month == "6":
                    traffic_month['june'] +=row[3] 
               elif month == "7":
                    traffic_month['july'] +=row[3] 
               elif month == "8":
                    traffic_month['aug'] +=row[3] 
               elif month == "9":
                    traffic_month['sept'] +=row[3] 
               elif month == "10":
                    traffic_month['oct'] +=row[3] 
               elif month == "11":
                    traffic_month['nov'] +=row[3] 
               elif month == "12":
                    traffic_month['dec'] +=row[3] 

     with open('month.csv', 'w') as csv_out:
          fields = traffic_month.keys()
          writer = csv.DictWriter(csv_out, fieldnames=fields)
          writer.writeheader()
          writer.writerow(traffic_month)
     return traffic_month
     

def weekday_traffic():
    traffic_by_days = { "Monday": 0, "Tuesday": 0, "Wednesday": 0,"Thursday": 0, "Friday" :0}
    with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
         trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
         trafficDataRaw.next()
         for row in trafficDataRaw: 
               row[3] = int(row[3])
               iDate = row[0].split(" ") ### splitting datetime into half
               date_str = iDate[0]  ### date 
               weekday = date_to_day(date_str)
                
               if weekday == "Monday":
                    traffic_by_days['Monday'] += row[3]
               if weekday == "Tuesday":
                    traffic_by_days['Tuesday'] += row[3]
               if weekday == "Wednesday":
                    traffic_by_days['Wednesday'] += row[3]
               if weekday == "Thursday":
                    traffic_by_days['Thursday'] += row[3]
               if weekday == "Friday":
                    traffic_by_days['Friday'] += row[3]

    with open('days.csv', 'w') as csv_out:
          fields = traffic_by_days.keys()
          writer = csv.DictWriter(csv_out, fieldnames=fields)
          writer.writeheader()
          writer.writerow(traffic_by_days)
    return traffic_by_days


def weekly_traffic():
     traffic_week = {"week 0":0,"week 1":0,"week 2":0,"week 3":0,"week 4":0,"week 5":0,"week 6":0,"week 7":0,"week 8":0,"week 9":0,"week 10":0,"week 11":0, "week 12":0,"week 13":0,"week 14":0,"week 15":0,"week 16":0,"week 17":0,"week 18":0,"week 19":0,"week 20":0,"week 21":0, "week 22":0,"week 23":0,"week 24":0,"week 25":0,"week 26":0,"week 27":0,"week 28":0,"week 29":0,"week 30":0,"week 31":0,"week 32":0,"week 33":0,"week 34":0,"week 35":0,"week 36":0,"week 37":0, "week 38":0,"week 39":0,"week 40":0,"week 41":0,"week 42":0,"week 43":0,"week 44":0,"week 45":0,"week 46":0,"week 47":0,"week 48":0,"week 49":0,"week 50":0,"week 51":0,"week 52":0}
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()
          for row in trafficDataRaw:
               row[3] = int(row[3])
               iDate = row[0].split(" ") ### splitting datetime into half
               date_str = iDate[0]  ### date 
               week = date_to_week(date_str)
               if week == '00':
                    traffic_week['week 0'] +=row[3]
               if week == '01':
                    traffic_week['week 1'] +=row[3]
               if week == '02':
                    traffic_week['week 2'] +=row[3]
               if week == '03':
                    traffic_week['week 3'] +=row[3]
               if week == '04':
                    traffic_week['week 4'] +=row[3]
               if week == '05':
                    traffic_week['week 5'] +=row[3]
               if week == '06':
                    traffic_week['week 6'] +=row[3]
               if week == '07':
                    traffic_week['week 7'] +=row[3]
               if week == '08':
                    traffic_week['week 8'] +=row[3]
               if week == '09':
                    traffic_week['week 9'] +=row[3]
               if week == '10':
                    traffic_week['week 10'] +=row[3]
               if week == '11':
                    traffic_week['week 11'] +=row[3]
               if week == '12':
                    traffic_week['week 12'] +=row[3]
               if week == '13':
                    traffic_week['week 13'] +=row[3]
               if week == '14':
                    traffic_week['week 14'] +=row[3]
               if week == '15':
                    traffic_week['week 15'] +=row[3]
               if week == '16':
                    traffic_week['week 16'] +=row[3]
               if week == '17':
                    traffic_week['week 17'] +=row[3]
               if week == '18':
                    traffic_week['week 18'] +=row[3]
               if week == '19':
                    traffic_week['week 19'] +=row[3]
               if week == '20':
                    traffic_week['week 20'] +=row[3]
               if week == '21':
                    traffic_week['week 21'] +=row[3]
               if week == '22':
                    traffic_week['week 22'] +=row[3]
               if week == '23':
                    traffic_week['week 23'] +=row[3]
               if week == '24':
                    traffic_week['week 24'] +=row[3]
               if week == '25':
                    traffic_week['week 25'] +=row[3]
               if week == '26':
                    traffic_week['week 26'] +=row[3]
               if week == '27':
                    traffic_week['week 27'] +=row[3]
               if week == '28':
                    traffic_week['week 28'] +=row[3]
               if week == '29':
                    traffic_week['week 29'] +=row[3]
               if week == '30':
                    traffic_week['week 30'] +=row[3]
               if week == '31':
                    traffic_week['week 31'] +=row[3]
               if week == '32':
                    traffic_week['week 32'] +=row[3]
               if week == '33':
                    traffic_week['week 33'] +=row[3]
               if week == '34':
                    traffic_week['week 34'] +=row[3]
               if week == '35':
                    traffic_week['week 35'] +=row[3]
               if week == '36':
                    traffic_week['week 36'] +=row[3]
               if week == '37':
                    traffic_week['week 37'] +=row[3]
               if week == '38':
                    traffic_week['week 38'] +=row[3]
               if week == '39':
                    traffic_week['week 39'] +=row[3]
               if week == '40':
                    traffic_week['week 40'] +=row[3]
               if week == '41':
                    traffic_week['week 41'] +=row[3]
               if week == '42':
                    traffic_week['week 42'] +=row[3]
               if week == '43':
                    traffic_week['week 43'] +=row[3]
               if week == '44':
                    traffic_week['week 44'] +=row[3]
               if week == '45':
                    traffic_week['week 45'] +=row[3]
               if week == '46':
                    traffic_week['week 46'] +=row[3]
               if week == '47':
                    traffic_week['week 47'] +=row[3]
               if week == '48':
                    traffic_week['week 48'] +=row[3]
               if week == '49':
                    traffic_week['week 49'] +=row[3]
               if week == '50':
                    traffic_week['week 50'] +=row[3]
               if week == '51':
                    traffic_week['week 51'] +=row[3]
               if week == '52':
                    traffic_week['week 52'] +=row[3]


     with open('week.csv', 'w') as csv_out:
          fields = traffic_week.keys()
          writer = csv.DictWriter(csv_out, fieldnames=fields)
          writer.writeheader()
          writer.writerow(traffic_week)
     return traffic_week
     
def hourly_traffic():
     traffic_hours = {"am5": 0, "am6": 0, "am7": 0, "am8": 0, "am9": 0, "pm3": 0, "pm4": 0, "pm5": 0, "pm6": 0}
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
         trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
         trafficDataRaw.next()
         for row in trafficDataRaw:
               row[3] = int(row[3])
               dateTime = row[0].split(" ") ### splitting datetime into half
               #time = iDate[1]
               hour = time_to_hour(dateTime)
                ### time
               if hour == '5':
                    traffic_hours['am5'] +=row[3]
               elif hour == '6':
                    traffic_hours['am6'] +=row[3]
               elif hour == '7':
                    traffic_hours['am7'] +=row[3]
               elif hour == '8':
                    traffic_hours['am8'] +=row[3]
               elif hour == '9':
                    traffic_hours['am9'] +=row[3]
               elif hour == '15':
                    traffic_hours['pm3'] +=row[3]
               elif hour == '16':
                    traffic_hours['pm4'] +=row[3]
               elif hour == '17':
                    traffic_hours['pm5'] +=row[3]
               elif hour == '18':
                    traffic_hours['pm6'] +=row[3]

     with open('hour.csv', 'w') as csv_out:
          fields = traffic_hours.keys()
          writer = csv.DictWriter(csv_out, fieldnames=fields)
          writer.writeheader()
          writer.writerow(traffic_hours)

     return traffic_hours
     
def east_west():
     direction = {"West":0, "East":0}
     with open('ExpressLanesTrafficWithTolls-2014.csv', 'rb') as csvfile:
          trafficDataRaw = csv.reader(csvfile, delimiter=',', quotechar='|')
          trafficDataRaw.next()

          for row in trafficDataRaw:
               row[3] = int(row[3])
               if row[1][-1] == 'E':
                    direction["East"] += row[3]
               else:
                    direction["West"] += row[3]
     
     with open('direction.csv', 'w') as csv_out:
          fields = direction.keys()
          writer = csv.DictWriter(csv_out, fieldnames=fields)
          writer.writeheader()
          writer.writerow(direction)

     return direction


def main():
     print total_2014()
     print month_traffic()
     print weekday_traffic()
     print weekly_traffic()
     print hourly_traffic()
     print east_west()
     days_dataframes()

main()
     
     
   