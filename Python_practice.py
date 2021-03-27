voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

voting_data.insert(1,{'County':'El Paso','registered_voters':461149})
print(voting_data)


counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#temperature = int(input("What is the temperature outside? "))

temperature = 90
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")   

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso i90s not in the list of counties.")    

    
counties_tuple = ("Arapahoe","Denver","Jefferson")
for county in counties_tuple:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for counties in  counties_dict:
    print (counties_dict.get(counties))

for county,voters in counties_dict.items():
    print(county,voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print  (county_dict)

for i in range(len(voting_data)):

      print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)     

for voting_dict in voting_data:
    print(voting_dict['registered_voters'])
    #for item,values in voting_dict.items():
     #   'print (values)        