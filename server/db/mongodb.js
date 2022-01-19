const mongoose = require("mongoose");

const init = () => {
    mongoose
        .connect("mongodb://localhost:27017/AMQP_MQTT", {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        })
        .catch((err) => {
            console.error("error: " + err.stack);
            process.exit(1);
        });
    mongoose.connection.on("open", () => {
        console.log("connected to database");
    });
};

mongoose.Promise = global.Promise;

module.exports = init;
