const {Schema, model} = require("mongoose");

const droneSchema = new Schema(
    {
        NOME: String,
        ID: Number,
        VELOCITA: String,
        POSIZIONE: String

    },
    {timestamps: true}
);

module.exports = model("drones", droneSchema);
