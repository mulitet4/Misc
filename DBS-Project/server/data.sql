-- CREATE TABLE city
CREATE TABLE city (
    city VARCHAR(25) PRIMARY KEY
);

INSERT INTO city values('HYDERABAD');
INSERT INTO city values('BENGALURU');
INSERT INTO city values('MUMBAI');
INSERT INTO city values('NEW DELHI');
INSERT INTO city values('CHENNAI');

-- CREATE TABLE manager_login
CREATE TABLE manager_login (
    manager_id SERIAL PRIMARY KEY,
    username VARCHAR(25) NOT NULL,
    passwords VARCHAR(25) NOT NULL
);

-- Set the starting value for manager_id sequence to 1000
ALTER SEQUENCE manager_login_manager_id_seq RESTART WITH 1000;

-- Set the starting value for manager_id sequence to 1000
ALTER SEQUENCE manager_login_manager_id_seq RESTART WITH 1000;

-- Insert statements for manager_login table
INSERT INTO manager_login (manager_id, username, passwords) VALUES (DEFAULT, 'manager1@gmail.com', 'password1');
INSERT INTO manager_login (manager_id, username, passwords) VALUES (DEFAULT, 'manager2@gmail.com', 'password2');
INSERT INTO manager_login (manager_id, username, passwords) VALUES (DEFAULT, 'manager3@gmail.com', 'password3');
INSERT INTO manager_login (manager_id, username, passwords) VALUES (DEFAULT, 'manager4@gmail.com', 'password4');
INSERT INTO manager_login (manager_id, username, passwords) VALUES (DEFAULT, 'manager5@gmail.com', 'password5');



-- CREATE TABLE manager_info
CREATE TABLE manager_info (
    manager_id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    contact BIGINT NOT NULL UNIQUE,
    aadhaar BIGINT NOT NULL UNIQUE,
    email_id VARCHAR(50) NOT NULL,
    branch VARCHAR(25) NOT NULL,
    joining_date DATE NOT NULL,
    salary INTEGER
);

-- Insert statements for manager_info table
INSERT INTO manager_info (manager_id, name, gender, contact, aadhaar, email_id, branch, joining_date, salary) 
VALUES 
(1000, 'SHANKAR VARMA', 'M', 9897243566, 656787981234, 'shankar.varma@gmail.com', 'HYDERABAD', '2020-04-15', 65000),
(1001, 'SRINIVASA HEGDE', 'M', 9899231477, 632312344321, 'srinivasa.hegde@gmail.com', 'BENGALURU', '2020-05-20', 65000),
(1002, 'RAVINDAR SINGH', 'M', 8984856123, 989711343566, 'ravindar.singh@gmail.com', 'MUMBAI', '2020-06-05', 65000),
(1003, 'DAYANAND MURTHY', 'M', 7879345543, 989123546756, 'dayanand.murthy@gmail.com', 'CHENNAI', '2020-08-08', 65000),
(1004, 'ARMAAN KAPUR', 'M', 7875612345, 453412128987, 'armaan.kapur@gmail.com', 'NEW DELHI', '2020-10-25', 65000);


-- CREATE TABLE driver_info
CREATE TABLE driver_info (
    driver_id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    contact BIGINT NOT NULL UNIQUE,
    aadhaar BIGINT NOT NULL UNIQUE,
    license VARCHAR(25) NOT NULL UNIQUE,
    branch VARCHAR(25) NOT NULL,
    joining_date DATE NOT NULL,
    salary INTEGER
);


