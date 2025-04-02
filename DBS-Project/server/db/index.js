const { Pool } = require("pg");

const pool = new Pool({ connectionString: process.env.DATABASE_URL });

// Exporting the query function using module.exports
module.exports.query = (text, params) => pool.query(text, params);
