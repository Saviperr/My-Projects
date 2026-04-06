const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(bodyParser.json());

const db = mysql.createConnection({
  host: "RDS-ENDPOINT",
  user: "admin",
  password: "password123",
  database: "userdata"
});

db.connect(err => {
  if (err) console.log("DB connection failed");
  else console.log("Connected to DB");
});

app.post("/submit-data", (req, res) => {
  const {name,email} = req.body;
  const sql = "INSERT INTO users (name,email) VALUES (?,?)";

  db.query(sql,[name,email],(err,result)=>{
    if(err) res.send(err);
    else res.send("Data stored successfully");
  });
});

app.listen(80,()=> console.log("Server running on port 80"));
