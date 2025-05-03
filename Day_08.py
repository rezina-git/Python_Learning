#Control Statements
#Continue--> 1 ta condition lai stop garera next condition laii execute garxa
for i in range(1,12,1):
    if i%2 == 0:
        continue
    print(i)

#Pass-->SEcure space for future
#Future ko lagi paxi keii  space secure garera rakhxa

for i in range (10):
    pass
print("Hello")

#Break--->Loop terminates whenever break keyword is encounter

i = 0
while i<5 :
    print(i)
    if i == 2 :
        break
    i += 1
    #0,1,2 matra print hunxa kina vaney jaba i ko value 2 hunxa loop laii break ley teii break garxa ra iya dekhi muni execute hunna