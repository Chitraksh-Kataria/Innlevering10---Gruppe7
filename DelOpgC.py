import matplotlib.pyplot as plt
import pandas as pd

from fellesFunksjoner import HentFraFil

### Husk å løp denne filen i root directoryen til innleveringen
filnavn = [
    "oslo_blindern_1954_2025_med_makstemperatur.csv",
    "roeros_1954_2025_med_makstemperatur.csv",
    "tromsoe_1954_2025_med_makstemperatur.csv",
    "vaernes_1954_2025_med_makstemperatur.csv",
    "venabu_1954_2025_med_makstemperatur.csv",
]


print(len(filnavn))


### Henter data ut fra filene
svar = []
for i in range(0, len(filnavn)):
    svar.append(HentFraFil(filnavn=filnavn[i]))

### Henter Tempraturene for alle værstasjonene
for i in range(0, len(filnavn)):
    antall_dager = 0
    temperatur_sum = 0
    gjeldende_aar = None

    aarstall = []
    gjennomsnitt = []

    for j in range(0, len(svar[i]["Tid"])):
        dato = pd.to_datetime(svar[i]["Tid"][j], dayfirst=True)
        aar = dato.year
        tempratur = svar[i]["Middeltemperatur (døgn)"][j]

        if gjeldende_aar != aar:
            if antall_dager >= 300:
                aarstall.append(gjeldende_aar)
                gjennomsnitt.append(temperatur_sum / antall_dager)

            antall_dager = 0
            temperatur_sum = 0
            gjeldende_aar = aar

        if pd.isna(tempratur) == False:
            antall_dager += 1
            temperatur_sum += float(tempratur)

    if antall_dager >= 300:
        aarstall.append(gjeldende_aar)
        gjennomsnitt.append(temperatur_sum / antall_dager)

    plt.plot(aarstall, gjennomsnitt, label=filnavn[i].split("_")[0])

plt.xlabel("År")
plt.ylabel("Gjennomsnittstemperatur (°C)")
plt.title("Gjennomsnittstemperatur per år")
plt.legend()
plt.grid()
plt.show()
