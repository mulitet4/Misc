const express = require("express");
const router = express.Router();
const db = require("../db/index.js");

// Login route remains unchanged as it's not specific to managers only
router.post("/login", async (req, res) => {
  const { email, password } = req.body;
  try {
    const queryText = "SELECT * FROM manager_login WHERE username = $1";
    const { rows } = await db.query(queryText, [email]);
    if (rows.length > 0) {
      const user = rows[0];
      const isValid = password === user.passwords; // For plain text comparison
      if (isValid) {
        const token = jwt.sign({ email }, process.env.JWT_SECRET, {
          expiresIn: "1h",
        });
        res.status(200).json({ email, token });
      } else {
        res.status(401).json({ message: "Invalid email or password" });
      }
    } else {
      res.status(401).json({ message: "Invalid email or password" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ detail: error.detail });
  }
});

module.exports = router;
