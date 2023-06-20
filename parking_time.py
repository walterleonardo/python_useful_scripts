"""
Pa"""


def solution(E, L):
    # Implement your solution here
    if ':' not in E:
        return False
    if ':' not in L:
        return False

    entry = E.split(':')
    leave = L.split(':')
    if len(entry) < 2:
        print("No correct format")
        return False
    if len(leave) < 2:
        print("No correct format")
        return False  
    entry_hours = int(entry[0])
    leave_hours = int(leave[0])    
    entry_minutes =  int(entry[1])
    leave_minutes =  int(leave[1])

    if leave_hours < entry_hours:
        print("la hora de salida es anterior a la de entrada")
        return False
    if leave_hours == entry_hours and leave_minutes < entry_minutes:
        print("los minutos de salida son anteriores a la entrada en la misma hora")
        return False
    hours = leave_hours - entry_hours
    minutes = 0
    minutes = leave_minutes - entry_minutes
    if minutes >= 60:
        minutes -= 60
        hours += 1

    total_minutes = hours * 60 + minutes
    hour_to_pay = total_minutes // 60 

    if minutes == 0:
        hour_to_pay_4 = hour_to_pay - 1 
    else:
        hour_to_pay_4 = hour_to_pay 
    return 2 + 3 + (4 * hour_to_pay_4)


print(solution("10:00","13:21"))
print("###################")
print(solution("9:42","11:42"))
print("###################")
print(solution("12:00","13:00"))
print(solution("12:00","12:10"))
print(solution("12:00","12:59"))
print(solution("12:33","13:32"))