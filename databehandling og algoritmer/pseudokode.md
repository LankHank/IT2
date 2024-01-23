# Pseudokode
- en måte å beskrive en algoritme eller et program på ved hjelp av naturlig språk
- brukes ofte som et verktøy for å planlegge og designe algoritmer før de faktisk blir kodet i et bestemt programmeringsspråk
- gjør det lettere å kommunisere og samarbeide med andre programmerere, samt å teste og feilsøke algoritmer før de blir kodet.
- en god måte å lære grunnleggende programmeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske uttrykk fungerer sammen for å løse et bestemt problem.


## Eksempel: Penger tjent på spotify

> En algoritme som regner ut hvor mte penger vi tjener på Spotify

### Pseudokode
```pseduo
Hent inn antall streams
Hvis antall stream er større enn 30mill: 
    Print antall streams * 0.7
Ellers hvis antall streams er større enn 1.4mill:
    Print antall streams * 0.4
Ellers:
    Print 0
```

### Pseudokode
```
SET antall_streams TO READ "Hvor mange streams?"
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streans GREATER THAN 1 400 000
    THEN DISPLAY antall_streams * 0.4
ELSE DISPLAY 0    
```

### Pythonkode
```python
antall_streams = int(input("Hvor mange streams?"))

if antall_streams <= 1_399_999:
    print 0
elif 1_400_000 <= antall_streams <= 29_999_999:
    print(0.40 * antall_streams)
else:
    print(0.70 * antall_streams)

```