const express = require("express");
const app = express();
const port = 3000;
const mysql = require("mysql");
app.use(express.json());

// /techhunt

var con = mysql.createConnection({
  host: "tap-db.cnfultx0d56f.us-east-1.rds.amazonaws.com",
  user: "admin",
  password: "lZGENKSGyAK7RO6SnAv7",
  port: 3306,
});

con.connect(function (err) {
  if (err) throw err;
  console.log("Connected!");
  con.query("SHOW TABLES;", (e,res, fields)=> console.log(fields))
});

app.post("/one", (req, res) => {
  const { message } = req.body;
  const names = message.split(",");

  // get latest bid
  let billId; // default billId
  con.query("SELECT MAX(BID) AS maxBid FROM USERS", function (error, results, fields) {
    if (error) throw error;

    billId = results[0].maxBid ?? 1;
  });

    let query = "";
    let messageString = "";
    names.forEach((name, index) => {
      nameId[index] = name;
      messageString += `${index} - ${name}\n`;

      query += `INSERT INTO TECHHUNT(id, name, to_pay, bid) VALUES(${billId}, ${index}, ${name}, 0);\n`;
    });

    con.query(query, function (error, results, fields) {
      if (error) throw error;
    });

    // persist billId, name, id

    res.send({
      message: `Cost of food\n${messageString}`,
      next: `http://localhost:3001/two/${billId}`,
    });
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
