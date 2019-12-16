let express = require("express")
let bodyparser=require("body-parser")
let R = require("rambda")


let app = express();
app.use(bodyparser.json())
app.use(bodyparser.urlencoded())
app.post('/',(request,response)=>{
    console.log(request.body)
    response.end();
})
app.listen('5000')