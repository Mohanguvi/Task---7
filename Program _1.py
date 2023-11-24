
# importing the datetime directory to get the current time
import datetime 

# Get the current timestamp and using strftime is to get time in string format
current_timestamp = datetime.datetime.now().strftime("%H%M%S")

# Creating a filename with the current timestamp on
filename = f"{current_timestamp}.txt"

# writing the content as current_timestamp in the file and clsoeing it.
with open(filename, 'w') as file: 
    file.write(current_timestamp)
    file.close()






