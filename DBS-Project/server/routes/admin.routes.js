const express = require("express");
const router = express.Router();
const db = require("../db/index.js");

// Get all list of managers from database with new route
router.get("/admin/manager", async (req, res) => {
  try {
    const response = await db.query("SELECT * FROM manager_info");
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        manager: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

// Delete manager from database with new route
router.delete("/admin/manager/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const response = await db.query(
      "DELETE FROM manager_info WHERE manager_id = $1",
      [id]
    );
    res.status(200).json({
      status: "success",
      message: "Manager deleted successfully",
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error deleting data from database");
  }
});

// Add manager to database with new route
router.post("/admin/manager", async (req, res) => {
  const {
    managerId,
    name,
    gender,
    contactNumber,
    aadhaarNumber,
    email,
    branch,
    salary,
    joiningDate,
  } = req.body;
  try {
    const queryText =
      "INSERT INTO manager_info VALUES($1, $2, $3, $4, $5, $6, $7 , $8, $9)";
    const queryParams = [
      managerId,
      name,
      gender,
      contactNumber,
      aadhaarNumber,
      email,
      branch,
      joiningDate,
      salary,
    ];
    const queryText2 =
      "INSERT INTO manager_login VALUES($1, $2, $3, $4, $5, $6, $7 , $8, $9)";
    const queryParams2 = [
      managerId,
      name,
      gender,
      contactNumber,
      aadhaarNumber,
      email,
      branch,
      joiningDate,
      salary,
    ];
    const response = await db.query(queryText, queryParams);
    res.status(200).json({
      status: "success",
      message: "Manager added successfully",
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error adding data to database");
  }
});

module.exports = router;
