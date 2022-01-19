Si è pensato alla struttura di un'istanza drone, con le seguenti proprietà:
- id
- nome
- velocità
- posizione

Abbiamo un producer che genera dati ogni mezzo secondo e li invia a RabbitMQ, vengono messi in coda e venogno correttamente letti dal consumer.
A sua volta quest'ultimo ad ogni messaggio ricvuto fa una call API salvando i dati su MongoDB.

Il tutto è stato testato e perfettamente funzionante



