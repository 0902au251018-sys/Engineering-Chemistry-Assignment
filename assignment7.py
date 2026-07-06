plastics = {
    1: ("PET", "Water bottles", "Highly recyclable", "Recycle properly to reduce pollution."),
    2: ("HDPE", "Milk bottles", "Highly recyclable", "Safe and reusable."),
    3: ("PVC", "Pipes", "Difficult to recycle", "May release harmful chemicals."),
    4: ("LDPE", "Plastic bags", "Limited recycling", "Avoid single-use."),
    5: ("PP", "Food containers", "Recyclable", "Widely used and durable."),
    6: ("PS", "Disposable cups", "Poor recyclability", "Avoid due to pollution."),
    7: ("Other", "Mixed plastics", "Very difficult", "Use only when necessary.")
}

code = int(input("Enter recycling code (1-7): "))

if code in plastics:
    p = plastics[code]
    print("\nPolymer Name:", p[0])
    print("Common Products:", p[1])
    print("Recyclability:", p[2])
    print("Environmental Remarks:", p[3])
else:
    print("Invalid recycling code.")
