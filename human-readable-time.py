"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
You can find some examples in the test fixtures."""

def seconds_to_time(seconds):
    hours = seconds // 3600  # get number of hours
    seconds = seconds % 3600 # remove full hours, keep only remaining seconds
    minutes = seconds // 60 # number of minutes
    seconds = seconds % 60 # number of seconds
    return(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

print(seconds_to_time(3661)) # Output: "01:01:01"