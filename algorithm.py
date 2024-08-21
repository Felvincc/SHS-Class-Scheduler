import sys
import random
import os
from collections import defaultdict


def info():

    all_info=[]

    levels =        (                                       #CHANGE ME BACK

                        "g11_steam",
                        "g12_steam"

                    )
    
    all_info.append(levels)


    section =       (
                        18,
                        18
                    )
    
    all_info.append(section)

    subjects = (                                    # Last to subjects should be the interchangeable subjects (pe, cffs)

                    (
                        "precalc",
                        "stats",
                        "ucsp",
                        "iphp",
                        "esci",
                        "emptech",
                        "oralcom",
                        "peh/cffs",



                    ),

                    (
                        #"english",
                        #"chemistry",
                        #"cpar",
                        "filipino",
                        "biology",
                        "inqvest",
                        "physics",
                        "peh/cffs",

                    )
                )
    
    all_info.append(subjects)

    buildings =     (

                        "suhs",
                        #"guy_hall",           

                    )
    
    all_info.append(buildings)

    floors =        (                  # COUNT FROM one)         
        
                        3,
                        #3
        
                    )
    
    all_info.append(floors)

    rooms =         (           #count from 1
        
                        12,
                        #12
        
                    )
    
    all_info.append(rooms)

    #                   Make exceptions list for rooms that are not able to be used (ex. faculty rooms)

    instructors =   (

                        "jimmy",
                        "bob",
                        "david"

                    )
    
    all_info.append(instructors)
    
    instructors_field = (

                    (

                        "precalc",
                        "genmath"

                    ),

                    (

                        "business_math",
                        "accounting"

                    )

    )

    all_info.append(instructors_field)

    instructors_avail_time = (

                    (
                        "111",
                        "111",
                        "111",
                        "111"
                    ),

                    (
                        "111",
                        "111",
                        "111",
                        "111"
                    ),

                    (
                        "111",
                        "111",
                        "111",
                        "111"
                    )
                )
    
    all_info.append(instructors_avail_time)



    #all_info = (levels, section, subjects, buildings, floors, rooms, instructors, instructors_field, instructors_available_time)

    return all_info

    


def output(compiled_data, chromosome):

    compiled_data=convert()

    # Unpacks
    levels = compiled_data[0]                       # Single list/tuple
    sections = compiled_data[1]                     # Single list/tuple
    instructors_avail_time = compiled_data[2]       # single list/tuple
    parent_subjects = compiled_data[3]              # raw, dict, conv
    parent_buildings = compiled_data[4]             # raw, dict, conv
    parent_floors = compiled_data[5]                # raw, conv
    parent_rooms = compiled_data[6]                 # raw, conv
    parent_instructors = compiled_data[7]           # raw, dict, conv
    parent_instructors_field = compiled_data[8]     # raw, dict, conv

    #chromome is the final output thing

    
    

 
