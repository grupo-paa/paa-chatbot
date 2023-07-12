type people = {
    age: number,
    name: string
}
type justPeople = {
    name: string
}

const p1: people = {age: 1, name: 'teste'}

const p: justPeople = {...p1}