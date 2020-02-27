import logging
import sys

# Log configuration
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s %(levelname)s %(message)s',
                    handlers=[
                            logging.FileHandler("debug.log"),  # Log to file
                            logging.StreamHandler(),   # Log to stderr,
                            logging.StreamHandler(sys.stdout)   # Log to stdout
                        ])

logging.debug('Ths is a debug')


# set log levels

logging.getLogger().setLevel(logging.INFO)


## When using logger in another file
log = logging.getLogger(__name__)
log.info("Hello logging!")
