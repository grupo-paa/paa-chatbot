// const axios = require('axios')
import axios from "axios";
import { forEach } from "lodash";
import { Schema, model, connect } from "mongoose"
// import _, { toPlainObject } from 'lodash'

const dbUrl = "mongodb+srv://admin:admin@paa-chatbot.tp4urq2.mongodb.net/flask_db"

await connect(dbUrl)

const base = "https://swapi.dev/api/"

type people_api = {
    films: Array<string>
    species: Array<string>
    vehicles: Array<string>
    starships: Array<string>
}
type base_people = {
    name: string
    height: string
    mass: string
    hair_color: string
    skin_color: string
    eye_color: string
    birth_year: string
    gender: string
    homeworld: string
    created: string
    edited: string
    url: string
}
type base_vehicle = {
    name: String
    model: String
    manufacturer: String
    cost_in_credits: String
    length: String
    max_atmosphering_speed: String
    crew: String
    passengers: String
    cargo_capacity: String
    consumables: String
    vehicle_class: String
    pilots: Array<string>
    films: Array<string>
    created: String
    edited: String
    url: String
}
type base_film = {
    title: String
    episode_id: Number
    opening_crawl: String
    director: String
    producer: String
    release_date: String
    characters: Array<string>
    planets: Array<string>
    starships: Array<string>
    vehicles: Array<string>
    species: Array<string>
    created: String
    edited: String
    url: String
}
type base_specie = {
    name: string
    classification: string
    designation: string
    average_height: string
    skin_colors: string
    hair_colors: string
    eye_colors: string
    average_lifespan: string
    homeworld: string
    language: string
    people: string
    films: string
    created: string
    edited: string
    url: string
}
type base_planet = {
    name: String
    rotation_period: String
    orbital_period: String
    diameter: String
    climate: String
    gravity: String
    terrain: String
    surface_water: String
    population: String
    residents: Array<string>
    films: Array<string>
    created: String
    edited: String
    url: String
}
type base_starship = {
    name: String
    model: String
    manufacturer: String
    cost_in_credits: String
    length: String
    max_atmosphering_speed: String
    crew: String
    passengers: String
    cargo_capacity: String
    consumables: String
    hyperdrive_rating: String
    MGLT: String
    starship_class: String
    pilots: Array<string>
    films: Array<string>
    created: String
    edited: String
    url: String
}

type Subject = Record<string, string | string[]> & { url: string }
type planet = {
    name: string,
    rotation_period: string,
    orbital_period: string
    diameter: string
    climate: string
    gravity: string
    terrain: string
    surface_water: string
    population: string
    residents: Array<string>
    films: Array<string>
    created: string
    edited: string
    url: string
}
type film = {
    title: string
    episode_id: number
    opening_crawl: string
    director: string
    producer: string
    release_date: string
    characters: Array<string>
    planets: Array<string>
    starships: Array<string>
    vehicles: Array<string>
    species: Array<string>
    created: string
    edited: string
    url: string
}
type starship = {
    name: string
    model: string
    manufacturer: string
    cost_in_credits: string
    length: string
    max_atmosphering_speed: string
    crew: string
    passengers: string
    cargo_capacity: string
    consumables: string
    hyperdrive_rating: string
    MGLT: string
    starship_class: string
    pilots: Array<string>
    films: Array<string>
    created: string
    edited: string
    url: string
}
type vehicle = {
    name: string,
    model: string,
    manufacturer: string,
    cost_in_credits: string,
    length: string,
    max_atmosphering_speed: string,
    crew: string,
    passengers: string,
    cargo_capacity: string,
    consumables: string,
    vehicle_class: string,
    pilots: Array<string>,
    films: Array<string>,
    created: string,
    edited: string,
    url: string
}
type species = {
    name: string,
    classification: string,
    designation: string,
    average_height: string,
    skin_colors: string,
    hair_colors: string,
    eye_colors: string,
    average_lifespan: string,
    homeworld: string,
    language: string,
    people: Array<string>,
    films: Array<string>,
    created: string,
    edited: string,
    url: string,
}

