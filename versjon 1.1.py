# programmeringsprosjekt skole. 10 klasse julespill
# Navn: the package thief
# versjon 1.1
# du som leser dette, ikke ha høye forventninger
# ---------------------------------------------------------
 
import time
 

def startup():
    #startmeny
    cls()	
    print("velkommen til julemysteriet")
    print("versjon 1.1")
    print("1. start fra begynnelsen" "\n" "2. savegames (kommer)" "\n" "3. credits")
    svar = input("")
 
    if svar == ("1"):
        game_start()
    
    elif svar == ("2"):
        savegames()
    
    elif svar == ("3"):
        creds()
    
    else:
        cls()
        print("beklager, noe gikk galt. Prøv igjen" "\n""(trykk enter)")
        vent_på_reaksjon = input()
        startup()
 
#--------------------storyline-----------------
 
def game_start():
    cls()
    global kjønn
    global hårfarge
    global navn
 
    print("_--lag din karakter--_""\n" "1.gutt" "\n" "2.jente")
    kjønn = input("")
    if kjønn == ("1"):
        kjønn = str("gutt")
    elif kjønn ==("2"):
        kjønn = str("jente")
    else:
        cls()
        kjønn = 0
        print("opsann, der gikk noe galt. prøv på ny")
        vent_på_reaksjon = input("")
        game_start()
    cls()
    
    print("_--hårfarge--_" "\n" "1.blondt" "\n" "2.svart" "\n" "3.brunt")
    hårfarge = input("")
    if hårfarge == ("1"):
        hårfarge = str("blondt")
    elif hårfarge == ("2"):
        hårfarge = str("svart")
    elif hårfarge ==("3"):
        hårfarge = str("brunt")
    else:
        cls()
        print("noe gikk galt, husk at du må velge noe på begge spørsmålene" "\n" "hvis ikke kommer du ikke videre")
        print("trykk enter")
        vent_på_reaksjon = input("")
        game_start()
           
    cls()
    print("_-navn-_" "\n" "hva vil du at navnet ditt skal være?")
    navn = str(input(""))
    cls()
    print("du heter " + navn + ", du er en " + kjønn + ". og håret ditt er " +hårfarge +"\n" "intressant valg" "\n" "spillet vil starte når du trykke enter. ta tiden du trenger")
    vent_på_reaksjon = input("")
    wake_up(kjønn,hårfarge,navn)
 
 
def wake_up(kjønn,hudfarge,navn):
    global kledd_på
    # veldig mange if/elif/else statments på vei.
    cls()
    print("Beep... Beeep... Beeep... det er alarmklokken. Klokken er 11:00, det er lørdag. og det er dagen før julaften" "\n" "hva vil du gjøre?")
    print("1.sjekk mobilen din")
    print("2.stå opp, og kle deg")
    print("3.prøv å sove litt lengre")
    svar = input("")
    if svar == ("1"):
        cls()
        print("sjekker telefonen din..." "\n" "Du ser på varslingene dine, og du har blitt bombandert av meldinger fra venner. julepresangene deres har blitt stjålet...")
        print("(trykk enter)")
        vent_på_reaksjon = input()
        gavene_er_stjålet()    
 
    
    elif svar == ("2"):
        cls()
        print("du står opp og går bort til skapet ditt, hva klær tar du på deg?")
        print("1.noe fargerikt")
        print("2.noe grått")
        kledd_på = input("")
        gavene_er_stjålet()
 
    elif svar == ("3"):
        cls()
        prøv_å_sov()
    
    else:
        wake_up(kjønn,hudfarge,navn)
 
 
def prøv_å_sov():
    cls()
    print("du prøver å sove litt lengre. men du får så mange varslinger at nysjerrigheten din tar over, og du sjekker hva folk vil...")
    print("\n" "du ser at folk har lagt ut at presangene deres er blitt stjålet over natten. Julen er ødelagt for bygda")
    print("(trykk enter)")
    vent_på_reaksjon = input("")
    gavene_er_stjålet()
 
 
def gavene_er_stjålet():
    global kledd_på
    cls()
    print("du finner ut at du må sjekke om gavene dine også er blitt stjålet")
    if kledd_på == 0:
        print("først må du kle deg. du går bort til skapet ditt, hva klær skal du ta på deg?")
        print("1.noe fargerikt")
        print("2.noe grått")
        kledd_på = input("")
        if kledd_på == ("0"):
            gavene_er_stjålet()
        if kledd_på == ("1"):
            cls()
            print("\n" "du tar på deg fargerike klær, passendes kledning til at det snart er jul")
        elif kledd_på == ("2"):
            cls()
            print("\n" "du tar på deg gråe kær, (generation depression mutch?)")
        print("\n" "nå som at du er kledd, springer du ut rommet og ned trappen. og inn i stuen.")
        print("du ser bort til juletreet, og til din forskrekkelse ser du at du og har blitt ett offer for denne gavebanditten...")
    else:
        print("du springer ned ut av rommet, ned trappen og inn i stuen")
        print("du ser bort til juletreet, og til din forskrekkelse ser du at du og har blitt ett offer for denne gavebanditten...")     
    input("(trykk enter)")
    frokost()
 
 
