schedule = None
try:
    schedule = open('schedule.txt', 'r+')

    line = schedule.readlines()
    classes = []
    long = len(line)
    hours = []
    hour = ''
    class_hours = {}
    number = 0

    for el in line:
        x = el.index(':')
        classes.append(el[0:x])

    hours = [0 for i in range(0,long)]

    for i in range(0, long):
        for el in line[i]:
            try:
                number = int(el)
                hour += str(el)
            except ValueError:
                if hour != '':
                    hours[i] += int(hour)
                hour = ''
                continue
        class_hours[i] = [classes[i],hours[i]]

    print(class_hours)
except Exception as e:
    raise (e)
finally:
    schedule.close()


