# Builtin Features

## Disclaimer !!!!


## colors.h

Defines colors for output.
	
### Available Colors

* RED
* GREEN
* YELLOW
* BLUE
* MAGENTA
* CYAN
* RESET



## logger.h

Declares functions to be used by logger.c
	
### Declared Functions

* void error(FILE *stream, char *type, char *message);
* void info(FILE *stream, char *type, char *message);

## logger.c

Defines functions declared by logger.h
	
* void error(...): outputs 'type' and 'messsage' into 'stream' but in the color RED.
* void info(...): outputs 'type' and 'message' into 'stream' but in the color GREEN.
