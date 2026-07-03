def make_record(xname,xid,xclass,xaddress):
    return [xname,xid,xclass,xaddress]
            
def get_name(student):
    return student[0]

def get_class(student):
    if student[2] == '':
        return 'No class info.'
    else:
        return student[2]
            
def get_address(student):
    if student[3] == '':
        return 'No address info.'
    else:
        return student[3]

def set_class(student):
    nric = input('Enter your NRIC : ')
    if student[1] == nric:
        newclass = input('Input the new class: ')
        student[2] = newclass
        #return student
    else:
        print('Invalid NRIC')

def set_address(student):
    nric = input('Enter your NRIC : ')
    if student[1] == nric:
        newaddress = input('Input the new address: ')
        student[3] = newaddress
        #return student
    else:
        print('Invalid NRIC')


def print_info(student):
    print()
    print('Name :', get_name(student))
    print('Class :', get_class(student))
    print('Address :', get_address(student))
    print()
        
def print_datatype(student):
    print()
    return type(student)




