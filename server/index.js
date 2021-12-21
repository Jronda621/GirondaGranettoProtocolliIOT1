//Import di MongoDB
var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";
//Import di Restify
var restify = require('restify');

var server = restify.createServer();
server.use(restify.plugins.bodyParser());

server.get('/drones', function(req, res, next) {
    res.send('List of drones: [TODO]');
    return next();
});

server.get('/drones/:id', function(req, res, next) {
    res.send('Current values for drone:' + req.params['id'] + ':[TODO]');
    return next();
});

server.post('/drones', function(req, res, next) {
    res.send('Data received from drone [TODO]');

    console.log(req.body);

    MongoClient.connect(url, function(err, db) {
        if (err) throw err;
        var dbo = db.db("DB_Drones");
        var myobj = req.body;
        dbo.collection("Drones_Datas").insertOne(myobj, function(err, res) {
            if (err) throw err;
            console.log("json inserito");
            db.close();
        });
    });

    return next();
});


server.listen(8013, function() {
    console.log('%s listening at %s', server.name, server.url);
});