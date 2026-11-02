from fellesFunksjoner import HentFraFil

### Husk å løp denne filen i root directoryen til innleveringen
filnavn = ["oslo_blindern_1954_2025_med_makstemperatur.csv", "roeros_1954_2025_med_makstemperatur.csv", "tromsoe_1954_2025_med_makstemperatur.csv", "vaernes_1954_2025_med_makstemperatur.csv", "venabu_1954_2025_med_makstemperatur.csv"]


print(len(filnavn))


### Henter data ut fra filene
svar = []
for i in range(0, len(filnavn)):
    svar.append(HentFraFil(filnavn=filnavn[i]))

### Henter Tempraturene for alle værstasjonene
