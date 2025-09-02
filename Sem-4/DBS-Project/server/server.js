// Import necessary modules
require("dotenv").config();
const express = require("express");
const cors = require("cors");
const db = require("./db/index.js");
const jwt = require("jsonwebtoken");
const cookieParser = require("cookie-parser");
const adminRoutes = require("./routes/admin.routes");
const authRoutes = require("./routes/auth.routes");

// Initialize express app
const app = express();

// Use middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.use(adminRoutes);
app.use(authRoutes);

// Start server
app.listen(4000, () => {
  console.log("Server running on port 4000");
});

// everything for manager data from now on
//get all drivers
app.get("/manager/getAllDriver/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    console.log(managerEmail);

    const managerResponse = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    // console.log(managerResponse);
    if (managerResponse.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const managerId = managerResponse.rows[0].manager_id;

    const response = await db.query(
      "SELECT * FROM driver_info WHERE manager_id = $1",
      [managerId]
    );
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        driver: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});
// add driver
app.post("/manager/addDriver", async (req, res) => {
  const {
    driverId,
    name,
    gender,
    contactNumber,
    aadhaarNumber,
    email,
    branch,
    joiningDate,
    salary,
    managerId,
  } = req.body;
  try {
    const queryText =
      "INSERT INTO driver_info VALUES($1, $2, $3, $4, $5, $6, $7 , $8, $9, $10)";
    const queryParams = [
      driverId,
      name,
      gender,
      contactNumber,
      aadhaarNumber,
      email,
      branch,
      joiningDate,
      salary,
      managerId,
    ];
    const response = await db.query(queryText, queryParams);
    res.status(200).json({
      status: "success",
      message: "Driver added successfully",
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error adding data to database");
  }
});

//get all driverstatus
app.get("/manager/getAllDriverStatus/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    const managerResponse = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    // console.log(managerResponse);
    if (managerResponse.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const managerId = managerResponse.rows[0].manager_id;
    // console.log(managerId);

    const response = await db.query(
      "SELECT * FROM driver_status WHERE manager_id = $1",
      [managerId]
    );
    console.log(response);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        driver: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

//delete a driver
app.delete("/manager/driver/:driverId", async (req, res) => {
  const { driverId } = req.params;
  try {
    const response = await db.query(
      "DELETE FROM driver_info WHERE driver_id = $1",
      [driverId]
    );
    res.status(200).json({
      status: "success",
      message: "Driver deleted successfully",
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error deleting data from database");
  }
});

//get all vechiles
app.get("/manager/getAllVehicle/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    const managerResponse = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    // console.log(managerResponse);
    if (managerResponse.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const managerId = managerResponse.rows[0].manager_id;

    //get branch from manager
    const branchResponse = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [managerId]
    );
    console.log(branchResponse.rows[0]);
    const branch = branchResponse.rows[0].branch;
    // console.log(managerId);
    const response = await db.query(
      "SELECT * FROM vehicle_info WHERE branch = $1",
      [branch]
    );
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        vehicle: response.rows,
      },
    });
    console.log(response.rows);
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});
//vechile status
app.get("/manager/getAllVehicleStatus/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    const managerResponse = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    // console.log(managerResponse);
    if (managerResponse.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const managerId = managerResponse.rows[0].manager_id;

    const response = await db.query(
      "SELECT * FROM vehicle_status WHERE manager_id = $1",
      [managerId]
    );
    console.log(response);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        vehicle: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

//get all insurance records
app.get("/manager/getAllInsurance/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    console.log(managerEmail);
    const manager_id = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    const branch = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [manager_id.rows[0].manager_id]
    );
    console.log(branch);
    if (branch.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const Id = branch.rows[0].branch;
    const vehicleid = await db.query(
      "SELECT vehicle_id FROM vehicle_info WHERE branch = $1",
      [Id]
    );
    if (vehicleid.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const vehicleId = vehicleid.rows[0].vehicle_id;
    const response = await db.query(
      "SELECT * FROM insurance_record natural join vehicle_info where branch = $1",
      [Id]
    );
    console.log(response.rows);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        insurance: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

//getall maintaince record
app.get("/manager/getAllMaintenance/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    // console.log(managerEmail);
    const manager_id = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    console.log(manager_id);
    const branch = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [manager_id.rows[0].manager_id]
    );

    console.log(branch);

    const vehicle_id = await db.query(
      "SELECT vehicle_id FROM vehicle_info WHERE branch = $1",
      [branch.rows[0].branch]
    );

    if (vehicle_id.rows.length === 0) {
      return res.status(404).send("Manager not found");
    }
    const vehicleId = vehicle_id.rows[0].vehicle_id;
    const response = await db.query(
      "SELECT * FROM maintenance_record natural join vehicle_info WHERE branch = $1",
      [branch.rows[0].branch]
    );
    console.log(response.rows);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        maintenancesb: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

//get allold vechileinfo
app.get("/manager/getAllOldDriver/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    console.log(managerEmail);
    const manager_id = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    const branch = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [manager_id.rows[0].manager_id]
    );
    console.log(branch);

    const response = await db.query(
      "SELECT * FROM old_driver_info WHERE branch = $1",
      [branch.rows[0].branch]
    );

    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        olddriver: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});
//GET ALL ASSIGNMENTS
app.get("/manager/getAllAssignments/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    console.log(managerEmail);
    const manager_id = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    const branch = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [manager_id.rows[0].manager_id]
    );
    const routeid = await db.query(
      "SELECT route_id FROM route WHERE source_city = $1",
      [branch.rows[0].branch]
    );
    console.log(routeid.rows[0].route_id);
    const response = await db.query(
      "SELECT * FROM assignment WHERE route_id = $1",
      [routeid.rows[0].route_id]
    );
    console.log(response.rows);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        assignments: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});
//get data for old assignment
app.get("/manager/getOldAssignment/:email", async (req, res) => {
  try {
    const managerEmail = req.params.email; // Extract email from request body
    // console.log(managerEmail);
    if (!managerEmail) {
      return res.status(400).send("Manager email is required");
    }
    console.log(managerEmail);
    const manager_id = await db.query(
      "SELECT manager_id FROM manager_login WHERE username = $1",
      [managerEmail]
    );
    const branch = await db.query(
      "SELECT branch FROM manager_info WHERE manager_id = $1",
      [manager_id.rows[0].manager_id]
    );
    const routeid = await db.query(
      "SELECT route_id FROM route WHERE source_city = $1",
      [branch.rows[0].branch]
    );
    console.log(routeid.rows[0].route_id);
    const response = await db.query(
      "SELECT * FROM old_assignment WHERE route_id = $1",
      [routeid.rows[0].route_id]
    );
    console.log(response.rows);
    res.status(200).json({
      status: "success",
      results: response.rows.length,
      data: {
        oldassignments: response.rows,
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});

//add Assignment

// driverId,
// vehicleId,
// RouteId,
// startDate,
// Status,
// returnDate,
app.post("/manager/addAssignment", async (req, res) => {
  try {
    const { driver_id, vehicleId, routeId, startDate, returnDate, status } =
      req.body;
    const response = await db.query(
      "INSERT INTO assignment (driver_id, vehicle_id, route_id, start_date,return_date, status) VALUES ($1, $2, $3, $4, $5) RETURNING *",
      [driver_id, vehicleId, routeId, startDate, returnDate, status]
    );
    res.status(201).json({
      status: "success",
      data: {
        assignment: response.rows[0],
      },
    });
  } catch (error) {
    console.error(error);
    res.status(500).send("Error retrieving data from database");
  }
});
