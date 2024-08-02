
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

        #num_levels = int(input("How many grade levels is present?: "))

        #num_subjects = int(input("How many subjects are there?: "))

        num_buildings = int(input("How many buildings are there?: "))

        #num_classrooms = int(input("How many clasrooms are there?: "))

        #num_sections = int(input("How many sections will there be in a grade level?: "))

        #num_teachers = int(input("How many teachers will be teaching?: "))

        stories_rooms, building_names, building_stories = info_gathering.building_info(num_buildings)


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
            

        



#=======================================

ui.start()


        

