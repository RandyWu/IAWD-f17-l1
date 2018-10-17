# Randy Wu 040914510 CST8279 Practical Midterm using data set 48

import csv, gmplot, re

def convertFileDate (date):
    split_date = re.split("[A-Z]", date)
    result_tuple = (split_date[0], split_date[1])

    return result_tuple

#print (convertFileDate("2017-08-12T14:19:29Zd"))
# Works


def convertFileCoordinates (file_name):
    split_name = file_name.split(",")
    result_tuple = (float(split_name[0]), float(split_name[1]))

    return result_tuple

#print (convertFileCoordinates("45.469807,12.50894"))
# Works

def convertFileCallsign (string):
    if len(string) >= 3:
        return string[:3]
    else:
        return "null"

#print (convertFileCallsign ("hello"))
#print (convertFileCallsign ("hi"))
# Works

def convertFileCallsign1 (string):
    if len(string) >= 3:
        return string[3:]
    else:
        return "null"

#print (convertFileCallsign1 ("hello"))
#print (convertFileCallsign1 ("hi"))
# Works

# ======> The following line prompts the user for the name of the output csv file and stores it in variable f1 (Python 3)
f1 = input("Please input the name of the output csv file (extension included): ")

#open the file for writing and write the header line
wf = open(f1,'w')
wf.write("id,CallSign,ICAO,Flight,Date,Time,Latitude,Longitude,Altitude,Speed,Direction\n")

# ======> The following line prompts the user for the name of the input csv file
#and stores it in variable f2 (Python 3)
f2 = input("Please input the name of the input csv file (extension included): ")

#open the file for reading
with open(f2,'rU') as f:
    reader = csv.reader(f)
    i=1
    #Skip the first line
    next(reader,None)

    #row is a list of all elements in the csv line
    for row in reader:

        # ======> call function convertFileDate on the date/time and store into a tuple t1
        t1 = convertFileDate(row[1])

        cs = row[2]
        # ======> call function convertFileCallsign on the variable cs and store into a variable csp1
        csp1 = convertFileCallsign(cs)

        # ======> call function convertFileCallsign on the variable cs and store into a variable csp2
        csp2 = convertFileCallsign1(cs)

        # ======> call function convertFileCoordinates on the coordinates and store into a tuple t2
        t2 = convertFileCoordinates(row[3])

        #store altitude, speed and direction
        alt = row[4]
        spd = row[5]
        dir = row[6]

        #create the line to write to the file
        strToPrint = (
            str(i) + "," + cs + "," + csp1 + "," + csp2 + "," + t1[0] + "," + t1[1] +
            "," + str(t2[0]) + "," + str(t2[1]) + alt + "," + spd + "," + dir + "\n"
        )

        wf.write(strToPrint)
        # ======> increment line counter by 1
        i += 1

#close the output file
wf.close()

with open(f1,'rU') as f:
    reader = csv.reader(f)
    next(reader, None)
    lat=[]
    lon=[]
    for row in reader:
        # ======> convert the read latitude to a float and store it into a variable lt
        lt = float(row[6])
        #
        # # ======> convert the read longitude to a float and store it into a variable lg
        lg = float(row[7])

        # ======> add lt to the latitude list lat
        lat.append(lt)

        # ======> add lg to the longitude list lon
        lon.append(lg)


#initialize the plot
gmap = gmplot.GoogleMapPlotter(lat[0],lon[0],5)
gmap.scatter(lat, lon, 'cornflowerblue', edge_width=4,marker=False)

#Create the html file
gmap.draw('map.html')
