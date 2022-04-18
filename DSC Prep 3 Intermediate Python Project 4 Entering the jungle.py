rarebirds  = {'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True},
        'Pearlescent Kingfisher':{
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False}, 
        'Four-metre Hummingbird':{
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False},
        'Giant Eagle':{
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True},
        'Ancient Vulture':{
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False}
        }
birdlocation = [
    'In the canopy directly above our heads.',
    'Between my 6 and 9 o’clock above.', 
    'Between my 9 and 12 o’clock above.', 
    'Between my 12 and 3 o’clock above.',
    'Between my 3 and 6 o’clock above.',
    'In a nest on the ground.',
    'Right behind you.'
    ]

codes = {'111':birdlocation[0],
        '110':birdlocation[1], 
        '101':birdlocation[2], 
        '100':birdlocation[3], 
        '011':birdlocation[4],
        '010':birdlocation[5],
        '001':birdlocation[6],
 }

actions = ['Back Away', 'Cover our Heads', 'Take a Photograph']

#Task 5:

print("Task 5: " +str(rarebirds['Giant Eagle']['Aggressive']))

#Task 6

print("\nTask 6:")
for key_1, value_1 in rarebirds.items():
    print("\nWe want to find the " + key_1 + "!")
    if rarebirds[key_1]['Aggressive']==True:
        print('Look out! The ' + key_1 + ' is aggressive! ' + actions[1] + "!")
    if rarebirds[key_1]['Endangered']==True:
        print("The " + key_1 + " is endangered. We need to " + actions[0] + "!")
#Task 7
print("\nTask 7:")

for key, value in codes.items():
    print("Remember, if I flash " +key +", it means the bird is: " +value)

#Task 8
for key, value in rarebirds.items():
    rarebirds[key].update({'Seen':False})
#Task 9
encounter = True
#Task 10
while encounter == True:
    sighting1 =(input("What do you see? ")).lower() 
    sighting = sighting1.title()
    if sighting not in rarebirds.keys(): 
       continue
    else: 
        encounter = False
rarebirdsList=list(rarebirds.keys())
rarebirdsList =[x.lower() for x in rarebirdsList]
   
#Task 12
print("\nTask 12")

if sighting1 in rarebirdsList:
    print(sighting + ": this is one of the birds we’re looking for!")
else:
    print("that’s not one of the birds we’re looking for.")

#Task 13
code = str(input("Where do you see it? Input the correct code: "))

#Task 14
location = codes[code]
#Task 15
print("So you've seen a " +  sighting1 +" " + location + " My goodness!")

#Task 16
 
if sighting in rarebirds.keys() and rarebirds[sighting]["Aggressive"]==True:
    print("Careful! The " + str(sighting) + " is aggressive. We need to " + str(actions[0]) + \
    " and " + str(actions[1]) + ". We also need to " + str(actions[2]) + " of " + str(sighting) +      " that is " + location)
elif sighting in rarebirds.keys() and rarebirds[sighting]["Endangered"]==True: 
    print ("The " + sighting + " is endangered. We need to " + actions[0] + " and "+ actions[2]      + " of the " + sighting + " that is " + location)
else: 
    print("We need to " + actions[2] + " of the ultra-rare " + sighting + " that is " + location)