def constrained_randomizer(compiled_data, restricted):

    compiled_data=convert()
    #print(compiled_data)

    # Unpacks
    levels = compiled_data[0]                       # Single list/tuple
    sections = compiled_data[1]                     # Single list/tuple
    instructors_avail_time = compiled_data[2]       # single list/tuple
    parent_subjects = compiled_data[3]              # raw, dict, conv
    parent_buildings = compiled_data[4]             # raw, dict, conv
    parent_floors = compiled_data[5]                # raw, conv
    parent_rooms = compiled_data[6]                 # raw, conv
    parent_instructors = compiled_data[7]           # raw, dict, conv
    parent_instructors_field = compiled_data[8]     # raw, dict, conv

    temp = []
    schedule_counter = []
    
    # combines all the subjects into a set (set to prevent duplicates)
    single_subjects = set()
    for subject in parent_subjects[0]:
        for x in subject:
            single_subjects.add(x)

    # dictionary comprehension for making a dictionary of all the subjects (with no duplicates) with a id number
    subject_id_dict = {element: idx + 1 for idx, element in enumerate(single_subjects)}


    # Creates lists for each level with their respective subject ids
    converted_level_subjects =[]
    for x in range(len(levels)):
        temp = []
        for i in parent_subjects[0][x]:
            
            for key, value in subject_id_dict.items():
                
                if i == key:
                    temp.append(value)
        temp = tuple(temp)
        converted_level_subjects.append(temp)
        
    temp = []
    all_converted_subjects = converted_level_subjects[0]+converted_level_subjects[1]

    # This loop makes the schedule counter, which tracks the subjects used per schedule, this is used to ensure that there will be as little overlapping in subject schedules
    for x in range(2):

        schedule_counter.append([])
        for y in range(6):

            schedule_counter[x].append([])
            for subject in all_converted_subjects:
                
                schedule_counter[x][y].append([subject, 0])

    # makes the thing with the thing (READ THE THING BELOW STUPID)
    temp=[]
    for level in range(2):

        temp.append([])
        for day in range(2):
            temp[level].append([])

            for timeslot in range(6):
                temp[level][day].append(1)

    schedule_restricted = temp
    temp = []



    # Main constrained randomizer =============================

    chromosome = []
    for level in range(len(levels)):

        chromosome_temp = []

        # creates the randomized subject schedule       (I MOVED THIS FROM THE LOOP FROM BELOW, IF SOMETHING BREAKS, PUT ME BACk!!!!!!!!!!(or dont))
        num_subjects = len(parent_subjects[0][level])+1

        for section in range(sections[level]):

            chromosome_temp.append(level)
            chromosome_temp.append(section)

            component_subject, ignore_list, schedule_restricted = rand_subjects_schedule(num_subjects, schedule_counter, subject_id_dict, converted_level_subjects, level, schedule_restricted)
            chromosome_temp.append(tuple(component_subject))

            # gets the randomized building, floors, and rooms values
            num_buildings = len(parent_buildings[0])-1
        
            address_module, error=buildings_floors_rooms(num_buildings,parent_floors,parent_rooms, restricted, ignore_list )
            chromosome_temp.append(address_module)

            if error:

                print("error_01")
                exit()

            chromosome_temp=[]
            chromosome.append(chromosome_temp)
        
    debug = False

    if debug:

        for x in chromosome:
            print(x)

    return chromosome
           
def buildings_floors_rooms(num_buildings,parent_floors,parent_rooms, restricted, ignore_list):

    address_module = []

    # fix restricted stuff
    # restricted format:  [ [[floor], [room], building 1], [[floor], [room], building 2] ]
    # BE SURE YOU APPEND THE RESTRICTED BUILDING AT THE LAST, NEVER AT THE FIRST

    for day in range(2):
        for x in range(6):

            overwrite = False
            if x in ignore_list[day]:

                error = False
                overwrite = True

            in_list = True

            error_01 = 0

            while in_list:
            
                chosen_building = random.randint(0, num_buildings)       # <<<<<<<<<<
                in_list = chosen_building in restricted[day][x]
                error_01 = error_01 + 1

                if error_01 == 500000:

                    error = True
                    return "000000", error
                    

            in_list = True
            error_01 = 0

            while in_list:

                chosen_floor = random.randint(1, len(parent_floors[1][chosen_building]))
                in_list = chosen_floor in restricted[day][x][chosen_building][0]
                error_01 = error_01 + 1

                if error_01 == 500000:
                    error = True
                    return "000000", error

        
            in_list = True
            error_01 = 0
            while in_list:

                chosen_room = random.randint(1,len(parent_rooms[1][chosen_building]))
                in_list = chosen_room in restricted[day][x][chosen_building][1][chosen_floor-1]
                error_01 = error_01 + 1

                if error_01 == 500000:
                    error = True
                    return "000000", error

            # inshallah you will get through debugging
            
            # appends the the values to restricted to preven them from showing up again
            if not overwrite:

                restricted[day][x][chosen_building][1][chosen_floor-1].append(chosen_room)
                if len(restricted[day][x][chosen_building][1][chosen_floor-1]) == len(parent_rooms[1][chosen_building]):

                    restricted[day][x][chosen_building][0].append(chosen_floor)

                if len(restricted[day][x][chosen_building][0]) == len(parent_floors[1][chosen_building]):

                    restricted[day][x][chosen_building].append(chosen_building)

        
            # pads all the values by 2 (1 = 01, 12 = 12, 6 = 06)
            chosen_building = str(chosen_building+1).zfill(2)
            chosen_floor = str(chosen_floor).zfill(2)
            chosen_room = str(chosen_room).zfill(2)

            # adds all the padded stuff together to complete the moudle
            address_module_temp = chosen_building+chosen_floor+chosen_room

            if overwrite:
                address_module_temp = "000000"

            address_module.append(address_module_temp)

            error = False
            debug = False
           
            # self explanatory
            if debug:

                os.system('cls')
                print(restricted)
                print()
                print(address_module)

    temp = []
    temp2 = []

    # halfs the list and turns it into a tuple
    for x in range(len(address_module)):
        temp.append(address_module[x])

        if x == 5 or x == 11:
            temp2.append(tuple(temp))
            
            temp = []

    temp2 = tuple(temp2)

    address_module = temp2

    return address_module, error

