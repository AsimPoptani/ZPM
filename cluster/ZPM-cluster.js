let express = require("express");
let bodyParser = require("body-parser");
let R = require("rambda");
const low = require("lowdb");
const FileSync = require("lowdb/adapters/FileSync");


// Setup server
let app = express();

// Setup database
const adapter = new FileSync("db.json");
const db = low(adapter);
db.defaults({ servers: [], ids:[] }).write();


app.use(bodyParser.json());
app.use(bodyParser.urlencoded());

app.post("/", (request, response) => {
  db.get("servers")
    .push(request.body)
    .write();
  response.end();
});
app.get("/getID", (request, response) => {
  response.send();
  response.end();
});
app.listen("5000");