-- Insert statements for driver_info table
INSERT INTO driver_info (driver_id, name, gender, contact, aadhaar, license, branch, joining_date, salary) 
VALUES 
-- Insert statements for driver_info table
INSERT INTO driver_info (driver_id, name, gender, contact, aadhaar, license, branch, joining_date, salary) 
VALUES 
(5001, 'Ramesh Kumar', 'M', 9876543210, 123456789012, 'TS123456', 'HYDERABAD', '2020-01-15', 30000), -- Valid
(5002, 'Suresh Patel', 'M', 9876543211, 234567890123, 'KA234567', 'BENGALURU', '2020-02-20', 31000), -- Valid
(5003, 'Anita Singh', 'F', 9876543212, 345678901234, 'MH345678', 'MUMBAI', '2020-03-25', 32000), -- Valid
(5004, 'Vijay Sharma', 'M', 9876543213, 456789012345, 'DL456789', 'NEW DELHI', '2020-04-10', 33000), -- Valid
(5005, 'Priya Reddy', 'F', 9876543214, 567890123456, 'TN567890', 'CHENNAI', '2020-05-15', 34000), -- Valid
(5006, 'Amit Kumar', 'M', 9876543215, 678901234567, 'TS678901', 'HYDERABAD', '2020-06-20', 35000), -- Valid
(5007, 'Suman Gupta', 'F', 9876543216, 789012345678, 'KA789012', 'BENGALURU', '2020-07-25', 36000), -- Valid
(5008, 'Rajesh Yadav', 'M', 9876543217, 890123456789, 'MH890123', 'MUMBAI', '2020-08-30', 37000), -- Valid
(5009, 'Pooja Sharma', 'F', 9876543218, 901234567890, 'DL901234', 'NEW DELHI', '2020-09-05', 38000), -- Valid
(5010, 'Sandeep Singh', 'M', 9876543219, 123412341237, 'TN123412', 'CHENNAI', '2020-10-10', 39000), -- Valid
(5011, 'Meera Patel', 'F', 9876543220, 234123412341, 'TS234123', 'HYDERABAD', '2020-11-15', 40000), -- Valid
(5012, 'Ajay Kumar', 'M', 9876543221, 341234123412, 'KA341234', 'BENGALURU', '2020-12-20', 41000), -- Valid
(5013, 'Rani Verma', 'F', 9876543222, 412341234123, 'MH412341', 'MUMBAI', '2021-01-25', 42000), -- Valid
(5014, 'Sunil Kumar', 'M', 9876543223, 123412341236, 'DL123412', 'NEW DELHI', '2021-02-28', 43000), -- Valid
(5015, 'Neha Gupta', 'F', 9876543224, 234123412345, 'TN234123', 'CHENNAI', '2021-03-05', 44000), -- Valid
(5016, 'Vivek Sharma', 'M', 9876543225, 341234123456, 'TS341234', 'HYDERABAD', '2021-04-10', 45000), -- Valid
(5017, 'Divya Patel', 'F', 9876543226, 412341234567, 'KA412341', 'BENGALURU', '2021-05-15', 46000), -- Valid
(5018, 'Rajesh Singh', 'M', 9876543227, 123412341235, 'MH123412', 'MUMBAI', '2021-06-20', 47000); -- Valid



