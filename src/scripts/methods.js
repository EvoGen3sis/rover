// Client side logic:

//let directions = ["forwards", "left", "right", "backwards"];
let request = {
    method: "POST", 
    header: {
        "Content-Type": "application/json"
    }, 
    body: JSON.stringify(direction)
}


 async function fetchAPI() {
    let req = await fetch("/motor", request)
    .then()
    .then()
    .catch()
}


/*
async function fetchById(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`); // async operation
    const user = await response.json(); // async operation
    let tuple = []
    tuple.push([user.id, user.name])
    console.log(tuple);
    /* console.log(user.username);
    console.log(user.email); 
}

for (let i = 0; i <= 10; i++){
    fetchById(i);
}
*/
