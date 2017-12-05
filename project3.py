#Udit Kaushik
#75825974
#project3.py

import project3_handler
import project3_classes

def user_input():
    """
    Takes the user input for location and wanted instructions.
    """
    input_list = []
    
    n = int(input())
    location_list = []
    
    for i in range(n):
        temp_input = str(input())
        location_list.append(temp_input)

    if len(location_list) != n:
        return 'Input Error'

    else:
        pass

    m = int(input())
    instruction_list = []

    for i in range(m):
        temp_input = str(input())
        instruction_list.append(temp_input)

    if len(instruction_list) != m:
        return 'Input Error'

    else:
        pass

    input_list.append(location_list)
    input_list.append(instruction_list)

    return(input_list)

def elevation_api_list(u_in_list: list) -> list:
    """
    Generates the elevation api for each url and returns them in one list.
    """
    elevation_base_url = 'http://open.mapquestapi.com/elevation/v1'
    elevation_class_key = '/profile?'

    try:
        elevation_url_list = project3_handler.elevation_url(elevation_base_url, u_in_list[0], elevation_class_key)
        if elevation_url_list == 'NO ROUTE FOUND':
            return 'NO ROUTE FOUND'
        else:
            pass
        
        elevation_api_data_list = []
        for url in elevation_url_list:
            elevation_api_data = project3_handler.get_results(url)
            elevation_api_data_list.append(elevation_api_data)
            
        return elevation_api_data_list

    except:
        return

def distance_api_list(u_in_list: list) -> list:
    """
    Generates the distance api and returns it in a list.
    
    *The input is a list type because of the return type of the
    elevation_api_list(). For the sake of duck typing, the input
    must be a list.
    """
    distance_base_url = 'http://open.mapquestapi.com/directions/v2'
    distance_class_key = '/route?'

    try:
        distance_api_data_list = []  
        distance_api_data = project3_handler.get_results(project3_handler.complete_url(distance_base_url, u_in_list[0], distance_class_key))
        distance_api_data_list.append(distance_api_data)

        return distance_api_data_list
    
    except:
        return

def sorter(instruction_list: list) -> list:
    """
    Sorts the output into the wanted list type and returns the instruction
    as a class object in the new ordered list.
    """
    ordered_instruction_list = []

    for instruction in instruction_list:
        if instruction == 'STEPS':
            ordered_instruction_list.append(project3_classes.STEPS())
        elif instruction == 'TOTALDISTANCE':
            ordered_instruction_list.append(project3_classes.TOTALDISTANCE())
        elif instruction == 'TOTALTIME':
            ordered_instruction_list.append(project3_classes.TOTALTIME())
        elif instruction == 'LATLONG':
            ordered_instruction_list.append(project3_classes.LATLONG())
        elif instruction == 'ELEVATION':
            ordered_instruction_list.append(project3_classes.ELEVATION())

    return ordered_instruction_list


def main():
    """
    Calls and runs the program when this module is run.
    """
    user_input_list = user_input()

    if type(user_input_list) == str:
        print(user_input_list)
        return

    else:
        pass
    
    try:
        elevation_api_data_list = elevation_api_list(user_input_list)
        
        if elevation_api_data_list == 'NO ROUTE FOUND':
            """
            Checks whether there is a possible route.
            """
            print()
            print('NO ROUTE FOUND')
            return
            
        elif elevation_api_data_list == None:
            """
            Checks whether there is an error from MapQuest.
            """
            print()
            print('MAPQUEST ERROR')
            return
        else:
            pass
        
        distance_api_data_list = distance_api_list(user_input_list)
        
        if distance_api_data_list == 'NO ROUTE FOUND':
            """
            Checks whether there is a possible route.
            """
            print()
            print('NO ROUTE FOUND')
            return
        
        elif distance_api_data_list == None:
            """
            Checks whether there is an error from MapQuest.
            """
            print()
            print('MAPQUEST ERROR')
            return
        
        else:
            pass

        final_list = sorter(user_input_list[1])

        for instruction in final_list:
            try:
                instruction.output_results(elevation_api_data_list)
            except:
                instruction.output_results(distance_api_data_list)

    except:
        print()
        print('NO ROUTE FOUND')

    

if __name__ == '__main__':
    main()
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
