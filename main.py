
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

class declare:
    
    def building_floors(a):
        
        return "building_"+str(a)

class system: # i am unsure if system is the best name for this class...
        
    def info_gathering():
        num_buildings_list = list()
        a=0
        b=0

        #num_levels = int(input("How many grade levels is present?: "))

        num_buildings = int(input("How many buildings are there?: "))

        #num_classrooms = int(input("How many clasrooms are there?: "))

        #num_sections = int(input("How many sections will there be in a grade level?: "))

        #num_subjects = int(input("How many subjects are there?: "))

        #num_teachers = int(input("How many teachers will be teaching?: "))

        
        for x in range(num_buildings): # Makes a dictionary for the buildings (building_1, building_2...) these values will be assigned a value based on how many floors the building has.
            a+=1
            building_name_temp = declare.building_floors(a)
            dict_buildings=dict()
            dict_buildings[building_name_temp] = "num_floors_temp"

            print(dict_buildings)

        building_name_temp=None

        for x in range(num_buildings): # take input for names for the buildings, and matches it with the blah blah blah you get the point
            b+=1
            building_name_temp = declare.building_floors(b)
            building_name_input_temp = str(input("\n\nRename Building_"+str(b)+": "))
            dict_buildings[building_name_temp]=building_name_input_temp

        print(dict_buildings)

            

            





        exit()

        num_building_floors = int(input("How many floors are there in building(s)"))



class ui():

    def start():
        system.info_gathering()


ui.start()


        

