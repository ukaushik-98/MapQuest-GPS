#Udit Kaushik
#75825974
#project3_classes.py

class STEPS:
    """
    Generates the step by step instruction of the map from the distance
    api list and displays it in a readable fashion.
    """
    def output_results(self, result_list: list) -> None:
        """
        Method of class that is used specifically for duck typing.
        """
        results = result_list[0] #API needed to be stored into a list for the sake of duck typing.
                                 #Since we know there is only one api in the distance_api_list, we
                                 #safely hard code the index value to 0.
        
        direction_list = []

        #Finds and takes the results from the api.
        for i in range(len(results['route']['legs'])):
            for j in range(len(results['route']['legs'][i]['maneuvers'])):
                direction_list.append(results['route']['legs'][i]['maneuvers'][j]['narrative'])

        print()
        print('DIRECTIONS')
        for direction in direction_list:
            print(direction)
            

class TOTALDISTANCE:
    """
    Takes the distance data from the distance api list and
    displays the total distance of the entire trip
    """
    def output_results(self, result_list: list) -> None:
        """
        Method of class that is used specifically for duck typing.
        """
        
        #Finds and takes the results from the api.
        results = result_list[0] #API needed to be stored into a list for the sake of duck typing.
                                 #Since we know there is only one api in the distance_api_list, we
                                 #safely hard code the index value to 0.
        
        distance = results['route']['distance']

        #Prints the results in the desired format.
        print()
        print('TOTAL DISTANCE: {} miles'.format(round(distance)))


class TOTALTIME:
    """
    Takes the distance api from the distance api list and
    displays the total time (in minutes) of the entire trip.
    """
    def output_results(self, result_list: list) -> None:
        """
        Method of class that is used specifically for duck typing.
        """

        #Finds and takes the results from the api.
        results = result_list[0] #API needed to be stored into a list for the sake of duck typing.
                                 #Since we know there is only one api in the distance_api_list, we
                                 #safely hard code the index value to 0.
        
        time = results['route']['time'] / 60 #Time taken in the api is in seconds; must divide by 60 to get minutes.

        #Prints the results in the desired format.
        print()
        print('TOTAL TIME: {} minutes'.format(round(time)))


class LATLONG:
    """
    Takes the latitude and longitude from the api and presents them
    in the desired layout.
    """
    def give_direction(lat_list: list, lng_list: list) -> list:
        """
        Takes the coordinates from the given data and returns them
        with the appropriate direction, i.e. N,S,E,W. Also, if the
        coordinate is negative, returns it as a positive.
        """ 
        final_list = []
        if len(lat_list) == len(lng_list):
            for i in range(len(lat_list)):
                if lat_list[i] > 0:
                    cord = '{:03.2f}N'.format(round(lat_list[i], 2)) #LAT -> NORTH
                    
                elif lat_list[i] < 0:
                    lat_list[i] = -1 * int(lat_list[i]) #Makes the coordinate positive while taking into account the direction.
                    cord = '{:03.2f}S'.format(round(lat_list[i], 2)) #LAT -> SOUTH

                final_list.append(cord)

            for i in range(len(lng_list)):   
                if lng_list[i] > 0:
                    cord = '{:03.2f}E'.format(round(lng_list[i], 2)) #LON -> EAST
                    
                elif lng_list[i] < 0:
                    lng_list[i] = -1 * lng_list[i] #Makes the coordinate positive while taking into account the direction.
                    cord = '{:03.2f}W'.format(round(lng_list[i], 2)) #LON -> WEST

                final_list.append(cord)

            return final_list
            
    def output_results(self, result_list: list) -> None:
        """
        Method of class that is used specifically for duck typing.
        """
        lat_list = []
        lng_list = []
        results = result_list[0] #API needed to be stored into a list for the sake of duck typing.
                                 #Since we know there is only one api in the distance_api_list, we
                                 #safely hard code the index value to 0.

        #Finds and takes the results from the api.
        for i in range(len(results['route']['locations'])):
            lng_list.append(results['route']['locations'][i]['latLng']['lng'])
            lat_list.append(results['route']['locations'][i]['latLng']['lat'])

        final_list = LATLONG.give_direction(lat_list, lng_list)

        #Prints the results in the desired format.
        print()
        print('LATLONGS')
        for i in range(len(lat_list)):
            print('{} {}'.format(final_list[i], final_list[i+len(lat_list)]))

    

class ELEVATION:
    """
    Takes the data from the apis in the api list and prints out the
    elevation for the individual location.
    """
    def output_results(self, result_list: list) -> None:
        """
        Method of class that is used specifically for duck typing.
        """

        #Prints the results in the desired format.
        print()
        print('ELEVATIONS')
        for i in range(len(result_list)): #A loop is used because there are multiple api data in the list (one for each location -> individual elevation).
            print(round(result_list[i]['elevationProfile'][0]['height'])) #Finds and takes the results from the api.

    
