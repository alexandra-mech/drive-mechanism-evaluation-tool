A = 6.07e6      #Reservoir area in m2
h = 21.3        #Thickness in m
NTG = 0.8       #Net-To-Gross
phi = 0.21      #Porosity
Sw = 0.25       #Water Saturation
Bo = 1.2        #Volumetric factor of petroleum
P0 = 26200      #Initial pressure in kPa
Pwf = 13800     #Final water pressure in kPa
Q0 = 95.4       #Initial flow rate in m3/day

def reservoir_model():
    print("=== DRIVE MECHANISMS ===")
    print("1. Rock & Fluid Expansion")
    print("2. Solution Gas Drive")
    print("3. Gas Cap Drive")
    print("4. Gravity Drainage")
    print("5. Aquifer Drive (weak)")
    print("6. Aquifer Drive (strong)")
    print("==========================")
        
    opt = int(input("Select the number of the desired drive mechanism: "))

    GRV = A * h
    STOOIP = (GRV * NTG * phi * (1 - Sw))/Bo
    NRV = GRV * NTG
    J = Q0/(P0 - Pwf)

    def select_Recovery_Factor(opt):
        if opt == 1:
            RF = STOOIP * 0.05
            return RF
        elif opt == 2:
            RF = STOOIP * 0.2
            return RF
        elif opt == 3:
            RF = STOOIP * 0.3
            return RF
        elif opt == 4:
            RF = STOOIP * 0.4
            return RF
        elif opt == 5:
            RF = STOOIP * 0.35
            return RF
        elif opt == 6:
            RF = STOOIP * 0.45
            return RF
        else:
            raise ValueError("Unknown drive mechanism")
        
    #Calculate estimated future flow rate
    Pf = 20000      #Estimated future pressure in kPa
    Qf = J * (Pf - Pwf)

    print("=== RESULTS ===")

    return{
    "Gross Rock Volume [m3]: ": GRV,
    "STOOIP [m3]: ": STOOIP,
    "Net Rock Volume [m3]: ": NRV,
    "Productivity Index [m3/day/bar]: ": J,
    "Recoverable Oil: ": select_Recovery_Factor(opt),
    "Drive Mechanism: ": opt,
    "Future Flow Rate [m3/s]: ": Qf
}

results = reservoir_model()

for parameter, value in results.items():
    print(parameter, value)