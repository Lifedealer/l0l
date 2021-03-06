#------------------------------------------------------------------#
#Author  : roissy
#Greetz  : b3mb4m
#Concat  : roissy@tuta.io
#Project : https://github.com/roissy/l0l
#LICENSE : https://github.com/roissy/l0l/blob/master/LICENSE
#------------------------------------------------------------------#


def ExeFile( shellcode, OS=None):
    if OS == None:
        OS = detectOS()

    from logger import logs
    from Database.exedb import ros
    from raw import RawFile


    db = ros()
    padd = ""
    if OS == "linux86":
        padd = db[0]
    elif OS == "linux64":
       padd = db[1]
    elif OS == "windows":
       padd = db[2]
    elif OS == "openbsdx86":
        padd = db[3]
    elif OS == "solarisx86":		
        padd = db[4]
    elif OS == "linuxpowerpc":
        padd = db[5]
    elif OS == "openbsdpowerpc":
        padd = db[6]
    elif OS == "linuxsparc":
        padd = db[7]
    elif OS == "freebsdsparc":
        padd = db[8]
    elif OS == "opensbdsparc":
        padd = db[9]
    elif OS == "solarissparc":
        padd = db[10]
    elif OS == "linuxarm":
        padd = db[11]
    elif OS == "freebsdarm":
        padd = db[12]
    elif OS == "opensbdarm":
       padd = db[13]
    else:
        print "Not supported os .."
        return



    shellcode = shellcode.replace("\\x", "")

    shellcode = padd.replace("SHELLCODE", shellcode)
    logs( shellcode.decode("hex"), None)

