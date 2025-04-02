import { Button } from "../../ui/button";
import { DialogTrigger, DialogContent, Dialog } from "../../ui/dialog";
import {
  CardTitle,
  CardDescription,
  CardHeader,
  CardContent,
  CardFooter,
  Card,
} from "../../ui/card";
import { Label } from "../../ui/label";
import { Input } from "../../ui/input";
import {
  DropdownMenuTrigger,
  DropdownMenuRadioItem,
  DropdownMenuRadioGroup,
  DropdownMenuContent,
  DropdownMenu,
} from "../../ui/dropdown-menu";
import { RadioGroupItem, RadioGroup } from "../../ui/radio-group";
import { useState } from "react";

export default function AddUsermodal() {
  const [gender, setGender] = useState("");
  const [driverId, setDriverId] = useState("");
  const [name, setName] = useState("");
  const [contactNumber, setContactNumber] = useState("");
  const [aadhaarNumber, setAadhaarNumber] = useState("");
  const [email, setEmail] = useState("");
  const [branch, setBranch] = useState("");
  const [joiningDate, setJoiningDate] = useState("");
  const [salary, setSalary] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const userData = {
      driverId,
      name,
      gender,
      contactNumber,
      aadhaarNumber,
      email,
      branch,
      joiningDate,
      salary,
    };
    console.log("Form Data:", userData);

    // Example POST request with fetch API
    try {
      const response = await fetch(`http://localhost:4000/manager/addDriver/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });
      if (response.ok) {
        const jsonResponse = await response.json();
        console.log("Success:", jsonResponse);
        // Handle success response
      } else {
        console.error("Error:", response.statusText);
        // Handle error response
      }
    } catch (error) {
      console.error("Error:", error);
      // Handle network errors
    }
  };

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button size="sm">Add User</Button>
      </DialogTrigger>
      <DialogContent className="p-0">
        <Card>
          <CardHeader className="p-4">
            <CardTitle>Add Driver</CardTitle>
            <CardDescription>
              Add the driver information and click Save.
            </CardDescription>
          </CardHeader>
          <CardContent className="p-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <Label htmlFor="manager-id">Driver ID</Label>
                <Input
                  id="manager-id"
                  placeholder="Manager ID"
                  value={driverId}
                  onChange={(e) => setDriverId(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="name">Name</Label>
                <Input
                  id="name"
                  placeholder="Name"
                  value={name}
                  onChange={(e) => setName(e.target.value.toUpperCase())}
                  required
                />
              </div>
              <div>
                <Label htmlFor="contact-number">Contact number</Label>
                <Input
                  id="contact-number"
                  placeholder="Contact number"
                  value={contactNumber}
                  onChange={(e) => setContactNumber(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="aadhaar-number">Aadhaar number</Label>
                <Input
                  id="aadhaar-number"
                  placeholder="Aadhaar number"
                  type="number"
                  value={aadhaarNumber}
                  onChange={(e) => setAadhaarNumber(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="gender">Gender</Label>
                <Input
                  id="gender"
                  placeholder="gender"
                  type="text"
                  value={gender}
                  maxLength={1}
                  onChange={(e) => setGender(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  placeholder="Email"
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="branch">Branch</Label>
                <Input
                  id="branch"
                  placeholder="Branch"
                  value={branch}
                  required
                  onChange={(e) => setBranch(e.target.value.toUpperCase())}
                />
              </div>
              <div>
                <Label htmlFor="joining-date">Joining date</Label>
                <Input
                  id="joining-date"
                  type="date"
                  value={joiningDate}
                  onChange={(e) => setJoiningDate(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="salary">Salary</Label>
                <Input
                  id="salary"
                  placeholder="Salary"
                  type="number"
                  value={salary}
                  onChange={(e) => setSalary(e.target.value)}
                  required
                />
              </div>
            </div>
          </CardContent>
          <CardFooter className="p-4 flex items-center justify-end">
            <Button type="submit" onClick={handleSubmit}>
              Save
            </Button>
          </CardFooter>
        </Card>
      </DialogContent>
    </Dialog>
  );
}
