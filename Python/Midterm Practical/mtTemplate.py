import csv
import gmplot


#The code of your four functions is below


# ======> The following line prompts the user for the name of the output csv file and stores it in variable f1 (Python 3)

#open the file for writing and write the header line
wf = open(f1,'w')
wf.write("id,CallSign,ICAO,Flight,Date,Time,Latitude,Longitude,Altitude,Speed,Direction\n")

# ======> The following line prompts the user for the name of the input csv file
#and stores it in variable f2 (Python 3)

#open the file for reading
with open(f2,'rU') as f:
    reader = csv.reader(f)
    i=1
    #Skip the first line
    next(reader,None)

    #row is a list of all elements in the csv line
    for row in reader:

        # ======> call function convertFileDate on the date/time and store into a tuple t1

        cs = row[2]
        # ======> call function convertFileCallsign on the variable cs and store into a variable csp1

        # ======> call function convertFileCallsign on the variable cs and store into a variable csp2

        # ======> call function convertFileCoordinates on the coordinates and store into a tuple t2

        #store altitude, speed and direction
        alt = row[4]
        spd = row[5]
        dir = row[6]

        #create the line to write to the file
        strToPrint = str(i)+ "," + cs + "," + csp1 + "," +csp2 + "," + t1[0] + "," + t1[1] + "," + str(t2[0]) + "," + str(t2[1]) + "," + alt + "," + spd + "," + dir + "\n"
        wf.write(strToPrint)

        # ======> increment line counter by 1

#close the output file
wf.close()

with open(f1,'rU') as f:
    reader = csv.reader(f)
    next(reader, None)
    lat=[]
    lon=[]
    for row in reader:
        # ======> convert the read latitude to a float and store it into a variable lt

        # ======> convert the read longitude to a float and store it into a variable lg

        # ======> add lt to the latitude list lat

        # ======> add lg to the longitude list lon


#initialize the plot
gmap = gmplot.GoogleMapPlotter(lat[0],lon[0],5)
gmap.scatter(lat, lon, 'cornflowerblue', edge_width=4,marker=False)

#Create the html file
gmap.draw('map.html')
