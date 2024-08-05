import sys
import random


def info():

    all_info=[]

    levels =        (

                        "g11_steam",
                        "g11_abm"

                    )
    
    all_info.append(levels)


    section =       (
                        17,
                        5
                    )
    
    all_info.append(section)

    subjects = (

                    (
                        "precalc",
                        "genmath",
                        "ucsp",
                        "iphp"
                    ),

                    (
                        "business_math",
                        "accounting",
                        "cpar",
                        "reading&writing"
                    )
                )
    
    all_info.append(subjects)

    buildings =     (

                        "suhs",
                        "guy_hall"

                    )
    
    all_info.append(buildings)

    floors =        (                  # COUNT FROM ZERO, INCLUDE GROUND FLOOR                 
        
                        2,
                        4
        
                    )
    
    all_info.append(floors)

    rooms =         (
        
                        12,
                        20
        
                    )
    
    all_info.append(rooms)

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
                        "0000",
                        "0000",
                        "0000",
                        "0000"
                    ),

                    (
                        "0000",
                        "0000",
                        "0000",
                        "0000"
                    )
                )
    
    all_info.append(instructors_avail_time)



    #all_info = (levels, section, subjects, buildings, floors, rooms, instructors, instructors_field, instructors_available_time)

    return all_info
    

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

    return_values.append(levels)
    return_values.append(sections)
    return_values.append(instructors_avail_time)

                         
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

    return_values_temp.append(raw_subjects)
    return_values_temp.append(dict_subjects)
    return_values_temp.append(subjects)
    return_values.append(return_values_temp)
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

    return_values_temp.append(raw_buildings)
    return_values_temp.append(dict_buildings)
    return_values_temp.append(buildings)
    return_values.append(return_values_temp)
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

                floors.append(floors_temp)

                floors_temp=[]

    
    # appends data from above to return_values_temp, then appends return_values_temp to the final return values

    return_values_temp.append(raw_floors)
    return_values_temp.append(floors)
    return_values.append(return_values_temp)
    return_values_temp=[]

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

    return_values_temp.append(raw_rooms)
    return_values_temp.append(rooms)
    return_values.append(return_values_temp)
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

    return_values_temp.append(raw_instructors)
    return_values_temp.append(dict_instructors)
    return_values_temp.append(instructors)
    return_values.append(return_values_temp)
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

    return_values_temp.append(raw_instructors_field)
    return_values_temp.append(dict_instructors_field)
    return_values_temp.append(instructors_field)
    return_values.append(return_values_temp)
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

  

    

start()

    

    