def frokost():
    global mat_spist
    global energi
    cls()
    print("dette må du gjøre noe med!" "\n" "men mat er alltid en prioritet, du går bort til kjøkkenet...")
    print("1.spis loff med sjokoladepålegg (det er jo lørdag tross alt)")
    print("2.spis grovbrød med makrell i tomat på. (fisk er jo godt det og)")
    svar = input("")
    if svar == ("1"):
        cls()
        print("du spiser loff med sjokoladepålegg, kanskje ikke det mest mettende." "\n" "men det smaker jo godt")
        mat_spist = 1
        energi = 2
        input("(trykk enter) ")
        ut_og_lete(mat_spist,energi)

    elif svar == ("2"):
        cls()
        print("du spiser grovbrød med makrell i tomat" "\n" "masse energi å hente ut ifra dette måltidet :)")
        mat_spist = 2
        energi = 4
        input("(trykk enter) ")
        ut_og_lete(mat_spist,energi)
    
    else:
        frokost()
  
  
def ut_og_lete(ms,energi):
    har_lommelykt = 0
    har_matpakke = 0
   
    cls()
    if ms == (1):
        mat = ("loff")
    elif ms == (2):
        mat = ("fisk")
    print("med "+ mat + " i magen er du nå klar for å finne gavene!")
    print("nå, skal du pakke med noe?")
    print("1.Ja, må jo det" "\n" "2.Nei, går fint det. Skal jo bare se meg rundt")
    svar = input("")
    if svar == ("1"):
        cls()
        print("\n" "du bestemmer deg for å ta med noe på leteaksjonen din.")
        print("1.lommelykt (dagene er jo korte)""\n" "2.matpakke (hvordan ellers skal man hodle konsentrasjonen oppe?)")
        print("(skriv noe annet / blankt for å angre)")
        svar = input("")
        if svar == ("1"):
            cls()
            print("du tar med en lommelyk. det er jo korte dager tross alt")
            har_lommelykt = 1
            input("(trykk enter) ")
            ut_og_lete_2(ms,energi,har_lommelykt,har_matpakke)

        elif svar == ("2"):
            cls()
            print("du pakker en matpakke med.""\n" "det er tross alt viktigt med jevne kosttilskudd gjennom dagen.")
            har_matpakke = 1
            input("(trykk enter) ")
            ut_og_lete_2(ms,energi,har_lommelykt,har_matpakke)

        else:
            ut_og_lete(ms,energi)
    
    elif svar == ("2"):
        print("du velger å ikke ta med deg noe...")
        input("(trykk enter) ")
        ut_og_lete_2(ms,energi,har_lommelykt,har_matpakke)

    else:
        ut_og_lete(ms,energi)    


def ut_og_lete_2(ms,energi,har_lommelykt,har_matpakke):
    cls()
    print(har_lommelykt)
    print(har_matpakke)
    input("")






#-----------------------utilities---------------------#
 
def savegames():
    cls()
    print("kommer i en sener versjon :)")
    vent_på_reaksjon = input("")
    startup()
 
 
def creds():
    cls()
    print("Duh, Håkon J. 10F" "\n" "trykk enter")
    vent_på_reaksjon = input()
    startup()
 
 
def cls():
    # laget som en workaround til at det er forskjellige måter å gjøre cls på forskjellige os'er
    # kan ha litt glitchy effekt når man ikke er i fullskjerm, men funker intil videre
    print("\n"*200)
    return
 
def loading():
    cls()
    print(".")
    time.sleep(1)
    cls()
    print("..")
    time.sleep(1)
    cls()
    print("...")
    time.sleep(1)
    cls()
    print(".")
    time.sleep(1)
    cls()
    print("..")
    time.sleep(1)
    cls()
    print("...")
    time.sleep(1)
    startup()
 
#---------------------varibler og greier----------------------
kjønn = 0
# 1,mann 2,dame
hårfarge = 0
#1,blonnd 2,svart hår 3,brunt
navn = "x"
 
kledd_på = 0
#0,av 1,farget 2,grått
 
mat_spist = 0
#0,ingenting 1,loff 2,grovbrød

energi = 0
#0,ingen energi 2,lav 4,høy

har_lommelykt = 0
har_matpakke = 0

loading()



