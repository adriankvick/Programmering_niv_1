Mil_idag=int(input("Mil idag?:"))
Mil_1_år_sen=int(input("Mil för ett år sen?:"))
Liter_bensin=float(input("Hur många liter bensin?:"))

Antal_totala_mil_körd_1_år=int(Mil_idag - Mil_1_år_sen)

print("Antal körda mil:", Antal_totala_mil_körd_1_år)

Lit_per_mil=float(Liter_bensin / Antal_totala_mil_körd_1_år)

print("Bensin förbrukning per mil:", round(Lit_per_mil,2))