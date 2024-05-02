from fetch import *

res = zfetch('https://www.google.com/example/page')
print(res.zread())
