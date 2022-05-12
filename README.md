# logger
Custom [logging](https://docs.python.org/3/howto/logging.html) instance  
- INFO & ERROR level messages go to separate log files

## Example
Running the following code...
```
from logger import logger

logger.info('hello info')
logger.error('uh oh error')
```
Would yield the following in whichever directory the logger.py file is placed...
```
_log
  MM-DD-YYYY_hhmmss.txt > 'hello info'
_err
  MM-DD-YYYY_hhmmss.txt > 'uh oh error'
```
