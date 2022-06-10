from random import randint
from dataclasses import dataclass, field


@dataclass
class Schedule:
    days_available: [(int, int)] = field(default_factory=list)
    used_slots: [[(str, int, int, int)]] = field(default_factory=list)


def day_to_string(day: int):
    if day == 0:
        return 'Mo'
    elif day == 1:
        return 'Tu'
    elif day == 2:
        return 'We'
    elif day == 3:
        return 'Th'
    elif day == 4:
        return 'Fr'


def slot_intersection(slot_a: (int, int), slot_b: (int, int)):
    earlier = slot_a
    later = slot_b
    if later[0] < earlier[0]:
        buffer = earlier
        earlier = later
        later = buffer
    result = (max(earlier[0], later[0]), min(earlier[1], later[1]))
    if result[0] >= result[1]:
        return None
    else:
        return result


def main():
    coaches = [
        ('Brooke Stevenson', Schedule()),
        ('Homer Phillips', Schedule()),
    ]
    students = [
        ('Steve Huang', []),
        ('John Duke', []),
        ('Mohammad Carey', []),
        ('Catherine Rasmussen', []),
        ('Aimee Wilkerson', []),
        ('Alexandra Dickerson', []),
        ('Rory Rios', []),
        ('Ofelia Davila', []),
        ('Scottie Herman', []),
        ('Dino Potter', []),
        ('Joel Charles', []),
        ('Hoyt Mckinney', []),
        ('Anibal Moon', []),
        ('Damien Villa', []),
        ('Orlando Roy', []),
        ('Liz Hoover', []),
        ('Julianne Austin', []),
        ('Milford Willis', []),
        ('Julia Tanner', []),
        ('Rhea Mann', []),
    ]
    for coach in coaches:
        for i in range(0, 5):
            coach[1].days_available.append((8, 16))
    for student in students:
        for i in range(0, 5):
            start = randint(8, 14)
            end = start + randint(1, 4)
            day = (start, end)
            student[1].append(day)

    day = 0
    while len(students) and day < 5:
        for coach in coaches:
            coach_slot = coach[1].days_available[day]
            students_to_remove = []
            for i in range(0, len(students)):
                student_slot = students[i][1][day]
                intersection = slot_intersection(coach_slot, student_slot)
                if intersection is None:
                    continue
                coach[1].used_slots.append((students[i][0], day, intersection[0], intersection[0] + 1))
                coach_slot = (intersection[0] + 1, coach_slot[1])

                students_to_remove.append(i)
                if coach_slot[0] >= coach_slot[1]:
                    break
            while len(students_to_remove):
                students.pop(students_to_remove.pop())
        day += 1
    for (name, schedule) in coaches:
        print(f'schedule for: {name}')
        for (student_name, day, start, end) in schedule.used_slots:
            print(f'  {student_name}: {day_to_string(day)} {start}-{end}')
        print()


if __name__ == '__main__':
    main()
