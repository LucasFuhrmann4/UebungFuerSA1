from datetime import datetime
def addUserToList(listOfUserObjects):
    userObject = dict() # {}

    userObject["username"] = input("Bitte geben Sie den Benutzernamen ein: ")
    userObject["password"] = input("Bitte geben Sie das Passwort ein: ")
    userObject["valid"] = True
    userObject["passwordChanged"] = datetime.now()
    userObject["e-mail"] = "lord@kelvin.org"

    listOfUserObjects.append(userObject)

    # Aufgabe 1: Welche Aufgabe implementiert die Funktion addUserToList?

    # Aufgabe 2: Ändern Sie die Funktion so ab, dass der Anwender bei jedem Aufruf den Benutzernamen
    # und das Passwort über die Konsole eingeben muss.

    # Aufgabe 3: Ändern Sie das Änderungsdatum des Passworts auf die aktuelle Uhrzeit.

# Aufgabe 4:
#
# Erstellen Sie eine Funktion checkYear mit dem Parameter listOfUserObjects. Der Parameter
# beinhaltet eine Liste mit allen Benutzerobjekten.

def checkYear(listOfUserObjects):
    for userObject in listOfUserObjects:
        if userObject["passwordChanged"] < datetime(2022, 12, 31):
            userObject["valid"] = False
# Aufgabe 5:
#
# Implementieren Sie nun die Funktion für die Aufgabe 4. Alle Benutzer seit dem
# Jahr 2022 ihr Kennwort nicht geändert haben, werden deaktiviert, in dem der Key valid
# den Value False erhält.

# Aufgabe 6:
#
# Erstellen Sie eine Funktion setValid mit dem Parameter listOfUserObjects. Der Parameter
# beinhaltet eine Liste mit allen Benutzerobjekten.
def setValid(listOfUserObjects):

    for userObject in listOfUserObjects:

        if userObject["valid"] == False:
            print("Hallo " + userObject["username"]+ " Sie müssen Ihr Passwort neu vergeben.")
            userObject["password"] = input("Bitte geben Sie das neue Passwort ein: ")
            userObject["valid"] = True

# Gehen Sie alle Benutzer der Liste des Parameter durch. Jeder Benutzer, welcher
# deaktivert wurde (siehe Aufgabe 5) erhält ein neues Passwort. Das Passwort gibt der
# Anwender über einen input ein. Zudem wird der Value für den valid-Key auf True gesetzt.

# Aufgabe 7:
#
# Prüfen Sie, mittels der Funktion checkMailAdresses(), ob doppelte E-Mail-Adressen vorliegen.

def checkMailAdresses(listOfUserObjects):
    for i, userObjects in enumerate(listOfUserObjects):
        for j in range(i + 1, len(listOfUserObjects)):
            if userObjects["e-mail"] == listOfUserObjects[j]["e-mail"]:
                print("Die Mail " + userObjects["e-mail"]+ " ist bereits vergeben.")
# In dem folgenden Bereich nehmen Sie keine Änderungen vor!
# Testdaten:
userList = list()

user = dict()
user["username"] = "peter.meyer"
user["password"] = "wer2"
user["valid"] = True
user["passwordChanged"] = datetime(2021, 2, 21)
user["e-mail"] = "peter@web.de"

userList.append(user)

user = dict()
user["username"] = "franz.huber"
user["password"] = "Passwort"
user["valid"] = False
user["passwordChanged"] = datetime(2023, 3, 1)
user["e-mail"] = "hubi@gmx.de"

userList.append(user)

user = dict()
user["username"] = "julia.meyer"
user["password"] = "abc123"
user["valid"] = True
user["passwordChanged"] = datetime(2024, 1, 2)
user["e-mail"] = "jule@meyer.de"

userList.append(user)




# Ab hier können Sie Ihre Lösungen testen:
print("Viel Erfolg!")

print(userList)
checkYear(userList)
print(userList)
setValid(userList)
print(userList)
checkMailAdresses(userList)