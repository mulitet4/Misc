import { Link } from "react-router-dom";
import React from "react";

import { Button } from "../ui/button";
import {
  DropdownMenuTrigger,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuItem,
  DropdownMenuContent,
  DropdownMenu,
} from "../ui/dropdown-menu";
import {
  TableHead,
  TableRow,
  TableHeader,
  TableCell,
  TableBody,
  Table,
} from "../ui/table";
// import { Badge } from "../../Components/ui/badge";
import { useEffect, useState } from "react";
import AddUserModal from "./AddUsermodal/AddUsermodal";
// import { authToken } from "../../Auth/Auth";
import { useCookies } from "react-cookie";
import { LineChartIcon, SettingsIcon } from "lucide-react";

export default function Manager2() {
  // const [showModal, setShowModal] = useState(false);
  const [drivers, setDrivers] = useState([]);
  const [cookies, setCookie, removeCookie] = useCookies();

  const handleLogout = async (id: any) => {
    removeCookie("authToken");
    removeCookie("Email");
    window.location.href = "/auth";
  };

  const getData = async () => {
    try {
      console.log("hello");
      // Encode the manager's email to ensure it's safe to include in a URL
      const managerEmail = cookies.Email;
      console.log(managerEmail);
      // const url = `http://localhost:4000/manager/getAllDriver/${managerEmail}`;
      const url = `http://localhost:4000/manager/getAllDriverStatus/${encodeURIComponent(
        managerEmail
      )}`;
      console.log(url);

      const response = await fetch(url, {
        method: "GET", // Correct method
        headers: {
          "Content-Type": "application/json",
        },
        // Removed the body property since GET requests cannot have a body
      });
      console.log(response);
      const data = await response.json();
      //   console.log(data);
      const drivers = data.data.driver;
      //   console.log(drivers);
      setDrivers(drivers);
    } catch (e) {
      //   console.error(e);
    }
  };
  // console.log(manager);
  useEffect(() => {
    getData();
  }, [setDrivers]);

  // console.log(manager);
  //handleDelete
  const handleDelete = async (id: any) => {
    try {
      const response = await fetch(
        `http://localhost:4000/manager/driver/${id}`,
        {
          method: "DELETE",
        }
      );
      const data = await response.json();
      console.log(data);
      getData();
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <div className="grid min-h-screen w-full grid-cols-[280px_1fr]">
      <div className="hidden border-r bg-black lg:block dark:bg-black-800/40 dark:border-black-800/20">
        <div className="flex h-full max-h-screen flex-col gap-2">
          <div className="flex h-[60px] items-center border-b px-6">
            <Link className="flex items-center gap-2 font-semibold" to="#">
              <MountainIcon className="h-6 w-6 text-white" />
              <span className="text-gray-50">SriKrishna Logistics</span>
            </Link>
            <Button
              className="ml-auto h-8 w-8 translate-y-1"
              size="icon"
              variant="outline"
            >
              <BellIcon className="h-4 w-4 text-white" />
              <span className="sr-only">Toggle notifications</span>
            </Button>
          </div>
          <div className="flex-1 overflow-auto py-2">
            <nav className="grid items-start px-4 text-sm font-medium">
              <Link
                className="flex items-center gap-3 rounded-lg bg-black-100 px-3 py-2 text-gray-900 transition-all hover:text-gray-900 dark:text-gray-50 dark:hover:text-gray-50"
                to="/Manager"
              >
                <UsersIcon className="h-4 w-4" />
                Drivers
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="#"
              >
                <LineChartIcon className="h-4 w-4" />
                Drivers Status
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/vehicle"
              >
                <SettingsIcon className="h-4 w-4" />
                Vehicles
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/vehiclestatus"
              >
                <SettingsIcon className="h-4 w-4" />
                Vehicle Status
              </Link>

              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/insurancerecord"
              >
                <SettingsIcon className="h-4 w-4" />
                Insurance Record
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/Maintainancerecord"
              >
                <SettingsIcon className="h-4 w-4" />
                Maintenance Record
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/OldDriver"
              >
                <SettingsIcon className="h-4 w-4" />
                Old Drivers
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/Assignment"
              >
                <SettingsIcon className="h-4 w-4" />
                Assignment
              </Link>
              <Link
                className="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-500 transition-all hover:text-gray-900 dark:text-gray-400 dark:hover:text-gray-50"
                to="/Manager/OldAssignment"
              >
                <SettingsIcon className="h-4 w-4" />
                Old Assignment
              </Link>
            </nav>
          </div>
        </div>
      </div>
      <div className="flex flex-col">
        <header className="flex h-14 lg:h-[60px] items-center gap-4 border-b bg-black-100/40 px-6 dark:bg-black-800/40">
          <Link className="lg:hidden" to="#">
            <MountainIcon className="h-6 w-6" />
            <span className="sr-only">Home</span>
          </Link>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button
                className="rounded-full border border-gray-200 w-8 h-8 dark:border-gray-800"
                size="icon"
                variant="ghost"
              >
                <img
                  alt="Avatar"
                  className="rounded-full"
                  height="32"
                  src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=facearea&facepad=2&w=300&h=300&q=80"
                  style={{
                    aspectRatio: "32/32",
                    objectFit: "cover",
                  }}
                  width="32"
                />
                <span className="sr-only">Toggle user menu</span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="min-w-36">
              <DropdownMenuLabel>My Account</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuItem>Settings</DropdownMenuItem>
              <DropdownMenuItem>Support</DropdownMenuItem>
              <DropdownMenuSeparator />
              <DropdownMenuItem>
                <Link to="#" onClick={handleLogout}>
                  Logout
                </Link>
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </header>
        <main className="flex flex-1 flex-col gap-4 p-4 md:gap-8 md:p-6">
          <div className="flex items-center">
            <h1 className="font-semibold text-lg md:text-2xl">Drivers</h1>
            {/* <Button className="ml-auto scale-95 border-black " size="sm">
              Add User
            </Button> */}
            {/* <React.Fragment className="ml-auto scale-95 border-black "> */}
            <div className="ml-auto scale-95 border-black">
              <AddUserModal />
            </div>

            {/* </React.Fragment> */}
          </div>
          <div className="border shadow-sm rounded-lg">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className=" bg-black">driver_id</TableHead>
                  <TableHead className=" bg-black">branch</TableHead>
                  <TableHead className=" bg-black">currentLocation</TableHead>
                  <TableHead className=" bg-black">Status</TableHead>
                  <TableHead className="text-right bg-black">Actions</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {drivers.map(
                  (item: {
                    driver_id: number;
                    name: string;
                    salary: number;
                    license: string;
                    contact: string;
                  }) => {
                    return (
                      <TableRow key={item.driver_id}>
                        <TableCell className="font-medium">
                          {item.driver_id}
                        </TableCell>
                        <TableCell>{item.branch}</TableCell>
                        <TableCell>{item.current_location}</TableCell>
                        <TableCell>{item.status}</TableCell>
                        <TableCell className="text-right">
                          <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                              <Button size="icon" variant="ghost">
                                <MoreHorizontalIcon className="h-4 w-4" />
                                <span className="sr-only">User actions</span>
                              </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end">
                              {/* <DropdownMenuItem>Edit</DropdownMenuItem> */}
                              {/* <DropdownMenuItem>Update</DropdownMenuItem> */}
                              <DropdownMenuItem
                                onClick={() => handleDelete(item.driver_id)}
                              >
                                Delete
                              </DropdownMenuItem>
                            </DropdownMenuContent>
                          </DropdownMenu>
                        </TableCell>
                      </TableRow>
                    );
                  }
                )}
              </TableBody>
            </Table>
          </div>
        </main>
      </div>
    </div>
  );
}

function BellIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9" />
      <path d="M10.3 21a1.94 1.94 0 0 0 3.4 0" />
    </svg>
  );
}

