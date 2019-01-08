names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]


PERSON_DATA = {"JACK": "12/04/1999", "JILL": "01/01/2000", "HARRY": "27/03/1982"}
input_name = input("Enter name : ").upper()
while input_name != PERSON_DATA :
    print("No data.")
    input_name = input("Enter name : ").upper()
if input_name in PERSON_DATA :
    print(input_name, "is born on", PERSON_DATA[colors])
    input_name = input("Enter name : ").upper()

