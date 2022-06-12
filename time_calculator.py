def add_time(start, duration, weekday = "1"):
    def time2decimal (time): #11:45 -> 11.75
        time = time.split(":")
        return int(time[0]) + int(time[1]) / 60

    def decimal2time (time): #11.75 -> 11:45
        minutes_decimal = time - int(time)
        minutes = minutes_decimal * 60
        if int(time) == 0:
            time = 12
        string = [str(int(time)), ":", str(round(minutes)).zfill(2)]
        return ("".join(string))

    semana = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    input_time = start #11:30 AM
    time_splitted = input_time.split() #11:30, AM
    input_time_decimal = time2decimal(time_splitted[0]) #11.5
    input_period = time_splitted[1] #AM

    if input_period == "AM":
        time = input_time_decimal
    elif input_period == "PM":
        time = input_time_decimal + 12

    add_time = time2decimal(duration)
    sum_time = time + add_time

    days_later = int(sum_time / 24)
    final_time = sum_time % 24

    if final_time >= 12:
        final_str = str(decimal2time(final_time - 12)) + " PM"
    else:
        final_str = str(decimal2time(final_time)) + " AM"

    if weekday != "1":
        day = weekday
        day = day.lower().capitalize()
        day_index = semana.index(day)
        final_str = final_str + ", " + semana[(day_index + days_later) % 7]

    if days_later == 1:
        final_str = final_str + " (next day)"
    elif days_later > 1:
        final_str = final_str + " (" + str(days_later) + " days later)"

    new_time = final_str
    return new_time
