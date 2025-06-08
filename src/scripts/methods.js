// Client side logic:

//let directions = ["forwards", "left", "right", "backwards"];

 async function move(direction) {
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({"direction": direction})
    }

    try{
        const response = await fetch("/motor", request);
        const data = await response.json();
        console.log("Direction sent:", direction);
        console.log("Server response:", data);
    } catch (e) {
        console.log(`Request returned an error: ${e}`);
    }

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
