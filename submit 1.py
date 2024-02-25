def schedule_task(workweek):
    while True:
        taskname = input('Enter your task name: ')
        taskduration = int(input('Enter your task duration (in hours): '))
        optionalday = input('Enter the day you want to do the task : ')
        optionalhour = int(input('Enter the starting hour for the task (from 0 to 23): '))
        
        if optionalday.lower() not in workweek:
            print('Invalid day. Please enter a valid day.')
            continue
        
        if optionalhour < 0 or  taskduration > 8:
            print('Invalid task duration. Please choose a valid time.')
            continue
        
        day_schedule = workweek[optionalday.lower()]
        conflict_tasks = [hour for hour in range(optionalhour, optionalhour + taskduration) if hour in day_schedule]
        
        if conflict_tasks:
            print('Task overlapping with existing task')
            decision = input('Do you want to overwrite the existing task(s)? (yes/no): ')
            if decision.lower() == 'yes':
                for hour in conflict_tasks:
                    day_schedule.remove(hour)
                print('Task overwritten.')
            else:
                continue
        
        for hour in range(optionalhour, optionalhour + taskduration):
            day_schedule.append(hour)
        
        print('Task "{}" scheduled for {} starting at hour {} for {} hour(s).'.format(taskname, optionalday, optionalhour, taskduration))
        
        another_task = input('Do you have more tasks to schedule? (yes/no): ')
        if another_task.lower() != 'yes':
            break


workweek = {
    'sunday': [],
    'monday': [],
    'tuesday': [],
    'wednesday': [],
    'thursday': []
}

schedule_task(workweek)


print('\nUpdated Workweek Schedule:')
for day, schedule in workweek.items():
    print(day.capitalize() + ':', schedule)
