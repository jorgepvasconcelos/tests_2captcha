import sys
import os

from twocaptcha import TwoCaptcha

from settings import API_KEY

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


solver = TwoCaptcha(API_KEY)

try:
    result = solver.normal('normal.jpg')

except Exception as e:
    print(e)

else:
    sys.exit('solved: ' + str(result))