const peopleSchema = new Schema<base_people & people_api>({
    name: String,
    height: String,
    mass: String,
    hair_color: String,
    skin_color: String,
    eye_color: String,
    birth_year: String,
    gender: String,
    homeworld: String,
    url: String,
    films: Array<string>,
    species: Array<string>,
    vehicles: Array<string>,
    starships: Array<string>
})

peopleSchema.pre<base_people>('save', function (next) {
    this.name = this.name.toLowerCase();
    next();
});

const specieSchema = new Schema<species>({
    name: String,
    classification: String,
    designation: String,
    average_height: String,
    skin_colors: String,
    hair_colors: String,
    eye_colors: String,
    average_lifespan: String,
    homeworld: String,
    language: String,
    people: Array<string>,
    films: Array<string>,
    created: String,
    edited: String,
    url: String,
})

specieSchema.pre<base_specie>('save', function (next) {
    this.name = this.name.toLowerCase();
    this.language = this.language.toLowerCase();
    next();
});

const vehicleSchema = new Schema<vehicle>({
    name: String,
    model: String,
    manufacturer: String,
    cost_in_credits: String,
    length: String,
    max_atmosphering_speed: String,
    crew: String,
    passengers: String,
    cargo_capacity: String,
    consumables: String,
    vehicle_class: String,
    pilots: Array<string>,
    films: Array<string>,
    created: String,
    edited: String,
    url: String
})

vehicleSchema.pre<base_vehicle>('save', function (next) {
    this.name = this.name.toLowerCase();
    this.model = this.model.toLowerCase();
    this.manufacturer = this.manufacturer.toLowerCase();
    next();
});

const planetSchema = new Schema<planet>({
    name: String,
    rotation_period: String,
    orbital_period: String,
    diameter: String,
    climate: String,
    gravity: String,
    terrain: String,
    surface_water: String,
    population: String,
    residents: Array<string>,
    films: Array<string>,
    created: String,
    edited: String,
    url: String,
})

planetSchema.pre<base_planet>('save', function (next) {
    this.name = this.name.toLowerCase();
    console.log(this.name)
    next();
});

const filmSchema = new Schema<film>({
    title: String,
    episode_id: Number,
    opening_crawl: String,
    director: String,
    producer: String,
    release_date: String,
    characters: Array<string>,
    planets: Array<string>,
    starships: Array<string>,
    vehicles: Array<string>,
    species: Array<string>,
    created: String,
    edited: String,
    url: String
})

filmSchema.pre<base_film>('save', function (next) {
    this.title = this.title.toLowerCase();
    this.opening_crawl = this.opening_crawl.toLowerCase();
    this.director = this.director.toLowerCase();
    this.producer = this.producer.toLowerCase();
    next();
});

const starshipSchema = new Schema<starship>({
    name: String,
    model: String,
    manufacturer: String,
    cost_in_credits: String,
    length: String,
    max_atmosphering_speed: String,
    crew: String,
    passengers: String,
    cargo_capacity: String,
    consumables: String,
    hyperdrive_rating: String,
    MGLT: String,
    starship_class: String,
    pilots: Array<string>,
    films: Array<string>,
    created: String,
    edited: String,
    url: String
})

starshipSchema.pre<base_starship>('save', function (next) {
    this.name = this.name.toLowerCase();
    this.model = this.model.toLowerCase();
    this.manufacturer = this.manufacturer.toLowerCase();
    next();
});

const Film = model<film>('Film', filmSchema)
const Specie = model<species>('Specie', specieSchema)
const Vehicle = model<vehicle>('Vehicle', vehicleSchema)
const People = model<base_people>('People', peopleSchema)
const Planet = model<base_planet>('Planet', planetSchema)
const Starship = model<base_people>('Starship', starshipSchema)

