
import datetime
import pandas as pd

import Utils.utils1

d_one = datetime.datetime.utcnow()

print(d_one)
print(type(d_one))

one_human = Utils.utils1.Human()
one_human.say_hello()

df1 = pd.DataFrame()

print(Utils.utils1.say_hello2())

