import re
"""
regualr expression
first create a metacharacter match
Then create a [] match for range and 
then create a {m,n} for repetition
then create a () for grouping them
"""
print("Hello")

value="abc_m19_310_ABC_A_1992.br.nz"
value="abc_m19_310_ABC_A_1992.br.nz"
value="abc_m19_310_ABC_A_1992.br.nz"


pattern=r'[a-c]{3}_\w\d{2}_3[0-2]{2}_[A-C]+_[A-C]+_\d{4}\.+br\.nz*'
print("Result",re.findall(pattern,value))

pattern=r'([a-c]{3})_(\w+\d{2})_(3[0-2]{2})_([A-C]{1}.*)_([A-C]+)_(\d{4})(\.br)(\.nz+)'

print("Result"
      ,re.match(pattern,value).groups()
      )