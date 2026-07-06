elements = {
    "Na": {
        "Atomic Number": 11,
        "Atomic Mass": 22.99,
        "Group": 1,
        "Period": 3,
        "Electronic Configuration": "[Ne] 3s1",
        "Oxidation State": "+1",
        "Application": "Street lighting"
    },
    "Fe": {
        "Atomic Number": 26,
        "Atomic Mass": 55.845,
        "Group": 8,
        "Period": 4,
        "Electronic Configuration": "[Ar] 3d6 4s2",
        "Oxidation State": "+2, +3",
        "Application": "Construction steel"
    },
    "Cl": {
        "Atomic Number": 17,
        "Atomic Mass": 35.45,
        "Group": 17,
        "Period": 3,
        "Electronic Configuration": "[Ne] 3s2 3p5",
        "Oxidation State": "-1",
        "Application": "Water purification"
    },
    "Cu": {
        "Atomic Number": 29,
        "Atomic Mass": 63.546,
        "Group": 11,
        "Period": 4,
        "Electronic Configuration": "[Ar] 3d10 4s1",
        "Oxidation State": "+1, +2",
        "Application": "Electrical wiring"
    }
}

symbol = input("Enter element symbol: ")

if symbol in elements:
    print("\nElement Information")
    for key, value in elements[symbol].items():
        print(f"{key}: {value}")
else:
    print("Element not found.")
