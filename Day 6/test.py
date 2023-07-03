# import mymodule as m

# a = m.add(2,4)
# print(a)
# b = m.sub(4,2)
# print(b)

# c = m.div(2,4)
# print(c)
# d = m.multi(2,4)

# print(d)

# import shape as sh

# re = sh.rect(2,3)
# print(re)
# ci = sh.circle(4)
# print(ci)

# import words as w

# s = 'fck u'
# f = w.first(s)
# print(f)
# L = w.last(s)
# print(L)
# le = w.length(s)
# print(le)

from Utils import string_Utils as su
s ='sunny'
s = su.reverse(s)
print('reverse of entered string is :',s)

s =su.occurrence(s)
print(s)