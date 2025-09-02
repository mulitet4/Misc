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
  //   const [gender, setGender] = useState("");
  const [driverId, setDriverId] = useState("");
  const [vehicleId, setVehicleId] = useState("");
  const [routeId, setRouteId] = useState("");
  //   const [aadhaarNumber, setAadhaarNumber] = useState("");
  //   const [email, setEmail] = useState("");
  //   const [branch, setBranch] = useState("");
  const [startDate, setStartDate] = useState("");
  const [status, setStatus] = useState("");
  const [returnDate, setReturnDate] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const userData = {
      driverId,
      vehicleId,
      routeId,
      startDate,
      status,
      returnDate,
    };
    console.log("Form Data:", userData);

    // Example POST request with fetch API
    try {
      const response = await fetch(
        `http://localhost:4000/manager/addAssignment/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(userData),
        }
      );
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
        <Button size="sm">Add Assigment</Button>
      </DialogTrigger>
      <DialogContent className="p-0">
        <Card>
          <CardHeader className="p-4">
            <CardTitle>Add Assigment</CardTitle>
            <CardDescription>
              Add Assigment Details and Click Save
            </CardDescription>
          </CardHeader>
          <CardContent className="p-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <Label htmlFor="DriverId">Driver ID</Label>
                <Input
                  id="DriverId"
                  placeholder="DriverId"
                  value={driverId}
                  onChange={(e) => setDriverId(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="VehicleId">Vehicle Id</Label>
                <Input
                  id="VehicleId"
                  placeholder="VehicleId"
                  value={vehicleId}
                  onChange={(e) => setVehicleId(e.target.value.toUpperCase())}
                  required
                />
              </div>
              <div>
                <Label htmlFor="RouteId">Route Id</Label>
                <Input
                  id="RouteId"
                  placeholder="Route Id"
                  value={routeId}
                  onChange={(e) => setRouteId(e.target.value)}
                  required
                />
              </div>{" "}
              <div>
                <Label htmlFor="startDate">Start date</Label>
                <Input
                  id="startDate"
                  type="date"
                  value={startDate}
                  onChange={(e) => setStartDate(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="returnDate">Return date</Label>
                <Input
                  id="Return date"
                  type="date"
                  value={returnDate}
                  onChange={(e) => setReturnDate(e.target.value)}
                  required
                />
              </div>
              <div>
                <Label htmlFor="email">Status</Label>
                <Input
                  id="Status"
                  placeholder="Status"
                  type="text"
                  value={status}
                  onChange={(e) => setStatus(e.target.value)}
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
