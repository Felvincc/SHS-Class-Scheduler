
import sys

class create:

    def section(x):

        pass

    def classroom():

        pass

    def teacher():

        pass

    def subject():

        pass

    def building():

        pass

    def level():

        pass

class declare: #currently unused, might delete later
    
    def building_floors(a):
        
        return "building_"+str(a)
    
class ui():

    def start():
        info_gathering.general()

class info_gathering: # i am unsure if system is the best name for this class...
        
    def general():

        num_levels = int(input("How many grade levels is present?: "))

        num_teachers = int(input("How many teachers will teach?"))



        

        #num_buildings = int(input("How many buildings are there?: "))



        
        #grade_levels, subjects, subject_time, subject_classroom_environments = 
        info_gathering.grade_level_info(num_levels, num_teachers)


        #stories_rooms, building_names, building_stories = info_gathering.building_info(num_buildings)


    def building_info(num_buildings):                                                                   # This function clarifies and compiles the information of the building

        a=0  
        stories_rooms=[]
        building_names=[]
        building_stories=[]
        stories_rooms_temp2=[]


        for x in range(num_buildings):                                                                  
            
            a+=1                                                                                        # used to track the building numbers (incremented by 1 so the users brain doesnt explode)

            building_name_temp=str(input("Enter a name for building "+str(a)+": " ))                    #gets name of building(s), and stores it in a temp var

            building_stories_temp=int(input("Enter How many floors there are in this building: "))      #gets how many floors are in the building, stores it in a temp var


            for x in range(building_stories_temp):                                                      # Gets the list of rooms per floor, names of the buildings, the number of stories in each building, respectively.
                    
                stories_rooms_temp=int(input("How many rooms are in the "+str(x+1)+" floor: "))         # gets temp input of how many rooms in each floor(x+1) 

                stories_rooms_temp2.append(stories_rooms_temp)                                          # appends temp input to a temp list (for keeping the values, after an iteration in the for loop)

                if x == building_stories_temp-1:                                                        # checks if the for loop is about to end

                    stories_rooms.append(stories_rooms_temp2)                                           # appends the list to the final rooms per story variable so that it will not be affected in the parent for loop iteration

                    stories_rooms_temp2=[]                                                              # resets the temp

                else:

                    pass
                    
            building_names.append(building_name_temp)                                                   # appends to the final building names, and stories variable
            building_stories.append(building_stories_temp)

            print(stories_rooms)
            print(building_names)
            print(building_stories)
            
        return stories_rooms, building_names, building_stories
            
    def grade_level_info(num_levels, num_teachers):

        name_teachers=[]
        level_name=[]
        num_subjects=[]
        name_subjects=[]
        level_subjects=[]

        level_subjects_temp2=[]
        a=0
        b=-1
        
        for x in range(num_teachers):                                                                   # fetches name of teacher, and places it in a list in order

            name_teachers_temp = str(input("Name of teacher " + str(x+1) + ": "))
            name_teachers.append(name_teachers_temp)

        for x in range(num_levels):                                                                     # fetches name of level
            level_name_temp=input( "Name of level " + str(x+1) + ": ")
            level_name.append(level_name_temp)

        for x in range(num_levels):                                                                     # fetches how many subjects are per levels

            subjects_temp=int(input("How many subjects are present in "+ level_name[x]+": " ))          
            num_subjects.append(subjects_temp)

        for num_subjects_temp in num_subjects:                                                          # fetches the name of the subjects per level (quite annoying to make)
            a+=1
            b+=1
            for x in range(num_subjects_temp):

                level_subjects_temp = input(level_name[b]+": What is the name of subject "+str(a)+": ") 
                level_subjects_temp2.append(level_subjects_temp)

            if x == num_subjects_temp-1:
                
                level_subjects.append(level_subjects_temp2)
                level_subjects_temp2=[]
                a=0

            else:
                pass
        
        print(level_subjects)








                







        



#=======================================

ui.start()


        

