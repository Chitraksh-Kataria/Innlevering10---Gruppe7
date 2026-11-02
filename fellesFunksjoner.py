import pandas as pd


def HentFraFil(filnavn):
    dataFrame = pd.read_csv(f"VærStasjoner/{filnavn}", sep=";", decimal=",", na_values=["-"])
    output = {
        "Navn": dataFrame["Navn"].to_numpy(),
        "Stasjon": dataFrame["Stasjon"].to_numpy(),
        "Tid": dataFrame["Tid(norsk normaltid)"].to_numpy(),
        "Maksimumstemperatur (døgn)": dataFrame["Maksimumstemperatur (døgn)"].to_numpy(),
        "Middeltemperatur (døgn)": dataFrame["Middeltemperatur (døgn)"].to_numpy(),
        "Nedbør (døgn)": dataFrame["Nedbør (døgn)"].to_numpy(),
        "Høyeste middelvind (døgn)": dataFrame["Høyeste middelvind (døgn)"].to_numpy(),
        "Snødybde": dataFrame["Snødybde"].to_numpy(),
    }
    return output
