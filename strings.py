#strings

value="entertainment"
print(value)

string='enttertainment'
print(string)

print("509\902/89")

#upper to lower case and lower to upper case

up='nthng is permanent'
print(up.upper())

low='anything is temporary'
print(low.lower())

print("hi".upper())

#\n = new line
error='my computer \n new folder'
print(error)
print('nthng to tell \n here')

'''solve for the \n problem (raw string (r))'''

error='nthng to tell \n here'
print(r'nthng to \n tell here')

#string indexes

alphabets='abcdefghijklmnopqrstuvwxyz'
print(alphabets[2])
print(alphabets[-1])
print(alphabets[0].upper())

#slicing operators

alphabets='abcdefghijklmnopqrstuvwxyz'
print(alphabets[0:8])
print(alphabets[5:11].upper())

#reverse slicing
print(alphabets[-8:-2])
print(alphabets[-26])

#title capitalize changing

modi="modi has announced"
sasi=(modi.title())
print(sasi)
print(modi.upper())

akash="vedhagiri"+"765"
print(akash)


# in command

name="entertainment"
print("t" in name)

w='hello '*6
print(w)
'''
#roundoff
tamil=87
english=87.6
print(int(tamil+english))

maths=int(input('maths is :'))
science=int(input('science :'))
social=float(input('social is :'))
total=int(maths+science+social)
print(total)'''


#reverse string

print(input('the numbers')[::-1])

k='123456'
print(len(k))