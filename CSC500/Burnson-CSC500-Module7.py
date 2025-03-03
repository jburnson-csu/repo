# John Burnson
# CSC500
# Module 7

print()

# Definitions
import datetime

keys_course = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]
values_inst = ["Haynes", "Alvarado", "Rich", "Burke", "Lee"]
values_room = ["3004", "4501", "6755", "1244", "1411"]
values_time = [datetime.datetime(2025,1,1,8,0,0), datetime.datetime(2025,1,1,9,0,0), datetime.datetime(2025,1,1,10,0,0), datetime.datetime(2025,1,1,11,0,0), datetime.datetime(2025,1,1,13,0,0)]

# https://stackoverflow.com/questions/423379/how-to-use-a-global-variable-in-a-function
# Python assumes that any name that is assigned to, anywhere within a function, is local to that function unless explicitly told otherwise.
# https://docs.python.org/3/faq/programming.html#what-are-the-rules-for-local-and-global-variables-in-python

def set_up_all_dictionaries():
    # https://stackoverflow.com/questions/20153512/read-and-reassign-a-global-dictionary-within-a-function
    # Before it is ever executed, Python analyzes the entire function body to figure out what variables are local and which are global.
    global course_dict_instruct, course_dict_meetroom, course_dict_meettime
    course_dict_instruct = dict([(k, v) for k, v in zip(keys_course, values_inst)])
    course_dict_meetroom = dict([(k, v) for k, v in zip(keys_course, values_room)])
    course_dict_meettime = dict([(k, v) for k, v in zip(keys_course, values_time)])

def get_course_info():
    return input("Enter your course number: ")

def print_course_info(in_course_number: str, in_course_instructor: str, in_course_meettime: datetime, in_course_meetroom: str) -> str:
    if in_course_instructor=='<missing>' and in_course_meettime=='<missing>' and in_course_meetroom=='<missing>':
      return False
    else:
      print("Course ",in_course_number," is taught by Prof. ",in_course_instructor, sep="",end="")
      print(" and meets in Rm ",in_course_meetroom, sep="",end="")
      try:
        print(" at ",in_course_meettime.strftime("%I:%M %p").lstrip("0"),".", sep="")
      except (IndexError, AttributeError):
        print(" at <missing>.")
      return True

def main():
    #print("\n*** Main Start ***")

    set_up_all_dictionaries()
    in_course_number = get_course_info()
    print()

    # https://www.geeksforgeeks.org/handling-missing-keys-python-dictionaries/
    found_course = print_course_info(in_course_number, course_dict_instruct.get(in_course_number,'<missing>'), course_dict_meettime.get(in_course_number,'<missing>'), course_dict_meetroom.get(in_course_number,'<missing>'))
    if not found_course:
      print("I have no information whatsoever about such a course")

    #print("*** Main End ***")

if __name__ != '__main__':
    print("This program is being imported from another module, so do not run main().")
else:
    #print("This program is being executed as __main__")
    main()

