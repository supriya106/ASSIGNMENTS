import logging
logging.basicConfig(filename="Log.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S')

i=10
try:
    i=i/0
except:
    logging.error("Division by zero")