#####################################
# Task 1 : Abstract Data Type (ADT) #  (20 marks)
#####################################


#######################
# Task 1a : Train ADT #  (1 marks)
#######################

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)

test_train1 = make_train('TRAIN 0-0')
test_train2 = make_train('TRAIN 1-2')
test_train3 = make_train('TRAIN 0-9')


def get_train_code(train):      #  (1 marks)
    # Write your code here
    pass

   
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
##print("## Task 1a ##")
##print('The tuple containing the train code : ', test_train1)  # ('TRAIN 0-0',)
##print('Train Code : ', get_train_code(test_train1))           #  'TRAIN 0-0'




#########################
# Task 1b : Station ADT #  (2 marks)
#########################

def make_station(station_code, station_name):
    ''' Do NOT modify this function'''
    return (station_code, station_name)

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


def get_station_code(station):        #  (1 marks)
    # Write your code here
    pass


def get_station_name(station):        #  (1 marks)
    # Write your code here
    pass



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
##print("## Task 1b ##")
##print('The tuple containing the station info : ', test_station1)  # ('CC2', 'Bras Basah')
##print('Station Code : ', get_station_code(test_station1))         # CC2
##print('Station Name : ', get_station_name(test_station1))         # Bras Basah




###########################
# Task 1c : MRT Line ADT  #  (7 marks)
###########################

def make_line(name, stations):                  #  (1 marks)
    # Write your code here
    pass

    
def get_line_name(line):                        #  (1 marks)
    # Write your code here
    pass


def get_line_stations(line):                    #  (1 marks)
    # Write your code here
    pass


def get_station_by_name(line, station_name):    #  (2 marks)
    # Write your code here
    pass 


def get_station_by_code(line, code):            #  (2 marks)
    # Write your code here
    pass


test_line = make_line('Circle Line', (test_station1, test_station2, test_station3))

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
##print("## Task 1c ##")
##print('The tuple containing the station info : ',test_line)                              # ('Circle Line', (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade')))
##print('Name of MRT Line : ',get_line_name(test_line))                                    # 'Circle Line'
##print('All the Stations in the LINE : ',get_line_stations(test_line))                    #(('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
##print("Station Info for 'Bras Basah' : ",get_station_by_name(test_line, 'Bras Basah'))   #('CC2', 'Bras Basah')
##print("Station Info for 'CC4' : ",get_station_by_code(test_line, 'CC4'))                 #('CC4', 'Promenade')

# Students should study the tuple 'test_line' carefully. 

def print_line(line):
    print()
    print('Details about the Line:')
    for ele in line:
        if type(ele) == tuple:
            for term in ele:
                print('*    ', term)
        else:
            print(ele)
    print()

##print_line(test_line)
##UNCOMMENT THE ABOVE TO GET THE FOLLOWING PRINT OUTPUT : 
'''
Details about the Line:
Circle Line
*     ('CC2', 'Bras Basah')
*     ('CC3', 'Esplanade')
*     ('CC4', 'Promenade')
'''



#################################
# Task 1d : Train_Position ADT  #  (6 marks)
#################################

def make_train_position(is_moving, from_station, to_station):
    ''' Do NOT modify this function'''
    return (is_moving, from_station, to_station)

test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)

def get_is_moving(train_position):                  #  (1 marks)
    # Write your code here
    pass


def get_previous_station(train_position):           #  (1 marks)
    # Write your code here
    pass


def get_next_station(train_position):               #  (1 marks)
    # Write your code here
    pass

 
def get_stopped_station(train_position):            #  (1 marks)
    # Write your code here
    pass


def get_direction(line, train_position):            #  (2 marks)
    # Write your code here
    pass



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
##print("## Task 1d ##")
##print(get_is_moving(test_train_position2))              # True
##print(get_stopped_station(test_train_position1))        #('CC2', 'Bras Basah')
##print(get_previous_station(test_train_position2))       #('CC4', 'Promenade')
##print(get_next_station(test_train_position2))           #('CC3', 'Esplanade')
##print(get_direction(test_line, test_train_position1))   # 0
##print(get_direction(test_line, test_train_position2))   # 1


########################
# Task 1e : Event ADT  #  (4 marks)
########################

from datetime import *

def make_event(train, train_position, time):
    # Write your code here
    pass


test_event1 = make_event(test_train1, test_train_position1, datetime(2016, 1, 1, 9, 27))
test_event2 = make_event(test_train2, test_train_position2, datetime(2016, 1, 1, 2, 25))


def get_train(event):
    # Write your code here
    pass


def get_train_position(event):
    # Write your code here
    pass


def get_event_time(event):
    # Write your code here
    pass



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1E
##print("## Task 1e ##")
##print(get_train(test_event1))             #('TRAIN 0-0',)
##print(get_train_position(test_event2))    #(True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
##print(get_event_time(test_event1))        #'2016-01-01 09:27:00'





######################################
## Task 2 : Data Parsing a CSV file ##  (12 marks)
######################################

import csv
def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

station_file = read_csv("station_info.csv")

# UNCOMMENT THE CODE BELOW TO PRINT THE STATION FILE 
##print(station_file)
##print(station_file[:10])

'''
(('station_code', 'station_name', 'line_name'), ('NS1', 'Jurong East', 'North
South Line'), ('NS2', 'Bukit Batok', 'North South Line'), ('NS3', 'Bukit Gombak',
'North South Line'), ('NS4', 'Choa Chu Kang', 'North South Line'), ('NS5', 'Yew
Tee', 'North South Line'), ('NS7', 'Kranji', 'North South Line'), ('NS8',
'Marsiling', 'North South Line'), ('NS9', 'Woodlands', 'North South Line'),
('NS10', 'Admiralty', 'North South Line'))
'''

