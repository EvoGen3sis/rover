// Client side logic:

let directions = ["forwards", "left", "right", "backwards", ]

/* function fetchAPI() {
    fetch("/motor", {

    })
    .then(re)
    .then()
    .catch()
}
*/

async function fetcher() {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = response.json();
    console.log(data);
}

fetcher();
