"""
Confonto i giri veloci di due piloti

"""

#importo le librerie
import matplotlib.pyplot as plt
import fastf1.plotting

# Abilito alcune modifiche di matplotlib per il tracciamento dei valori timedelta e carico
# lo schema di colori predefinito di FastF1
fastf1.plotting.setup_mpl(misc_mpl_mods=False)

# Carico una sessione e i suoi dati di telemetria
session = fastf1.get_session(2023, 'Ungheria Grand Prix', 'Q')
session.load()

def prepara_dati(driver):
    # Seleziona il giro più veloce del pilota
    giro = session.laps.pick_driver(driver).pick_fastest()

    # ottengo i dati di telemetria per il giro e aggiungo una colonna 'Distanza'
    telemetria = giro.get_car_data().add_distance()

    return telemetria

# Preparo i dati per i piloti
telemetria_ver = prepara_dati('VER')
telemetria_ham = prepara_dati('HAM')

# Preparo i colori delle squadre
colore_rbr = fastf1.plotting.team_color('RBR')
colore_mer = fastf1.plotting.team_color('MER')

fig, ax = plt.subplots()

# Traccio le linee di velocità per entrambi i piloti
ax.plot(telemetria_ver['Distance'], telemetria_ver['Speed'], color=colore_rbr, label='VER')
ax.plot(telemetria_ham['Distance'], telemetria_ham['Speed'], color=colore_mer, label='HAM')

ax.set_xlabel('Distanza in m')
ax.set_ylabel('Velocità in km/h')

ax.legend()

plt.suptitle(f"Confronto dei giri più veloci \n "
             f"{session.event['EventName']} {session.event.year} Qualifica")

plt.show()
