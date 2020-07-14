import string

uppers = list(string.ascii_uppercase)                   # set with uppercase letters
lowers = list(string.ascii_lowercase)                   # set with lowercase letters
numbers = list('0123456789')                            # set with all one digit numbers

elements = {                                            # dictionary of elements with corresponding atomic mass
    'H': 1.008,
    'He': 4.002,
    'Li': 6.94,
    'Be': 9.012,
    'B': 10.8,
    'C': 12.0,
    'N': 14.0,
    'O': 16.0,
    'F':  19.0,
    'Ne': 20.2,
    'Na': 23.0,
    'Mg': 24.3,
    'Al': 27.0,
    'Si': 28.1,
    'P': 31.0,
    'S': 32.1,
    'Cl': 35.5,
    'Ar': 39.9,
    'K': 39.1,
    'Ca':40.1,
    'Sc': 44.956,
    'Ti': 47.867,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938,
    'Fe': 55.845,
    'Co': 58.933,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.38,
    'Ga': 69.723,
    'Ge': 72.630,
    'As': 74.921,
    'Se': 78.971,
    'Br': 79.9,
    'Kr': 83.798,
    'Rb': 85.4678,
    'Sr': 87.62,
    'Y': 88.906,
    'Zr': 91.224,
    'Nb': 92.906,
    'Mo': 95.95,
    'Tc': 98
    }
    
"""
44 Ru - Ruthenium - 101.07(2)
45 Rh - Rhodium - 102.905 50(2)
46 Pd - Palladium - 106.42(1)
47 Ag - Silver - 107.8682(2)
48 Cd - Cadmium - 112.414(4)
49 In - Indium - 114.818(1)
50 Sn - Tin - 118.710(7)
51 Sb - Antimony - 121.760(1)
52 Te - Tellurium - 127.60(3)
53 I  - Iodine - 126.904 47(3)
54 Xe - Xenon - 131.293(6)
55 Cs - Cesium - 132.905 451 96(6)
56 Ba - Barium - 137.327(7)
57 La - Lanthanum - 138.905 47(7)
58 Ce - Cerium - 140.116(1)
59 Pr - Praseodymium - 140.907 66(2)
60 Nd - Neodymium - 144.242(3)
61 Pm - Promethium - <145>
62 Sm - Samarium - 150.36(2)
63 Eu - Europium - 151.964(1)
64 Gd - Gadolinium - 157.25(3)
65 Tb - Terbium - 158.925 35(2)
66 Dy - Dysprosium - 162.500(1)
67 Ho - Holmium - 164.930 33(2)
68 Er - Erbium - 167.259(3)
69 Tm - Thulium - 168.934 22(2)
70 Yb - Ytterbium - 173.054(5)
71 Lu - Lutetium - 174.9668(1)
72 Hf - Hafnium - 178.49(2)
73 Ta - Tantalum - 180.947 88(2)
74 W - Tungsten - 183.84(1)
75 Re - Rhenium - 186.207(1)
76 Os - Osmium - 190.23(3)
77 Ir - Iridium - 192.217(3)
78 Pt - Platinum - 195.084(9)
79 Au - Gold - 196.966 569(5)
80 Hg - Mercury - 200.592(3)
81 Tl - Thallium - [204.382; 204.385]
82 Pb - Lead - 207.2(1)
83 Bi - Bismuth - 208.980 40(1)
84 Po - Polonium - <209>
85 At - Astatine - <210>
86 Rn - Radon - <222>
87 Fr - Francium - <223>
88 Ra - Radium - <226>
89 Ac - Actinium - <227>
90 Th - Thorium - 232.037 7(4)
91 Pa - Protactinium - 231.035 88(2)
92 U  - Uranium - 238.028 91(3)
93 Np - Neptunium - <237>
94 Pu - Plutonium - <244>
95 Am - Americium - <243>
96 Cm - Curium - <247>
97 Bk - Berkelium - <247>
98 Cf - Californium - <251>
99 Es - Einsteinium - <252>
100 Fm - Fermium - <257>
101 Md - Mendelevium - <258>
102 No - Nobelium - <259>
103 Lr - Lawrencium - <262>
104 Rf - Rutherfordium - <267>
105 Db - Dubnium - <268>
106 Sg - Seaborgium - <271>
107 Bh - Bohrium - <272>
108 Hs - Hassium - <270>
109 Mt - Meitnerium - <276>
110 Ds - Darmstadtium - <281>
111 Rg - Roentgenium - <280>
112 Cn - Copernicium - <285>
113 Uut - Ununtrium - <284>
114 Fl - Flerovium - <289>
115 Uup - Ununpentium - <288>
Lv - Livermorium - <293>
Uuo - Ununoctium - <294>
"""
while True:
    formula = input('Enter Compound:')                  # user inputs formula

    totalmass = 0                                       # initialization of total mass elementCount
    positions = []                                      # intialize list
    
    for i in range(len(formula)):                       # determination of indices of capital letters
        if formula[i] in uppers:
            positions.append(i)

    for i in range(len(positions)):
        positions.append(None)
        packet = formula[positions[i]:positions[i+1]]   # break each element and following number into packets
        print(packet)
        if len(packet) == 1:                            # case for single character packets; note: there is only one element if single character
            element = packet[0]
            elementCount = 1
        elif packet[1] in lowers:                       # case for two character packets    
            if packet[2] in numbers:                    # check for following number
                elementCount = float(packet[2:])
            else:
                elementCount = 1
            element = packet[0:1]
        elif packet[1] in numbers:                      # case for multiple of a single charater element
            elementCount = float(packet[1:])
            element = packet[0]
        else:                                           # error catcher
            print('An Unexpected Error Occurred')
            
        mass = elements.get(element) * elementCount     # total mass of packet
        totalmass = totalmass + mass                    # packet mass added to the total

    print(totalmass)                                    # output total calculated mass
            
    
    

















    
