import sys
import random
import os


def info():

    all_info=[]

    levels =        (                                       #CHANGE ME BACK

                        "g11_steam",
                        #"g12_steam"

                    )
    
    all_info.append(levels)


    section =       (
                        45,
                        #19
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
                        "oralcom"
                        "peh",
                        "cffs",


                    ),

                    (
                        "english",
                        "chemistry",
                        "cpar",
                        "filipino"
                        "biology",
                        "inqvest",
                        "physics",
                        "peh",
                        "cffs"
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

    

def fitness ():             #checks fitness level
    
    ideal_num_breaks_morning = 1

    ideal_num_breaks_afternoon = 1

    ideal_sched_start = 1

    ideal_sched_end = 3

    room_distance = 1


    difficulty_0 = ()

    difficulty_1 = ()

    difficulty_2 = ()

    ideal_subject_placement = ("0120","0120")

def constrained_randomizer(compiled_data, restricted):

    compiled_data=convert()
    #print(compiled_data)

    #               UNPACKS THE DATA RETURNED FROM convert()

    # Single list/tuple
    levels = compiled_data[0]
    #print(levels)

    # Single list/tuple
    sections = compiled_data[1]
    #print(sections)

    # single list/tuple
    instructors_avail_time = compiled_data[2]
    #print(instructors_avail_time)

    # raw, dict, conv
    parent_subjects = compiled_data[3]
    #print(parent_subjects)
    
    # raw, dict, conv
    parent_buildings = compiled_data[4]
    #print(parent_buildings)

    # raw, conv
    parent_floors = compiled_data[5]
    #print(parent_floors)

    # raw, conv
    parent_rooms = compiled_data[6]
    #print(parent_rooms)

    # raw, dict, conv
    parent_instructors = compiled_data[7]
    #print(parent_instructors)

    # raw, dict, conv
    parent_instructors_field = compiled_data[8]
    #print(parent_instructors_field)


    chromosome = []



    for level in range(len(levels)):

        for section in range(sections[level]):

            chromosome.append(level)

            # no 1st segment yet make this NOW!

            schedule_conditions = 0

            '''      This code snippet is dumb, but il keep it here
                        

            # creates randomized binary thing for schedule, keeps repeating until the amount of 1s reaches the minimum number (number of subjects)

            num_subjects = len(parent_subjects[0][level])+1

            component_schedule = rand_schedule(num_subjects)

            chromosome.append(component_schedule)
                
            #print(component_schedule)
            '''


            # creates the randomized subject schedule

            num_subjects = len(parent_subjects[0][level])+1

            conv_subjects = parent_subjects[2][level]

            component_subject, ignore_list = rand_subjects_schedule(num_subjects)

            chromosome.append(component_subject)

            #print(component_subject)


            # gets the randomized building, floors, and rooms values

            num_buildings = len(parent_buildings[0])-1

            #print(num_buildings)
            
            address_module, error=buildings_floors_rooms(num_buildings,parent_floors,parent_rooms, restricted, ignore_list )

            if error:

                print("error_01")
                exit()
   
    pass
           
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
            if debug:
                os.system('cls')
                print(restricted)
                print()
                print(day)
                print(x)
                print(ignore_list)
                print(address_module)

    return address_module, error

def rand_subjects_schedule(num_subjects):            # this function turned out more complex than expected

    component_subject_temp = []

    component_subject = []

    temp = []

    num_subjects_list = []

    # turns the num of subjects into a list

    for x in range(num_subjects):
        num_subjects_list.append(x)

    # removes the 0 from the newly made list, (0 is intended for no subjects)

    num_subjects_list = num_subjects_list[1:]

    # random sample thing for the arrangement of subjects

    temp = random.sample(num_subjects_list, num_subjects-1)

    # takes the center of the num of subjects

    half = num_subjects // 2

    # random number thing (will make sense later)

    random_half = random.randint(0,1)

    # splits the subject schedule for the 2 days of class

    first_half = temp[:half]

    second_half = temp[half:]
    
    # subtracts how many subjects per day to the available time in the schedule (8)

    first_half_blank = 6 - len(first_half)

    second_half_blank = 6 - len(second_half)

    # adds the blank subjects to fill it up

    for x in range(first_half_blank):

        temp = random.randint(0,len(first_half))

        first_half.insert(temp, 0)

    for x in range(second_half_blank):

        temp = random.randint(0,len(first_half))

        second_half.insert(temp, 0)

    first_half = tuple(first_half)

    second_half = tuple(second_half)

    # uses the random number generated to determine the order of the halves (in odd number cases, the bigger number will always be last, this is to prevent that)

    if random_half == 0:

        component_subject_temp = first_half, second_half

    else:

        component_subject_temp = second_half, first_half


    #turns the stuff into a tuple (apparently tuples are more efficient, but i dont know if its less efficient to convert them, or leave them as lists)

    for tuple_elem in component_subject_temp:

        temp = []
        
        for int_elem in tuple_elem:

            str_elem = str(int_elem).zfill(2)

            temp.append(str_elem)

        temp_2 = tuple(temp)

        component_subject.append(temp_2)


    ignore_list = []

    for x in range(2):

        ignore_list.append([])

        for y in range(6):

            ignore = "00" in component_subject[x][y]

            if ignore:
                ignore_list[x].append(y)
        
        ignore_list[x] = tuple(ignore_list[x])
        
    ignore_list = tuple(ignore_list)
    
    print(component_subject)

    return component_subject, ignore_list

def rand_schedule(num_subjects):        # currently serves no purpose (will indefinetly stay with no purpose)

    schedule_conditions = 0

    component_schedule = []


    while schedule_conditions != num_subjects:

        component_schedule=[]

        for _ in range(4):

            for _ in range(4):

                component_schedule.append(random.randint(0,1))

        schedule_conditions = component_schedule.count(1)

    component_schedule = tuple()

    return component_schedule
        
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
    #print(compiled_data)

    #               UNPACKS THE DATA RETURNED FROM convert()

    # Single list/tuple
    levels = compiled_data[0]
    #print(levels)

    # Single list/tuple
    sections = compiled_data[1]
    #print(sections)

    # single list/tuple
    instructors_avail_time = compiled_data[2]
    #print(instructors_avail_time)

    # raw, dict, conv
    parent_subjects = compiled_data[3]
    #print(parent_subjects)
    
    # raw, dict, conv
    parent_buildings = compiled_data[4]
    #print(parent_buildings)

    # raw, conv
    parent_floors = compiled_data[5]
    #print(parent_floors)

    # raw, conv
    parent_rooms = compiled_data[6]
    #print(parent_rooms)

    # raw, dict, conv
    parent_instructors = compiled_data[7]
    #print(parent_instructors)

    # raw, dict, conv
    parent_instructors_field = compiled_data[8]
    #print(parent_instructors_field)

    #  you should turn this into a function soon 

   


    # restricted area maker thing, format:  []   [ [[floor], [room], building 1], [[floor], [room], building 2]  ], [repeat]   ]
    #                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #                                             one schedule module (for lack of a better term) repeat 8 times

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

 

    constrained_randomizer(compiled_data, restricted)

    
    

start()

    

    