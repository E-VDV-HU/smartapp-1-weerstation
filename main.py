# Smart app sprint 1: weerstation
# Esper

# Variables
totaal_dagen = range(1,8) # begint bij 1 ivm dag 1, eindigt bij 8 ivm python logica ofzo
temp_celcius_list = [] # leeg lijstje om de temp_celcius in op te slaan en later het gemiddelde uit te rekenen.
dag = 0 # +1 komt automatisch bij de for loop in de functie weerstation()

# Functions
def vraag_input(dag):
    while True:
        temp_celcius = input(f"dag {dag}: Wat is momenteel de temp_celcius? \n > ")
        if temp_celcius == "" or temp_celcius == " ":
            print("Lege waarde! Exiting...")
            exit()
        else: 
            try:
                temp_celcius = float(temp_celcius)
                break
            except:
                print(f"{temp_celcius} is geen getal! \n Probeer opnieuw...")
                continue

    while True:    
        windsnelheid = input (f"dag {dag}: Wat is momenteel de windsnelheid? \n > ")
        if windsnelheid == "" or windsnelheid == " ":
            print(f"Lege waarde! Exiting...")
            exit()
        else:
            try: 
                windsnelheid = float(windsnelheid)
                break
            except:
                print(f"{windsnelheid} is geen getal! \n Probeer opnieuw...")
                continue

    while True:
        luchtvochtigheid = input (f"dag {dag}: Wat is momenteel de luchtvochtigheid? Vul in als percentage \n > ")
        if luchtvochtigheid == "" or luchtvochtigheid == " ":
            print("Lege waarde! Exiting...")
            exit()
        else:
            try:
                luchtvochtigheid = int(luchtvochtigheid) # kan ook float...? idk of dat wel of niet moet.
                if luchtvochtigheid > 100 or luchtvochtigheid < 0:
                    print(f"{luchtvochtigheid} is geen percentage! \n Probeer opnieuw...")
                    continue
                else:
                    break
            except:
                print(f"{luchtvochtigheid} is geen getal! \n Probeer opnieuw...")
                continue

    return temp_celcius, windsnelheid, luchtvochtigheid

def Fahrenheit_b(temp_celcius):
    # print(type(temp_celcius))
    Fahrenheit = 32 + 1.8 * temp_celcius
    # print(Fahrenheit) # print komt bij weerstation()
    return Fahrenheit

def gevoelstemperatuur_b(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoelstemperatuur = temp_celcius - luchtvochtigheid / 100 * windsnelheid
    # print(gevoelstemperatuur) # print komt bij weerstation()
    return gevoelstemperatuur

def weerrapport(windsnelheid,gevoelstemperatuur): # moet anders volgens de opdracht, even controleren bij de docent.
    if gevoelstemperatuur < 0:
        if  windsnelheid > 10:
            return "Het is heel koud en het stormt! Verwarming helemaal aan!"
        elif windsnelheid <= 10:
            return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif gevoelstemperatuur >= 0 and gevoelstemperatuur < 10:
        if windsnelheid > 12:
            return "Het is best koud en het waait; verwarming aan en roosters dicht!"
        elif windsnelheid <= 12:
            return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif gevoelstemperatuur >= 10 and gevoelstemperatuur < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation(temp_celcius_list,dag):
    for dag in totaal_dagen:
        temp_celcius, windsnelheid, luchtvochtigheid = vraag_input(dag)
        Fahrenheit = Fahrenheit_b(temp_celcius)
        gevoelstemperatuur = gevoelstemperatuur_b(temp_celcius, windsnelheid, luchtvochtigheid)
        print(f"Het is {temp_celcius}C ({Fahrenheit}F)")
        print(weerrapport(windsnelheid,gevoelstemperatuur))
        temp_celcius_list.append(temp_celcius)
        temp_celcius_gemiddelde = sum(temp_celcius_list) / len(temp_celcius_list)
        print(f"Het is gemiddeld {temp_celcius_gemiddelde}C")
        print("================================")
    print("Weerstation is klaar met de input van 7 dagen. Exiting...")
    
    
weerstation(temp_celcius_list,dag)