use test
db.dropDatabase()
db.planets.insertMany(
    [
        { name: "Tatooine", climate: "arid", terrain: "desert" },
        { name: "Coruscant", climate: "humid", terrain: "cityscape" },
        { name: "Hoth", climate: "frozen", terrain: "ice caves" }
    ]
)
