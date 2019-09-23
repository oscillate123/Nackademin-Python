n = "\n"
# line breaker

input_sec = int(input("Hur många sekunder: "))
# number of seconds the user want to use for the program

days = input_sec//86400
input_sec = input_sec - 86400*days
# subtract the number of days in the value of seconds, if the input_sec//86400 = 0, no seconds will
# withdraw from the input_sec value

hours = input_sec//3600
input_sec = input_sec - 3600*hours
# subtract the number of hours in the value of seconds, if the input_sec//3600 = 0, no seconds will
# withdraw from the input_sec value

minutes = input_sec//60
input_sec = input_sec - 60*minutes
# subtract the number of minutes in the value of seconds, if the input_sec//60 = 0, no seconds will
# withdraw from the input_sec value

msg_time_types = (str(days) + " dagar" + n + str(hours) +
                   " timmar" + n + str(minutes) + " minuter" + n + str(input_sec) + " sekunder")

# msg_log = (n + str(input_sec) + n + str(days) + n + str(hours) + n + str(minutes))

print(msg_time_types)
# print(msg_log)
