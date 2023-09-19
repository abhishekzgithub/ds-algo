"""
1234 — One thousand two hundred thirty four
always four digit

"""
def first_second_place(num):
    if num==0:
        return None
    name_dict={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four"
    }
    return name_dict[num]

def third_place(num2):
    if num2==0:# or num1==0:
        return None

    name_dict={
        2:"twenty",
        3:"thirty",
        4:"fourty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
    }
    return name_dict[num2]

def last_place(num):
    if num==0:
        return None
    name_dict={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four"
    }
    return name_dict[num]

def convert_to_string(nums):
    thousandth=0
    hundredth=0
    tens=0
    ones=0
    name_dict={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four"
    }
    thousandth =nums//1000
    hundredth=(nums//100)%10
    tens =(nums//10)%10
    ones=nums%10
    first=first_second_place(thousandth)
    resultant_str=""
    if first==0:
        return None
    else:
        resultant_str+=first+" thousand "
    second = first_second_place(hundredth)
    if second==None:
        pass
    else:
        resultant_str+=second +" hundred "
    third=third_place(tens)
    if third==None:
        pass
    else:
        resultant_str+=third+" "
    fourth=last_place(ones)
    if fourth==None:
        pass
    else:
        resultant_str+=fourth
    return resultant_str

print(convert_to_string(nums=1234))
print(convert_to_string(nums=4321))
print(convert_to_string(nums=1000))
print(convert_to_string(nums=1001))
print(convert_to_string(nums=3333))

"""

row 
"""