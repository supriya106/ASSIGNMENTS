I am using Python logging to generate log files when processing and I am trying
The logging module provides the basicConfig(), used to configure the logging.
It accepts some of the commonly used argument as follows.

level - used some ERRORS like WARNING, CRITICAL & ERROR.
filename - It specifies a Log file where all exceptions will stored.
filemode - It opens a file in a specific mode. The default mode of the opening file is a, which means we can append the content.
format - The asctime() function uses a 24-hour-clock format
         for level in ('CRITICAL', 'ERROR', 'INFO', 'WARNING', 'DEBUG')
         message->> The format defines the format of the log message

by using for loop try to show the error and when we will run the code a log.txt file is automatically
with all exceptuons created
