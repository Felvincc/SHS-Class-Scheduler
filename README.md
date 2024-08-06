# class schedule thing

ignore main.py im using algorithm.py now

scratch the genetic algorithm, that just isnt the right solution for this. Using some kind of elitist constrained random population thing

















main premise is,

This will automatically create class schedules for any number of classes, classrooms, teachers, subjects.

there will also be conditions you can set for the classes, teachers, subjects, and maybe sometimes rooms
wherein when theres a specific condition of one of the students, such as health conditions, the algorithm will try its best
to make sure the class where the student belongs will not encounter as many stairs or rooms in other floors.

num_levels

num_subjects 

num_buildings 

num_classrooms 

num_sections 



num_teachers 



important stuff things:







how many levels there are (ex. grade 11, 12) and their respective subjects

teachers that may have conditions (ex. health stuff[same as student thing])

what subjects the teachers teach

Available time the teacher has for teaching (taking into account teachers that also teach from other departments)

subjects that require a specific learning environment



time alloted for these subjects

stories, rooms per story, building name of buildings

classroom environments (ex. has_tv, comp_lab, chem_lab), and where they are located

class sections and any notable conditions of students (ex. health problems that prohibit them from climbing many flights of stairs)


genetic algorithm stuff:

fitness indicators:

    how many breaks in a day

    when the breaks are in a day

    how early/late schedule starts

    how early/late schedule ends

    how far the rooms are from each other


chromosome define thing:

    5 digit choromosome

    1st digit: how many breaks per day int(0-3) 

    2nd digit: when the breaks are int(0,1) (0 - morning, 1 - afternoon)

    3rd digit: when schedule starts int(0,1,2,3) (0 - 7am, 1 - 8am, 2 - 9am, 3 - 10am)

    4th digit: when schedule starts int(0,1,2) (0-5pm, 1-4pm, 2-3pm)

    5th digit: how farm rooms are int(0,1,2,3) ( 0-1st, 1-2nd, 2-3rd, 3 - separate building)
















 