-- CREATE TABLE driver_status
CREATE TABLE driver_status (
    driver_id INT PRIMARY KEY,
    manager_id INT,
    current_location VARCHAR(25) NOT NULL,
    status VARCHAR(25) NOT NULL CHECK (status IN ('BUSY', 'AVL')),
    FOREIGN KEY (driver_id) REFERENCES driver_info(driver_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES manager_info(manager_id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (current_location) REFERENCES city(city) ON UPDATE CASCADE ON DELETE CASCADE
);


-- Insert statements for driver_status table

INSERT INTO driver_status (driver_id, manager_id, current_location, status) 
VALUES 
-- For HYDERABAD branch
(5001, 1000, 'HYDERABAD', 'AVL'),
(5006, 1000, 'HYDERABAD', 'AVL'),
(5011, 1000, 'HYDERABAD', 'AVL'),
(5016, 1000, 'HYDERABAD', 'AVL'),

-- For BENGALURU branch
(5002, 1001, 'BENGALURU', 'AVL'),
(5007, 1001, 'BENGALURU', 'AVL'),
(5012, 1001, 'BENGALURU', 'AVL'),
(5017, 1001, 'BENGALURU', 'AVL'),

-- For MUMBAI branch
(5003, 1002, 'MUMBAI', 'AVL'),
(5008, 1002, 'MUMBAI', 'AVL'),
(5013, 1002, 'MUMBAI', 'AVL'),
(5018, 1002, 'MUMBAI', 'AVL'),

-- For NEW DELHI branch
(5004, 1004, 'NEW DELHI', 'AVL'),
(5009, 1004, 'NEW DELHI', 'AVL'),
(5014, 1004, 'NEW DELHI', 'AVL'),

-- For CHENNAI branch
(5005, 1003, 'CHENNAI', 'AVL'),
(5010, 1003, 'CHENNAI', 'AVL'),
(5015, 1003, 'CHENNAI', 'AVL');




-- CREATE TABLE vehicle_info
CREATE TABLE vehicle_info (
    vehicle_id SERIAL PRIMARY KEY,
    license_plate VARCHAR(25) NOT NULL UNIQUE,
    model VARCHAR(25) NOT NULL,
    commissioned_on DATE NOT NULL,
    mileage INTEGER,
    branch VARCHAR(25) references city(city)
);

-- Insert statements for vehicle_info table
INSERT INTO vehicle_info (vehicle_id, license_plate, model, commissioned_on, mileage, branch) 
VALUES 
(2001, 'TS 09 AB 1234', 'Tata 407 Lorry', '2020-01-01', 7, 'HYDERABAD'),
(2002, 'KA 10 CD 5678', 'Mahindra Bolero Pickup', '2020-02-01', 13, 'BENGALURU'),
(2003, 'MH 47 EF 2345', 'Ashok Leyland Dost', '2020-03-01', 15, 'MUMBAI'),
(2004, 'DL 09 QR 5678', 'Mahindra Furio 12', '2020-04-01', 9, 'NEW DELHI'),
(2005, 'TN 01 OP 1234', 'Tata Xenon Yodha', '2020-05-01', 12, 'CHENNAI'),
(2006, 'Ts 07 DF 3425', 'Tata Ultra 1518', '2020-06-01', 8, 'HYDERABAD'),
(2007, 'KA 20 CD 5678', 'Ashok Leyland Dost', '2020-07-01', 15, 'BENGALURU'),
(2008, 'MH 07 IJ 6789', 'Bharat Benz 1217C', '2020-08-01', 8, 'MUMBAI'),
(2009, 'DL 01 LM 2314', 'Ashok Leyland Captain', '2020-09-01', 7, 'NEW DELHI'),
(2010, 'TN 47 YZ 4536', 'Eicher Pro 6037', '2020-10-01', 7, 'CHENNAI'),
(2011, 'TS 09 ST 9024', 'Bharat Benz 1617R', '2020-11-01', 7, 'HYDERABAD'),
(2012, 'KA 20 AB 7890', 'Tata 407 Lorry', '2020-12-01', 7, 'BENGALURU'),
(2013, 'MH 09 EF 9012', 'Eicher Pro 3015', '2021-01-01', 15, 'MUMBAI'),
(2014, 'DL 09 AB 2345', 'Ashok Leyland Dost', '2021-02-01', 15, 'NEW DELHI'),
(2015, 'TN 07 GH 8765', 'Tata Ace Zip', '2021-03-01', 20, 'CHENNAI');



-- CREATE TABLE vehicle_status
CREATE TABLE vehicle_status (
    vehicle_id INT PRIMARY KEY,
    manager_id INT,
    current_location VARCHAR(25) NOT NULL,
    status VARCHAR(25) NOT NULL CHECK (status IN ('BUSY', 'AVL')),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (manager_id) REFERENCES manager_info(manager_id) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (current_location) REFERENCES city(city) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Insert statements for vehicle_status table
INSERT INTO vehicle_status (vehicle_id, manager_id, current_location, status) 
VALUES 
(2001, 1000, 'HYDERABAD', 'AVL'),
(2002, 1001, 'BENGALURU', 'AVL'),
(2003, 1002, 'MUMBAI', 'AVL'),
(2004, 1004, 'NEW DELHI', 'AVL'),
(2005, 1003, 'CHENNAI', 'AVL'),
(2006, 1000, 'HYDERABAD', 'AVL'),
(2007, 1001, 'BENGALURU', 'AVL'),
(2008, 1002, 'MUMBAI', 'AVL'),
(2009, 1004, 'NEW DELHI', 'AVL'),
(2010, 1003, 'CHENNAI', 'AVL'),
(2011, 1000, 'HYDERABAD', 'AVL'),
(2012, 1001, 'BENGALURU', 'AVL'),
(2013, 1002, 'MUMBAI', 'AVL'),
(2014, 1004, 'NEW DELHI', 'AVL'),
(2015, 1003, 'CHENNAI', 'AVL');


-- CREATE TABLE route
CREATE TABLE route (
    route_id SERIAL PRIMARY KEY,
    source_city VARCHAR(25) NOT NULL,
    destination_city VARCHAR(25) NOT NULL CHECK (destination_city != source_city),
    distance INT,
    FOREIGN KEY (source_city) REFERENCES city(city) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (destination_city) REFERENCES city(city) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Insert statements for route table
INSERT INTO route (route_id, source_city, destination_city, distance) 
VALUES 
(5001, 'HYDERABAD', 'BENGALURU', 575),
(5002, 'HYDERABAD', 'CHENNAI', 673),
(5003, 'HYDERABAD', 'MUMBAI', 710),
(5004, 'HYDERABAD', 'NEW DELHI', 1560),
(6001, 'BENGALURU', 'HYDERABAD', 575),
(6002, 'BENGALURU', 'CHENNAI', 345),
(6003, 'BENGALURU', 'MUMBAI', 983),
(6004, 'BENGALURU', 'NEW DELHI', 2163),
(7001, 'MUMBAI', 'HYDERABAD', 710),
(7002, 'MUMBAI', 'BENGALURU', 983),
(7003, 'MUMBAI', 'NEW DELHI', 1426),
(8001, 'NEW DELHI', 'HYDERABAD', 1560),
(8002, 'NEW DELHI', 'BENGALURU', 2163),
(8003, 'NEW DELHI', 'MUMBAI', 1426),
(9001, 'CHENNAI', 'HYDERABAD', 673),
(9002, 'CHENNAI', 'BENGALURU', 345),
(9003, 'CHENNAI', 'MUMBAI', 1318);


-- CREATE TABLE accident_record
CREATE TABLE accident_record (
    report_id SERIAL PRIMARY KEY,
    vehicle_id INT NOT NULL,
    date DATE NOT NULL,
    damages VARCHAR(100),
    repair_bill INT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Insert statements for accident_record table
INSERT INTO accident_record (vehicle_id, date, damages, repair_bill) 
VALUES 
(2001, '2020-09-01', 'Minor scratches on the body', 5000),
(2002, '2020-10-01', 'Front bumper damage', 8000),
(2003, '2020-11-01', 'Side panel dents', 6000),
(2004, '2021-01-01', 'Rear-end collision', 10000),
(2005, '2021-02-01', 'Broken windshield', 7000);



-- CREATE TABLE insurance_record
CREATE TABLE insurance_record (
    policy_id SERIAL PRIMARY KEY,
    vehicle_id INT NOT NULL,
    policy_number VARCHAR(25) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Insert statements for insurance_record table
INSERT INTO insurance_record (vehicle_id, policy_number, start_date, end_date)
VALUES
(2001, 'INS20010001', '2020-01-02', '2021-01-01'),
(2002, 'INS20010002', '2020-02-02', '2021-02-01'),
(2003, 'INS20010003', '2020-03-02', '2021-03-01'),
(2004, 'INS20010004', '2020-04-02', '2021-04-01'),
(2005, 'INS20010005', '2020-05-02', '2021-05-01'),
(2006, 'INS20010006', '2020-06-02', '2021-06-01'),
(2007, 'INS20010007', '2020-07-02', '2021-07-01'),
(2008, 'INS20010008', '2020-08-02', '2021-08-01'),
(2009, 'INS20010009', '2020-09-02', '2021-09-01'),
(2010, 'INS20010010', '2020-10-02', '2021-10-01'),
(2011, 'INS20010011', '2020-11-02', '2021-11-01'),
(2012, 'INS20010012', '2020-12-02', '2021-12-01'),
(2013, 'INS20010013', '2021-01-02', '2022-01-01'),
(2014, 'INS20010014', '2021-02-02', '2022-02-01'),
(2015, 'INS20010015', '2021-03-02', '2022-03-01');


-- CREATE TABLE maintenance_record
CREATE TABLE maintenance_record (
    maintenance_id SERIAL PRIMARY KEY,
    vehicle_id INT NOT NULL,
    date DATE NOT NULL,
    type VARCHAR(50),
    bill INT NOT NULL,
    description VARCHAR(50),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Insert statements for maintenance_record table
INSERT INTO maintenance_record (vehicle_id, date, type, bill, description)
VALUES 
(2001, '2020-09-01', 'Oil Change', 5000, 'Routine maintenance'),
(2002, '2020-10-01', 'Brake Inspection', 7500, 'Checking brake system'),
(2003, '2020-11-01', 'Engine Service', 10000, 'Engine maintenance'),
(2004, '2020-12-01', 'Electrical Check', 6000, 'Checking electrical components'),
(2005, '2021-01-01', 'Tire Rotation', 8000, 'Rotating tires'),
(2006, '2021-02-01', 'Oil Change', 5500, 'Routine maintenance'),
(2007, '2021-03-01', 'Brake Inspection', 7200, 'Checking brake system'),
(2008, '2021-04-01', 'Engine Service', 9500, 'Engine maintenance'),
(2009, '2021-05-01', 'Electrical Check', 6300, 'Checking electrical components'),
(2010, '2021-06-01', 'Tire Rotation', 8200, 'Rotating tires'),
(2011, '2021-07-01', 'Oil Change', 5200, 'Routine maintenance'),
(2012, '2021-08-01', 'Brake Inspection', 7400, 'Checking brake system'),
(2013, '2021-09-01', 'Engine Service', 9800, 'Engine maintenance'),
(2014, '2021-10-01', 'Electrical Check', 6100, 'Checking electrical components'),
(2015, '2021-11-01', 'Tire Rotation', 8300, 'Rotating tires');


-- CREATE TABLE fuel_transaction_record
-- CREATE TABLE fuel_transaction_record (
--    transaction_id SERIAL PRIMARY KEY,
--    vehicle_id INT NOT NULL,
--    driver_id INT NOT NULL,
--    date DATE NOT NULL,
--    quantity NUMERIC(8,2) NOT NULL,
--    bill INT NOT NULL,
--    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE,
--    FOREIGN KEY (driver_id) REFERENCES driver_info(driver_id) ON UPDATE CASCADE ON DELETE CASCADE
--);



-- CREATE TABLE assignment
CREATE TABLE assignment (
    assignment_id SERIAL PRIMARY KEY,
    vehicle_id INT NOT NULL,
    driver_id INT NOT NULL,
    route_id INT NOT NULL,
    start_date DATE NOT NULL,
    return_date DATE NOT NULL,
    status VARCHAR(25) NOT NULL CHECK (status IN ('ACTIVE', 'DONE')),
    FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (driver_id) REFERENCES driver_info(driver_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (route_id) REFERENCES route(route_id) ON UPDATE CASCADE ON DELETE CASCADE
);



-- Assigning routes for vehicle_id 2001 (HYDERABAD) with driver_id 5001
INSERT INTO assignment VALUES (10001, 2001, 5001, 5001, '2020-01-10', '2020-01-13', 'DONE');

-- Assigning routes for vehicle_id 2001 (HYDERABAD) with driver_id 5006
INSERT INTO assignment VALUES (10002, 2001, 5006, 5002, '2020-06-04', '2020-06-07', 'DONE');

-- Assigning routes for vehicle_id 2001 (HYDERABAD) with driver_id 5011
INSERT INTO assignment VALUES (10003, 2001, 5011, 5003, '2020-11-06', '2020-11-09', 'DONE');

-- Assigning routes for vehicle_id 2001 (HYDERABAD) with driver_id 5016
INSERT INTO assignment VALUES (10004, 2001, 5016, 5004, '2021-04-10', '2021-04-13', 'DONE');

-- Assigning routes for vehicle_id 2006 (HYDERABAD) with driver_id 5001
INSERT INTO assignment VALUES (10005, 2006, 5001, 5001, '2020-02-10', '2020-01-13', 'DONE');

-- Assigning routes for vehicle_id 2006 (HYDERABAD) with driver_id 5006
INSERT INTO assignment VALUES (10006, 2006, 5006, 5002, '2020-07-04', '2020-06-07', 'DONE');

-- Assigning routes for vehicle_id 2006 (HYDERABAD) with driver_id 5011
INSERT INTO assignment VALUES (10007, 2006, 5011, 5003, '2020-12-06', '2020-11-09', 'DONE');

-- Assigning routes for vehicle_id 2006 (HYDERABAD) with driver_id 5016
INSERT INTO assignment VALUES (10008, 2006, 5016, 5004, '2021-05-10', '2021-04-13', 'DONE');

-- Assigning routes for vehicle_id 2011 (HYDERABAD) with driver_id 5001
INSERT INTO assignment VALUES (10009, 2011, 5001, 5001, '2020-03-10', '2020-01-13', 'DONE');

-- Assigning routes for vehicle_id 2011 (HYDERABAD) with driver_id 5006
INSERT INTO assignment VALUES (10010, 2011, 5006, 5002, '2020-08-04', '2020-06-07', 'DONE');

-- Assigning routes for vehicle_id 2011 (HYDERABAD) with driver_id 5011
INSERT INTO assignment VALUES (10011, 2011, 5011, 5003, '2021-01-06', '2020-11-09', 'DONE');

-- Assigning routes for vehicle_id 2011 (HYDERABAD) with driver_id 5016
INSERT INTO assignment VALUES (10012, 2011, 5016, 5004, '2021-06-10', '2021-04-13', 'DONE');


-- Assigning routes for vehicle_id 2002 (BENGALURU) with driver_id 5002
INSERT INTO assignment VALUES (10013, 2002, 5002, 6001, '2020-02-20', '2020-02-23', 'DONE');

-- Assigning routes for vehicle_id 2002 (BENGALURU) with driver_id 5007
INSERT INTO assignment VALUES (10014, 2002, 5007, 6002, '2020-07-25', '2020-07-30', 'DONE');

-- Assigning routes for vehicle_id 2002 (BENGALURU) with driver_id 5012
INSERT INTO assignment VALUES (10015, 2002, 5012, 6003, '2020-12-20', '2020-12-27', 'DONE');

-- Assigning routes for vehicle_id 2002 (BENGALURU) with driver_id 5017
INSERT INTO assignment VALUES (10016, 2002, 5017, 6004, '2021-05-15', '2021-05-25', 'DONE');

-- Assigning routes for vehicle_id 2007 (BENGALURU) with driver_id 5002
INSERT INTO assignment VALUES (10017, 2007, 5002, 6001, '2020-03-20', '2020-03-23', 'DONE');

-- Assigning routes for vehicle_id 2007 (BENGALURU) with driver_id 5007
INSERT INTO assignment VALUES (10018, 2007, 5007, 6002, '2020-08-25', '2020-08-30', 'DONE');

-- Assigning routes for vehicle_id 2007 (BENGALURU) with driver_id 5012
INSERT INTO assignment VALUES (10019, 2007, 5012, 6003, '2021-01-20', '2021-01-27', 'DONE');

-- Assigning routes for vehicle_id 2007 (BENGALURU) with driver_id 5017
INSERT INTO assignment VALUES (10020, 2007, 5017, 6004, '2021-06-15', '2021-06-25', 'DONE');

-- Assigning routes for vehicle_id 2012 (BENGALURU) with driver_id 5002
INSERT INTO assignment VALUES (10021, 2012, 5002, 6001, '2020-04-20', '2020-04-23', 'DONE');

-- Assigning routes for vehicle_id 2012 (BENGALURU) with driver_id 5007
INSERT INTO assignment VALUES (10022, 2012, 5007, 6002, '2020-09-25', '2020-09-30', 'DONE');

-- Assigning routes for vehicle_id 2012 (BENGALURU) with driver_id 5012
INSERT INTO assignment VALUES (10023, 2012, 5012, 6003, '2021-02-20', '2021-02-27', 'DONE');

-- Assigning routes for vehicle_id 2012 (BENGALURU) with driver_id 5017
INSERT INTO assignment VALUES (10024, 2012, 5017, 6004, '2021-07-15', '2021-07-25', 'DONE');


-- Assigning routes for vehicle_id 2003 (MUMBAI) with driver_id 5003
INSERT INTO assignment VALUES (10025, 2003, 5003, 7001, '2020-03-25', '2020-03-30', 'DONE');

-- Assigning routes for vehicle_id 2003 (MUMBAI) with driver_id 5008
INSERT INTO assignment VALUES (10026, 2003, 5008, 7002, '2020-08-30', '2020-09-05', 'DONE');

-- Assigning routes for vehicle_id 2003 (MUMBAI) with driver_id 5013
INSERT INTO assignment VALUES (10027, 2003, 5013, 7003, '2021-01-25', '2021-02-01', 'DONE');

-- Assigning routes for vehicle_id 2003 (MUMBAI) with driver_id 5018
INSERT INTO assignment VALUES (10028, 2003, 5018, 7001, '2021-06-20', '2021-06-30', 'DONE');

-- Assigning routes for vehicle_id 2008 (MUMBAI) with driver_id 5003
INSERT INTO assignment VALUES (10029, 2008, 5003, 7001, '2020-04-30', '2020-05-05', 'DONE');

-- Assigning routes for vehicle_id 2008 (MUMBAI) with driver_id 5008
INSERT INTO assignment VALUES (10030, 2008, 5008, 7002, '2020-09-30', '2020-10-05', 'DONE');

-- Assigning routes for vehicle_id 2008 (MUMBAI) with driver_id 5013
INSERT INTO assignment VALUES (10031, 2008, 5013, 7003, '2021-02-27', '2021-03-02', 'DONE');

-- Assigning routes for vehicle_id 2008 (MUMBAI) with driver_id 5018
INSERT INTO assignment VALUES (10032, 2008, 5018, 7002, '2021-07-30', '2021-08-09', 'DONE');

-- Assigning routes for vehicle_id 2013 (MUMBAI) with driver_id 5003
INSERT INTO assignment VALUES (10033, 2013, 5003, 7001, '2020-05-25', '2020-06-01', 'DONE');

-- Assigning routes for vehicle_id 2013 (MUMBAI) with driver_id 5008
INSERT INTO assignment VALUES (10034, 2013, 5008, 7002, '2020-10-25', '2020-11-05', 'DONE');

-- Assigning routes for vehicle_id 2013 (MUMBAI) with driver_id 5013
INSERT INTO assignment VALUES (10035, 2013, 5013, 7003, '2021-03-25', '2021-04-01', 'DONE');

-- Assigning routes for vehicle_id 2013 (MUMBAI) with driver_id 5018
INSERT INTO assignment VALUES (10036, 2013, 5018, 7003, '2021-08-25', '2021-09-04', 'DONE');


-- Assigning routes for vehicle_id 2004 (NEW DELHI) with driver_id 5004
INSERT INTO assignment VALUES (10037, 2004, 5004, 8001, '2020-04-10', '2020-04-17', 'DONE');

-- Assigning routes for vehicle_id 2004 (NEW DELHI) with driver_id 5009
INSERT INTO assignment VALUES (10038, 2004, 5009, 8002, '2020-09-05', '2020-09-15', 'DONE');

-- Assigning routes for vehicle_id 2004 (NEW DELHI) with driver_id 5014
INSERT INTO assignment VALUES (10039, 2004, 5014, 8003, '2021-02-27', '2021-03-06', 'DONE');

-- Assigning routes for vehicle_id 2004 (NEW DELHI) with driver_id 5018
INSERT INTO assignment VALUES (10040, 2004, 5018, 8001, '2021-07-25', '2021-08-01', 'DONE');

-- Assigning routes for vehicle_id 2009 (NEW DELHI) with driver_id 5004
INSERT INTO assignment VALUES (10041, 2009, 5004, 8001, '2020-05-01', '2020-05-08', 'DONE');

-- Assigning routes for vehicle_id 2009 (NEW DELHI) with driver_id 5009
INSERT INTO assignment VALUES (10042, 2009, 5009, 8002, '2020-10-01', '2020-10-08', 'DONE');

-- Assigning routes for vehicle_id 2009 (NEW DELHI) with driver_id 5014
INSERT INTO assignment VALUES (10043, 2009, 5014, 8003, '2021-03-01', '2021-03-08', 'DONE');

-- Assigning routes for vehicle_id 2009 (NEW DELHI) with driver_id 5018
INSERT INTO assignment VALUES (10044, 2009, 5018, 8002, '2021-08-01', '2021-08-11', 'DONE');

-- Assigning routes for vehicle_id 2014 (NEW DELHI) with driver_id 5004
INSERT INTO assignment VALUES (10045, 2014, 5004, 8001, '2020-06-01', '2020-06-08', 'DONE');

-- Assigning routes for vehicle_id 2014 (NEW DELHI) with driver_id 5009
INSERT INTO assignment VALUES (10046, 2014, 5009, 8002, '2020-11-01', '2020-11-08', 'DONE');

-- Assigning routes for vehicle_id 2014 (NEW DELHI) with driver_id 5014
INSERT INTO assignment VALUES (10047, 2014, 5014, 8003, '2021-04-01', '2021-04-08', 'DONE');

-- Assigning routes for vehicle_id 2014 (NEW DELHI) with driver_id 5018
INSERT INTO assignment VALUES (10048, 2014, 5018, 8003, '2021-09-01', '2021-09-08', 'DONE');


-- Assigning routes for vehicle_id 2005 (CHENNAI) with driver_id 5005
INSERT INTO assignment VALUES (10049, 2005, 5005, 9001, '2020-05-15', '2020-05-20', 'DONE');

-- Assigning routes for vehicle_id 2005 (CHENNAI) with driver_id 5010
INSERT INTO assignment VALUES (10050, 2005, 5010, 9002, '2020-10-10', '2020-10-13', 'DONE');

-- Assigning routes for vehicle_id 2005 (CHENNAI) with driver_id 5015
INSERT INTO assignment VALUES (10051, 2005, 5015, 9003, '2021-03-05', '2021-03-12', 'DONE');

-- Assigning routes for vehicle_id 2010 (CHENNAI) with driver_id 5005
INSERT INTO assignment VALUES (10052, 2010, 5005, 9001, '2020-06-15', '2020-06-20', 'DONE');

-- Assigning routes for vehicle_id 2010 (CHENNAI) with driver_id 5010
INSERT INTO assignment VALUES (10053, 2010, 5010, 9002, '2020-11-10', '2020-11-13', 'DONE');

-- Assigning routes for vehicle_id 2010 (CHENNAI) with driver_id 5015
INSERT INTO assignment VALUES (10054, 2010, 5015, 9003, '2021-04-05', '2021-04-12', 'DONE');

-- Assigning routes for vehicle_id 2015 (CHENNAI) with driver_id 5005
INSERT INTO assignment VALUES (10055, 2015, 5005, 9001, '2020-07-15', '2020-07-20', 'DONE');

-- Assigning routes for vehicle_id 2015 (CHENNAI) with driver_id 5010
INSERT INTO assignment VALUES (10056, 2015, 5010, 9002, '2020-12-10', '2020-12-13', 'DONE');

-- Assigning routes for vehicle_id 2015 (CHENNAI) with driver_id 5015
INSERT INTO assignment VALUES (10057, 2015, 5015, 9003, '2021-05-05', '2021-05-12', 'DONE');


-- Tables for triggers

CREATE TABLE old_vehicle_info (
    vehicle_id SERIAL PRIMARY KEY,
    license_plate VARCHAR(25) NOT NULL UNIQUE,
    model VARCHAR(25) NOT NULL,
    commissioned_on DATE NOT NULL,
    mileage INTEGER,
    branch VARCHAR(25) references city(city)
);


CREATE TABLE old_manager_info (
    manager_id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    contact BIGINT NOT NULL UNIQUE,
    aadhaar BIGINT NOT NULL UNIQUE,
    email_id VARCHAR(50) NOT NULL,
    branch VARCHAR(25) NOT NULL,
    joining_date DATE NOT NULL,
    salary INTEGER
);

CREATE TABLE old_driver_info (
    driver_id SERIAL PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
    contact BIGINT NOT NULL UNIQUE,
    aadhaar BIGINT NOT NULL UNIQUE,
    license VARCHAR(25) NOT NULL UNIQUE,
    branch VARCHAR(25) NOT NULL,
    joining_date DATE NOT NULL,
    salary INTEGER
);


-- CREATE TABLE old_assignment
CREATE TABLE old_assignment (
    assignment_id SERIAL PRIMARY KEY,
    vehicle_id INT NOT NULL,
    driver_id INT NOT NULL,
    route_id INT NOT NULL,
    start_date DATE NOT NULL,
    return_date DATE NOT NULL,
    status VARCHAR(25) NOT NULL CHECK (status IN ('ACTIVE', 'DONE')),
    -- FOREIGN KEY (vehicle_id) REFERENCES vehicle_info(vehicle_id) ON UPDATE CASCADE ON DELETE CASCADE,
    -- FOREIGN KEY (driver_id) REFERENCES driver_info(driver_id) ON UPDATE CASCADE ON DELETE CASCADE,
    -- FOREIGN KEY (route_id) REFERENCES route(route_id) ON UPDATE CASCADE ON DELETE CASCADE
);