const findOneOrCreatePeople = async (subject: Subject) => {
    const people = new People(subject)
    console.log("people.name ", people.name);
    console.log("people.url ", people.url);

    const reg = await People.findOne({ url: people.url }).exec()
    if (!reg) {
        console.log("cadastrando people")
        await people.save()
    }
}
const findOneOrCreateFilm = async (subject: Subject) => {
    const film = new Film(subject)
    const reg = await Film.findOne({ title: film.title }).exec()
    if (!reg) {
        console.log("cadastrando film")
        await film.save()
    }
}
const findOneOrCreatePlanet = async (subject: Subject) => {
    const planet = new Planet(subject)
    const reg = await Planet.findOne({ url: planet.url }).exec()
    if (!reg) {
        console.log("cadastrando planeta")
        await planet.save()
    }
}
const findOneOrCreateStarship = async (subject: Subject) => {
    const starship = new Starship(subject)
    const reg = await Starship.findOne({ url: starship.url }).exec()
    if (!reg) {
        console.log("cadastrando starship")
        await starship.save()
    }
}
const findOneOrCreateVehicle = async (subject: Subject) => {
    const vehicle = new Vehicle(subject)
    const reg = await Vehicle.findOne({ url: vehicle.url }).exec()
    if (!reg) {
        console.log("cadastrando vehicle")
        await vehicle.save()
    }
}
const findOneOrCreateSpecie = async (subject: Subject) => {
    const specie = new Specie(subject)
    const reg = await Specie.findOne({ url: specie.url }).exec()
    if (!reg) {
        console.log("cadastrando specie")
        await specie.save()
    }
}

const write = async (subject: Subject) => {
    if (subject.url.indexOf("people") >= 0) {
        await findOneOrCreatePeople(subject)
    } else if (subject.url.indexOf("films") >= 0) {
        await findOneOrCreateFilm(subject)
    } else if (subject.url.indexOf("planet") >= 0) {
        await findOneOrCreatePlanet(subject)
    } else if (subject.url.indexOf("starship") >= 0) {
        await findOneOrCreateStarship(subject)
    } else if (subject.url.indexOf("vehicle") >= 0) {
        await findOneOrCreateVehicle(subject)
    } else if (subject.url.indexOf("specie") >= 0) {
        await findOneOrCreateSpecie(subject)
    }
}

async function getFromApi(url: string) {
    console.log("Inside")
    try {
        const res = await axios.get(url)
        if (res.status == 404)
            return;

        const subject: Subject = res.data
        const refs: Array<string> = Object.entries(subject).filter(el => {
            if (Array.isArray(el[1])) {
                return true
            } else {
                try {
                    new URL(el[1])
                    return true && el[0] != "url";
                } catch (e) {
                    return false;
                }
            }
        }).map(el => {
            return (el[0])
        })
        await write(subject)
        for (const ref of refs) {
            if (Array.isArray(subject[ref])) {
                for (const link of subject[ref]) {
                    let reg
                    if (link.indexOf("people") >= 0) {
                        reg = await People.findOne({ url: link }).exec()
                    } else if (link.indexOf("planet") >= 0) {
                        reg = await Planet.findOne({ url: link }).exec()
                    } else if (link.indexOf("film") >= 0) {
                        reg = await Film.findOne({ url: link }).exec()
                    } else if (link.indexOf("starship") >= 0) {
                        reg = await Starship.findOne({ url: link }).exec()
                    } else if (link.indexOf("vehicle") >= 0) {
                        reg = await Vehicle.findOne({ url: link }).exec()
                    } else if (link.indexOf("specie") >= 0) {
                        reg = await Specie.findOne({ url: link }).exec()
                    }
                    if (!reg) {
                        await getFromApi(link)
                    }
                }
            } else await getFromApi(subject[ref] as string)
        }
    } catch (error) {
        console.log(error);
    }
}

var entities = {
    // people: 82,
    // planets: 60,
    starships: 36,
    // films: 6,
    // species: 37,
    // vehicles: 39
};
  
console.log("running")
for (const [entity, size] of Object.entries(entities)) {
    for (let index = 1; index <= size; index++) {
        console.log(`current page => ${base} + ${entity}/${index}/`);
        console.log(base + `${entity}/${index}/`);
        await getFromApi(base + `${entity}/${index}/`);
    }
}

console.log("done")
process.exit();
