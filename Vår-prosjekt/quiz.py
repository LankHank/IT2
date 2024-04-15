from random import randint

spørsmåls = [
    {
        "nummer": 1,
        "spm": "Hvilket år kom første sesong av Game og Thrones ut?",
        "alternativer": ["a: 2013","b: 2009","c: 2011"],
        "fasit": "c"
    }
]

print("-- QUIZ --")
spørsmål_nummer = randint(0, 1)

print(spørsmåls[spørsmål_nummer]["spm"])
for alternativer in spørsmåls[spørsmål_nummer]["alternativer"]:
    print(alternativer)

brukerinput = input("> ")

if brukerinput == spørsmåls[spørsmål_nummer]["fasit"]:
    pass


