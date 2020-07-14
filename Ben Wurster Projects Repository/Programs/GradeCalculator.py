import string

print('Input Known Values, Type "Done" When Complete')

totalpp = 0
egp = 0

while totalpp < 1:
    
    ep = input('Earned Points:')
    
    if ep == 'Done':
        break
    else:
        epnum = float(ep)

    tp = input('Total Points:')
    tpnum = float(tp)
    
    chunk = input('Percentage of Grade(As Decimal):')
    chunktot = float(chunk)
    
    sgnum = epnum/tpnum
    
    totalpp += chunktot
    chunkgrade = sgnum * chunktot

    egp += chunkgrade

if totalpp > 0.9999 and totalpp < 1.0001:
    print('Final grade:' + str(egp))
elif totalpp < 0.9999:
    print('Earned grade:' + str(egp))
    remainingpp = 1 - totalpp
    print('What Ifs?:')
    for i in range(101):
        print('If you earn ' + str(i) + '% of the remaining ' + str(remainingpp) + ', your final grade will be ' + str(egp + (i/100)*remainingpp))   
else:
    print('Error: You Cannot Exceed 100%')
    
