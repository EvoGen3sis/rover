// Client side logic:

let directions = ["forwards", "left", "right", "backwards"]

/* function fetchAPI() {
    fetch("/motor", {

    })
    .then(re)
    .then()
    .catch()
}
*/

async function fetchById(id) {
    const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`); // async operation
    const data = await response.json(); // async operation
    //const user = data.find(user => user.id === id);
    console.log(data);
}