#############################################
# Task 2a : Print details in Stations file  #  (1 mark)
#############################################


def print_station_details(tup):
    # Write your code here
    pass


# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A.
##print_station_details(station_file)
##print_station_details(station_file[:10])

'''

('station_code', 'station_name', 'line_name')
('NS1', 'Jurong East', 'North South Line')
('NS2', 'Bukit Batok', 'North South Line')
('NS3', 'Bukit Gombak', 'North South Line')
('NS4', 'Choa Chu Kang', 'North South Line')
('NS5', 'Yew Tee', 'North South Line')
('NS7', 'Kranji', 'North South Line')
('NS8', 'Marsiling', 'North South Line')
('NS9', 'Woodlands', 'North South Line')
('NS10', 'Admiralty', 'North South Line')

'''


#########################################
# Task 2b : Extract Stations on a Line  # (4 marks)
#########################################

def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            # Addition #1
            pass
        else:
            # Addition #2
            pass
    # Addition #3
    return lines


LINES = parse_lines('station_info.csv')

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
##print("## Task 2B ##")
##print(LINES)



#########################################
# Task 2c : Extract Stations on a Line  # (2 marks)
#########################################


def filter_line(line_name, all_lines):
    # Write your code here
    pass

        

CCL = filter_line('Circle Line', LINES) 

##print(CCL[0])
##print(get_line_stations(CCL)[5:8])

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2C
##print("## Task 2c ##")
##print(get_line_stations(CCL)[5:8])#==(('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota')))

    


##########################################
# Task 2d : Extracting Breakdown Events  # (5 marks)
##########################################

from datetime import *

def parse_events(data_file):
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        # Your code here
        pass
    return events


# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2D. THIS IS NOT OPTIONAL TESTING!
# BD_EVENTS = parse_events('breakdown_events.csv')

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2D
##print("## Task 2d ##")
##print(BD_EVENTS[9])

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))


##print(BD_EVENTS[27])

# Expected Output #
# (('TRAIN 0-8',), (False, ('CC25', 'Haw Par Villa'), ('CC26', 'Pasir Panjang')), datetime.datetime(2017, 1, 6, 9, 33))




def print_event(file):
    for ele in file:
        print(ele[0][0])
        if type(ele) == tuple:
            for term in ele[1:]:
                print('*    ', term)
        else:
            print(ele)
        print()

##print_event(BD_EVENTS)
'''
TRAIN 1-6
*     (False, ('CC17', 'Caldecott'), ('CC16', 'Marymount'))
*     2017-01-06 23:13:00

TRAIN 1-7
*     (True, ('CC20', 'Farrer Road'), ('CC19', 'Botanic Gardens'))
*     2017-01-06 23:14:00

TRAIN 1-7
*     (False, ('CC19', 'Botanic Gardens'), ('CC17', 'Caldecott'))
*     2017-01-06 23:14:00
'''




##############################################
# Task 3a : Data Cleaning - Breakdown Events # (5 marks)
##############################################


def is_valid(bd_event):
    '''your code here'''
    pass


test_bd_event1 = make_event(test_train1, test_train_position2, datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_event(test_train1, test_train_position1, datetime(2016, 1, 1, 2, 25))

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
##print("## Task 3a ##")
##print(test_bd_event1)
##print(is_valid(test_bd_event1))   # True
##print(is_valid(test_bd_event2))   # False


def filter(pred, seq):
    ''' Do NOT modify this function'''
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

   
def get_valid_events(bd_events):
    ''' Do NOT modify this function'''
    return filter(is_valid, bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
# VALID_BD_EVENTS = filter(is_valid, BD_EVENTS)


##########################################
# Task 3b : Examine the Breakdown Events # (1 marks)
##########################################

# Use the print_event function to display the Breakdown Events :
'''
TRAIN 1-1
*     ('True', ('CC13', 'Serangoon'), ('CC12', 'Bartley'))
*     2017-01-06 06:44:00

TRAIN 1-3
*     ('True', ('CC15', 'Bishan'), ('CC14', 'Lorong Chuan'))
*     2017-01-06 06:49:00

TRAIN 1-5
*     ('True', ('CC17', 'Caldecott'), ('CC16', 'Marymount'))
*     2017-01-06 06:54:00

TRAIN 1-6
*     ('True', ('CC19', 'Botanic Gardens'), ('CC17', 'Caldecott'))
*     2017-01-06 06:56:00

TRAIN 1-6
*     ('True', ('CC19', 'Botanic Gardens'), ('CC17', 'Caldecott'))
*     2017-01-06 06:57:00
'''

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
##print("## Task 3b ##")
##print(VALID_BD_EVENTS)
##print_event(VALID_BD_EVENTS)
##print_event(VALID_BD_EVENTS[:5])



#############################
## Task 4 : Data Filtering ## (2 marks)
#############################

# UNCOMMENT the following to read the entire train schedule
# (This will take some time to run)
# FULL_SCHEDULE = parse_events('train_schedule.csv')    

###########
# Task 4a #
###########

def get_schedules_at_time(train_schedule, time):
    '''your code here'''
    pass



test_datetime = datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
##print("## Task 4a ##")
##print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))


###########
# Task 4b # (Omitted)
###########

def get_schedules_near_loc_id(train_schedule, loc_id):
    '''your code here'''
    pass


###########
# Task 4c # (Omitted)
###########

def get_rogue_schedules(train_schedule, time, loc_id):
    '''your code here'''
    pass


###################################
## Task 5 : Find the Rogue Train ## (To be continue ...)
###################################