# fancy way of making a list with 12 zeros ( [0,0,0,0,0,0,0,0...])
subject_frequency = defaultdict(lambda: [0] * 12)  

# this function turned out more complex than expected
def rand_subjects_schedule(num_subjects, schedule_counter, subject_id_dict, converted_level_subjects, level, schedule_restricted):   
    iterations = 100

    global subject_frequency
    component_subject_2 = None
    best_score = float('inf')

    for _ in range(iterations):
        component_subject = []
        num_subjects_list = []

        # makes list a of "XX", where it is repeated x times, where x is the num of subjects
        for _ in range(1,num_subjects):
            num_subjects_list.append("XX")
        
        # Determine the split point
        half = num_subjects // 2
        
        # Split the subjects into two groups
        first_half = num_subjects_list[:half]
        second_half = num_subjects_list[half:]
        
        # Calculate how many blanks ("00") need to be added to each half
        first_half_blank = 6 - len(first_half)
        second_half_blank = 6 - len(second_half)
        
        # Add blanks to each half
        for _ in range(first_half_blank):
            first_half.insert(random.randint(0, len(first_half)), 0)
        
        for _ in range(second_half_blank):
            second_half.insert(random.randint(0, len(second_half)), 0)
        
        # Combine halves and pad numbers to two digits, also pads the values
        first_half = tuple(str(x).zfill(2) for x in first_half)
        second_half = tuple(str(x).zfill(2) for x in second_half)

        component_subject_temp = first_half, second_half

        for tuple_elem in component_subject_temp:
            temp = [str(int_elem).zfill(2) for int_elem in tuple_elem]
            component_subject.append(tuple(temp))
        
        # Calculate the distribution score (lower is better)
        score = 0
        for i in range(6):
            score += subject_frequency[component_subject[0][i]][i]
            score += subject_frequency[component_subject[1][i]][i + 6]

        # Keep the schedule with the best (lowest) score
        if score < best_score:
            best_score = score
            component_subject_2 = component_subject

    # Update the frequency tracker with the best schedule
    for i in range(6):
        subject_frequency[component_subject_2[0][i]][i] += 1
        subject_frequency[component_subject_2[1][i]][i + 6] += 1

    # Create ignore_list
    ignore_list = []

    best_component_subject = []
    for x in range(2):
        ignore_list.append([])
        for y in range(6):
            if component_subject_2[x][y] == "00":
                ignore_list[x].append(y)
        ignore_list[x] = tuple(ignore_list[x])

    ignore_list = tuple(ignore_list)
    temp = []

    #FFUUUUUUUUUUUUUCKKKKKKK  FIX THI SHIT!!!!!!!!!!!!!!    
    for x in range(2):

        counter = -1
        for y in range(6):

            counter = counter + 1
            subject = component_subject_2[x][y]
            if subject == "00":
                temp.append("00")
                break

            else:


                while 
                condition = False
                
                for i in converted_level_subjects[level]:

                    print(i)

                    for a in schedule_counter[x][counter]:

                        print(a)
                        

                        if i == a[0]:

                            condition = True
                            break

                    if condition:
                        break
                

                if i == converted_level_subjects[level][-1]:
                    schedule_restricted[level][x][counter] = schedule_restricted[level][x][counter] + 1 

    print(component_subject)
    print(temp)


    debug = False
    #print(num_subjects)

    if debug:
        print(component_subject_temp) #Switch me to component_subject_temp for the subject template stuff
        print(ignore_list)

    return component_subject_2, ignore_list, schedule_restricted

        
