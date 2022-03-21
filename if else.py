'''looping concept'''


#if else

tamil=89
english=99
maths=100
if tamil==english:
    print("tamil and english are equal" )
elif english<tamil:
    print('english is greater')
elif maths>english:
    print('maths is greater')
else:
    print('both are wrong')

uk=200
usa=200
india=200
kiwis=200
netherlands=200

if uk==usa==india==kiwis==netherlands:
    print("all are same")
elif uk<netherlands:
    print("uk and netherlands are equal")
elif india>kiwis:
    print("india is greater than kiwis")
elif netherlands==kiwis:
    print("nethers and kiwis are equal")
else:
    print("kiwis is the highest")

#runtime in if else condition

'''tamil=int(input("tamil mark is "))
english=int(input('english mark is '))
maths=int(input('maths mark is '))
science=int(input('science mark is '))
social=int(input('social mark is '))

if tamil==english:
    print("both are equal")
elif maths>=english:
    print(('maths is greater'))
elif science>=maths:
    print('science is greater'
          )
elif social<=science:
    print('social is lesser')
else: print("everything is wrong")

us=int(input('us ='))
uk=int(input('uk='))
ind=int(input('ind =')
        )
pak=int(input('pak =')
        )
sri=int(input('sri ='))
aus=int(input('aus ='))
rus=int(input('rus ='))

print('the answer is',us+uk+ind+pak+sri+aus+rus)


if us==uk:
    print('us = uk')
elif uk>=ind:
    print('uk is greater')
elif sri<=pak:
    print('nthng'
          )
elif ind==pak:
 print('ind and pak r equal')
else:
    print('it is nthng')'''


#nested if

'''using if condition inside a if condition is called nested if'''

'''age=int(input('ur age: '))
if age>5:
    nationality=input('enter the nationality:')
    if nationality=='indian' or nationality=="INDIAN":
        print('eligible for aadhar')
    else: print('not eligible for aadhar')

else:
    print('not under the age criteria')'''

#sorted

'''abc=input('word 1:')
bcd=input('word 2:')

if sorted(abc)==sorted(bcd):
    print('both the word are same')
else:
    print('not same')'''

'''mark1=float(input('mark1 :'))
mark2=int(input('mark2 :'))
mark3=float(input('mark3 :'))

if mark1==mark2 or mark2==mark3 :
    print('the  conditions are true')

else:
    print('conditions is false')'''

kim="sorting is a thing"
kom="thingis a sorting"

if sorted(kim)==sorted(kom):
    print('it is equal')
else: print('not equal')

#not

'''d=int(input('value of d:'))

if not d==3:
    print('it is right')
else: print('it is wrong')

age=int(input('enter the age:'))
if not age!=3:
       nationality=input('nationality:')
       if nationality=='indian' or nationality=='INDIAN':
           print('eligible')
       else:
           print('not eligible')

else:
    print('age not in criteria')'''

age=int(input('your age:'))

if not age==1:

    nationality=(input('enter your nationality'))
    if nationality=='INDIAN' or nationality=='indian' or nationality=='Indian':
      state = (input('enter your state'))
      if state=='tamilnadu' or state==['TAMILNADU','tamilnadu']:
          district=(input('enter the name of the district'))
          if district=='salem' or district=='namakkal' or district=='trichy' or district=='madurai' or district=='chennai' or district=='naagai':
            print('district is eligible')
          else:
             print('district is not eligible')
      else: print('state is not eligible')
    else: print("nation is not eligible")
else: print('age is not eligible')