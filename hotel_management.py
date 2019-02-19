#Display a menu asking whether to check in or check out
#Prompt the user for a floor number, then a room number
#If checking in, ask for the number of occupants and what their names are
#If checking out, remove the occupants from that room
#Do not allow anyone to check into a room that is already occupied
#Do not allow checking out of a room that isn't occupied

#Used to print hotel dictionary in a readable format
import json

#Initialize hotel dictionary with guests
hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}


#Prompt user for Check In/Out status as well as floor and room number
checking_status = input("Welcome. Are you checking in or out? (Enter 'in' or 'out'): ").lower()
floor_number = input("Please enter the floor number (digits only): ")
room_number = input("Please enter the room number (digits only): ")


#If checking in, ask for number of occupants and ask for names
if(checking_status == "in"):

  #While loop is used to check if the room is taken. If it is, it prompts the user for another floor/room number
  roomTaken = True
  while(roomTaken):
      if room_number in hotel[floor_number]:
          print("Already Occupied.")
          floor_number = input("Please enter the floor number (digits only): ")
          room_number = input("Please enter the room number (digits only): ")
      else:
          hotel[floor_number] = {room_number: []}
          roomTaken = False
    
  #Prompts the user for the number of occupants and their names
  occupants_number = int(input("Please enter the number of occupants (digits only): "))
  count = 1
  while count < occupants_number + 1:
    occupant_name = input("Please enter Occupant %d's name: " % count)
    hotel[floor_number][room_number].append(occupant_name)
    count += 1
 
if(checking_status == "out"):

  #While loop is used to check if the room was taken. If it is not, it prompts the user for another floor/room number
  roomEmpty = True
  while(roomEmpty):
    if room_number not in hotel[floor_number]:
      print("Room is not occupied.")
      floor_number = input("Please enter the floor number (digits only): ")
      room_number = input("Please enter the room number (digits only): ")
    else:
      roomEmpty = False
  
  #Deletes room number as well as occupants from the hotel dictionary
  del hotel[floor_number][room_number]


print(json.dumps(hotel, indent=2))