def convert():

    temp = []
    return_values = []
    return_values_temp=[]


    label = {   # index dictionary labels to prevent eye sores when programming

        "levels":0,
        "sections":1,
        "subjects":2,
        "buildings":3,
        "floors":4,
        "rooms":5,
        "instructors":6,
        "instructors_field":7,
        "instructors_avail_time":8

    }

    all_info = info()

    # No need to convert these data because it will only be used for for loop values, or conditions, as supposed to genes in the chromosome

    levels = all_info[label["levels"]]

    sections = all_info[label["sections"]]           

    instructors_avail_time = all_info[label["instructors_avail_time"]]

    # Appends values above to the final return values

    return_values.append(tuple(levels))                     #sadddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
    return_values.append(tuple(sections))
    return_values.append(tuple(instructors_avail_time))

                         
    #                         raw = straight from data set, no prefix = default data, converted data, dict = conversion dictionary for raw data and converted data,                      
                               
    #Creates raw subjects data                                
    
    raw_subjects = all_info[label["subjects"]]

    # Creates conversion dictionary for subjects

    dict_subjects=[]    

    for raw_subjects_elem in raw_subjects:

        dict_subjects_temp = {index: element for index, element in enumerate(raw_subjects_elem)}

        dict_subjects.append(dict_subjects_temp)


    # Creates default data from raw subject data
    subjects = []

    for subjs in all_info[label["subjects"]]:                                   

        for x in range(len(subjs)):

            temp.append(x)

            if x == len(subjs)-1:

                subjects.append(temp)

                temp = []

    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_subjects))
    return_values_temp.append(dict_subjects)
    return_values_temp.append(tuple(subjects))
    return_values.append(tuple(return_values_temp))
    return_values_temp=[]

                


    # Creates raw buildings data

    raw_buildings = all_info[label["buildings"]]

    # Creates dictionary buildings data

    dict_buildings = {index: element for index, element in enumerate(all_info[label["buildings"]])}


    # Creates default buildings data

    buildings = []

    for buildings_elem in range(len(raw_buildings)):

        buildings.append(buildings_elem)

    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_buildings))
    return_values_temp.append(dict_buildings)
    return_values_temp.append(tuple(buildings))
    return_values.append(tuple(return_values_temp))

    return_values_temp=[]



    # Creates raw floors data

    raw_floors = all_info[label["floors"]]   

    # Creates default floors data

    floors = []

    floors_temp=[]

    for raw_floors_elem in raw_floors:

        for temp in range(raw_floors_elem):

            floors_temp.append(temp)

            if temp == raw_floors_elem-1:

                floors_temp = tuple(floors_temp)

                floors.append(floors_temp)

                floors_temp=[]

    
    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_floors))
    return_values_temp.append(tuple(floors))
    return_values.append(tuple(return_values_temp))
    return_values_temp=[]

    #print(floors)

    # Creates raw rooms data
      
    raw_rooms = all_info[label["rooms"]]

    # Creates default rooms data

    rooms_temp = []

    rooms = []

    for raw_rooms_elem in raw_rooms:

        for temp in range(raw_rooms_elem):

            rooms_temp.append(temp)

            

            if temp == raw_rooms_elem-1:

                rooms.append(rooms_temp)

                rooms_temp = []

    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_rooms))
    return_values_temp.append(tuple(rooms))
    return_values.append(tuple(return_values_temp))
    return_values_temp=[]


                
    # Creates raw instructors

    raw_instructors = all_info[label["instructors"]]

    # Creates dictionary for instructors

    dict_instructors = {index: element for index, element in enumerate(all_info[label["instructors"]])}

    # Creates default instructors data

    instructors = []

    for raw_instructor_elem in range(len(raw_instructors)):

        instructors.append(raw_instructor_elem)

    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_instructors))
    return_values_temp.append(dict_instructors)
    return_values_temp.append(tuple(instructors))
    return_values.append(tuple(return_values_temp))
    return_values_temp=[]
        

    # Create raw instructors field data

    raw_instructors_field = all_info[label["instructors_field"]]

    # Create dictionary for instructors field data

    dict_instructors_field = []

    for raw_instructors_field_elem in raw_instructors_field:

        dict_instructors_field_temp = {index: element for index, element in enumerate(raw_instructors_field_elem)}

        dict_instructors_field.append(dict_instructors_field_temp)

    # Creates defaults instructors field data

    instructors_field = []

    instructors_field_temp = []

    for raw_instructors_field_temp in raw_instructors_field:

        for temp in range(len(raw_instructors_field_temp)):

            instructors_field_temp.append(temp)

            if temp == len(raw_instructors_field_temp)-1:

                instructors_field.append(instructors_field_temp)

                instructors_field_temp = []

    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(tuple(raw_instructors_field))
    return_values_temp.append(dict_instructors_field)
    return_values_temp.append(tuple(instructors_field))
    return_values.append(tuple(return_values_temp))
    return_values_temp=[]


    debug = False

    if debug:
        

        print("\nLevels: ")

        print(levels)
        print("\nSections: ")
        print(sections)

        print()

        print("\nraw subjects: ")
        print(raw_subjects)
        print("\n dict subjects: ")
        print(dict_subjects)
        print("\nsubjects: ")
        print(subjects)

        print()

        print("\nraw buildings: ")
        print(raw_buildings)
        print("\ndict buildings: ")
        print(dict_buildings)
        print("\nbuildings: ")
        print(buildings)

        print()

        print("\nraw_floors: ")
        print(raw_floors)
        print("\nfloors: ")
        print(floors)
        
        print()

        print("\nrooms: ")
        print(rooms)
        print("\nraw rooms: ")
        print(raw_rooms)

        print()

        print("\nraw_instructors: ")
        print(raw_instructors)
        print("\ndict_instructors: ")
        print(dict_instructors)
        print("\ninstructors: ")
        print(instructors)
        
        print()

        print("\nraw_instructors_field: ")
        print(raw_instructors_field)
        print("\ndict_instructors_field: ")
        print(dict_instructors_field)
        print("\ninstructors_field: ")
        print(instructors_field)
        
        print()

        print("\ninstructors_avail_time: ")
        print(instructors_avail_time)
    

    return return_values

