def make_record(xname,xid,xclass,xaddress):
    student = {}
    student['name'] = xname
    student['nric'] = xid
    student['class'] = xclass
    student['address'] = xaddress
    return student

def get_name(student):
    return student['name']
        
def get_class(student):
    if student['class'] == '':
        return 'No class info.'
    else:
        return student['class']
    
def get_address(student):
    if student['address'] == '':
        return 'No address info.'
    else:
        return student['address']

def set_class(student):
    nric = input('Enter your NRIC : ')
    if student['nric'] == nric:
        newclass = input('Input the new class: ')
        student['class'] = newclass
        #return student
    else:
        print('Invalid NRIC')

def set_address(student):
    nric = input('Enter your NRIC : ')
    if student['nric'] == nric:
        newaddress = input('Input the new address: ')
        student['address'] = newaddress
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

