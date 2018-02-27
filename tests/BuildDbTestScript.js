use test
db.dropDatabase()
db.planets.insertMany(
    [
        { _id : ObjectId("5a959ef17ef03fc0da5bc177"), name : "Tatooine", climate : "arid", terrain : "desert" },
        { _id : ObjectId("5a959ef17ef03fc0da5bc178"), name : "Coruscant", climate : "humid", terrain : "cityscape" },
        { _id : ObjectId("5a959ef17ef03fc0da5bc179"), name : "Hoth", climate : "frozen", terrain : "ice caves" }
    ]
)
