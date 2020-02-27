# Raise and Catch Exception

try:
    raise Exception("Shit hit the fan!")
except Exception as errObj:
    print(str(errObj))


# Getting Stacktrace

import traceback

try:
    raise Exception("Shit hit the fan!")
except Exception as errObj:
    print(traceback.format_exc())


# Assertion can be disabled by option - o
# Assertion does not need to be in try catch

assert False == True, 'false does not equal true!'

