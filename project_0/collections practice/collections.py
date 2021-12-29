from collections import Counter
from collections import defaultdict
from collections import deque
from collections import OrderedDict

# cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
# cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

# counter_moscow = Counter(cars_moscow)
# counter_spb = Counter(cars_spb)

# print(counter_moscow)
# print(counter_spb)
# print(counter_moscow + counter_spb)

# print(list(counter_moscow))
# print(dict(counter_moscow))
# print(counter_moscow.most_common(2))

# students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
#             ('Nikitina',2),('Markov',3),('Pavlov',2)]

# groups = defaultdict(list)
# for student, group in students:
#     groups[group].append(student)
    
# print(groups)
# print(groups[3])
# print(groups[2021])
# print(groups)

# clients = deque()
# clients.append('Ivanov')
# clients.append('Petrov')
# clients.append('Smirnov')
# clients.append('Tikhonova')
# print(clients)

# def brackets(line):
#     status_bracks = None
#     bracks = deque()
#     for el in line: 
#         if el == '(':
#             bracks.append(el)
#         elif el == ')':
#             if '(' in bracks: 
#                 bracks.pop()
#             else:
#                 bracks.append(el)
#     if '(' in bracks or ')' in bracks:
#         status_bracks = False
#     else: 
#         status_bracks = True
#     return status_bracks
            
            
# print(brackets("(()())"))
# # True
# print(brackets(""))
# # True
# print(brackets("(()()))"))
# # False


def task_manager(tasks):
    task_dict = defaultdict(deque)
    for task_num, server_name, prioroty in tasks:
        if prioroty: 
            task_dict[server_name].appendleft(task_num)
        else:
            task_dict[server_name].append(task_num)
                    
    return task_dict

tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))

    






 
 