// function LineChartIcon(props: React.SVGProps<SVGSVGElement>) {
//   return (
//     <svg
//       {...props}
//       xmlns="http://www.w3.org/2000/svg"
//       width="24"
//       height="24"
//       viewBox="0 0 24 24"
//       fill="none"
//       stroke="currentColor"
//       strokeWidth="2"
//       strokeLinecap="round"
//       strokeLinejoin="round"
//     >
//       <path d="M3 3v18h18" />
//       <path d="m19 9-5 5-4-4-3 3" />
//     </svg>
//   );
// }

function MoreHorizontalIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="1" />
      <circle cx="19" cy="12" r="1" />
      <circle cx="5" cy="12" r="1" />
    </svg>
  );
}

export function MountainIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}

// function SettingsIcon(props: React.SVGProps<SVGSVGElement>) {
//   return (
//     <svg
//       {...props}
//       xmlns="http://www.w3.org/2000/svg"
//       width="24"
//       height="24"
//       viewBox="0 0 24 24"
//       fill="none"
//       stroke="currentColor"
//       strokeWidth="2"
//       strokeLinecap="round"
//       strokeLinejoin="round"
//     >
//       <path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z" />
//       <circle cx="12" cy="12" r="3" />
//     </svg>
//   );
// }

function UsersIcon(props: React.SVGProps<SVGSVGElement>) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
      <circle cx="9" cy="7" r="4" />
      <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
      <path d="M16 3.13a4 4 0 0 1 0 7.75" />
    </svg>
  );
}
