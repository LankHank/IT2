personer = [
    {
        "navn": "Thor",
        "alder": 33
    },
    {
        "navn": "Ravi",
        "alder": 39
    },
    {
        "navn": "Ingrid",
        "alder": 21
    }
]

sortert_personer = sorted(personer, key=lambda person:person["alder"], reverse=True)
topp_2 = sortert_personer[:2]
print(topp_2)