def start():    
    compiled_data=convert()

    # Unpacks
    levels = compiled_data[0]                       # Single list/tuple
    sections = compiled_data[1]                     # Single list/tuple
    instructors_avail_time = compiled_data[2]       # single list/tuple
    parent_subjects = compiled_data[3]              # raw, dict, conv
    parent_buildings = compiled_data[4]             # raw, dict, conv
    parent_floors = compiled_data[5]                # raw, conv
    parent_rooms = compiled_data[6]                 # raw, conv
    parent_instructors = compiled_data[7]           # raw, dict, conv
    parent_instructors_field = compiled_data[8]     # raw, dict, conv

    # restricted area maker thing, format
    restricted = []
    my_list = []
    i = [[],[]]


    for day in range(2):

        my_list = []
        restricted.append(my_list)
        for restricted_list_num in range(6):      # appends the 8 lists correspondent to the 8 available schedules per day

            my_list = []
            restricted[day].append(my_list)
            for floors in range(len(parent_floors[1])): # appends the frs block to each schedule block, x amounts of times (x = how many buildings there are)

                i = [[],[]]
                restricted[day][restricted_list_num].append(i)       
                y=-1

        for restricted_list_num in range(6):    # goes 0 - 7

            a = - 1     
            for x in parent_floors[1]:

                a = a + 1       #im not sure if theres a better way to get the current iteration, but this seems to work jsut fine
                for y in x:

                    my_list = []
                    restricted[day][restricted_list_num][a][1].append(my_list)   #appends the number of rooms per floor in each building block

    chromosome = constrained_randomizer(compiled_data, restricted)

    output(compiled_data, chromosome)

    
    

start()

    

    