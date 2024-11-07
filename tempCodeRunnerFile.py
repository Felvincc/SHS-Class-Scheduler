
def predetermined_info():

    all_info=[]

    levels =        (                                

                        "G11 STEAM",
                        "G12 STEAM",
                        "G11 ABM",
                        "G12 ABM",
                        
                  
                    )
    
    all_info.append(levels)


    section =       (
                        15,
                        15,
                        15,
                        15,
                        
                    
                    )
    
    all_info.append(section)

    subjects = (                                 

                    (
                        "Pre-calculus S11",
                        "Statistics S11",
                        "UCSP S11",
                        "IPHP S11",
                        "Earth Science S11",
                        "Emptech S11",
                        "Oral Com S11",
                        "PE/CFFS S11"
                    ),

                    (
                        "English S12",
                        "Chemistry S12",
                        "CPAR S12",
                        "Filipino S12",
                        "Biology S12",
                        "InqVest S12",
                        "Physics S12",
                        "PEH/CFFS S12",
                    ),

                    (
                        "RWS A11",
                        "Business Math A11",
                        "Entrep A11",
                        "UCSP A11",
                        "Gen Math A11",
                        "PE/CFFS A11",
                        "CPAR A11",
                        "Medil A11",
                        "Org and Manage A11"
                        "Earth Science A11"
                    ),

                    (
                        "Personal Dev A12",
                        "Applied Economics A12",
                        "RDL A12",
                        "Business Finance A12",
                        "Pagbasa A12",
                        "Profesional English A12",
                        "FABM A12",
                        "PE/CFFS A12"
                    ),

     

                )
    
    all_info.append(subjects)

    buildings =     (

                        "SUHS",
                        "Guy Hall"
                        
                         

                    )
    
    all_info.append(buildings)

    floors =        (                  # COUNT FROM one)         
        
                        3,
                        3
                        
        
                    )
    
    all_info.append(floors)

    rooms =         (           #count from 1
        
                        12,
                        12
                        
        
                    )
    
    all_info.append(rooms)

    #                   Make exceptions list for rooms that are not able to be used (ex. faculty rooms)

    restricted_address =   (

                        (0, 1, [1,2,3]),
                        (1, 1, [6]),

                    )
    
    all_info.append(restricted_address)
    
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

def output(compiled_data, chromosome, schedule_counter):