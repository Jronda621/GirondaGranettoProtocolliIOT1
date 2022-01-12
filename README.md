Il progetto è stato così pensato:

1.Struttura Drone
2.Implementazione Protocollo HTTP
3.Implementazione Protocollo MQTT

1)

Si è pensato alla struttura di un'istanza drone, con le seguenti proprietà:
*id
*nome
*velocità
*posizione

2)

3)

Partendo da un'applizazione Main, dove vengono generati i dati relativi al drone [parte comune], si è proseguito con la creazione di un publisher che si occupa della trasmissione dei precedenti dati e di un subscriber che si occupa della ricezione.
Come broker è stato usato il broker online test.mosquitto.org.
I dati vengono trasfetiti inizialmente in formato json, con il topic *DA SISTEMARE* ...
Successivamente i dati ricevuti dal subscriber, tramite una chiamata API vengono salvati in un database su MongoDB [parte comune]

