Si è pensato alla struttura di un'istanza drone, con le seguenti proprietà:
- id
- nome
- velocità
- posizione

Partendo da un'applizazione Main, dove vengono generati i dati relativi al drone [parte comune], si è proseguito con la creazione di un publisher che si occupa della trasmissione dei precedenti dati e di un subscriber che si occupa della ricezione.

Come broker è stato usato il broker online test.mosquitto.org per mancanza di tempo per implementare il docker.


La gestione dei topic è stata affrontata velocemente e in maniera generica (per ora) inserendo il tutto nel topic NOME/ID. Viene inviato un JSON dal publisher con tutti i dati del drone ogni tempo n (nome, id, velocita, posizione)
Questi dati vengono letti da un subscriber e ad ogni lettura viene fatta una chiamata tramite python.requests di tipo POST alla REST API che salva i dati su MongoDB.




