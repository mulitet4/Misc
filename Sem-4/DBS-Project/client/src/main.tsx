import React from "react";
import ReactDOM from "react-dom/client";
import Background from "./Components/AuroraBackground/Background";
import "./index.css";
import {
  RouterProvider,
  createBrowserRouter,
  Navigate,
} from "react-router-dom";
import Admin from "./Components/Admin/Admin";
import Manager from "./Components/Manager/Manager";
import { Auth } from "./Components/Auth/Auth"; // Ensure this is a component for rendering
import RequireAuth from "./Components/Auth/RequireAuth"; // Import the RequireAuth component
import Manager2 from "./Components/Manager/Manager2";
import Manager3 from "./Components/Manager/Manager3";
import VechileStatus from "./Components/Manager/VechileStatus";
import InsuranceRecord from "./Components/Manager/InsuranceRecord";
import Maintainancerecord from "./Components/Manager/Maintainancerecord";
import Old_driver from "./Components/Manager/Old_driver";
import Assignment from "./Components/Manager/Assignment";
import Old_Assignment from "./Components/Manager/Old_Assignment";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Background />,
  },
  {
    path: "/Admin",
    element: <Admin />,
    // Ensure you have valid children or remove the empty object
  },
  {
    path: "/Manager",
    element: (
      <RequireAuth>
        <Manager />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/driver",
    element: (
      <RequireAuth>
        <Manager2 />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/vehicle",
    element: (
      <RequireAuth>
        <Manager3 />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/vehiclestatus",
    element: (
      <RequireAuth>
        <VechileStatus />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/insurancerecord",
    element: (
      <RequireAuth>
        <InsuranceRecord />,
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/Maintainancerecord",
    element: (
      <RequireAuth>
        <Maintainancerecord />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/OldDriver",
    element: (
      <RequireAuth>
        <Old_driver />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/Assignment",
    element: (
      <RequireAuth>
        <Assignment />
      </RequireAuth>
    ),
  },
  {
    path: "/Manager/OldAssignment",
    element: (
      <RequireAuth>
        <Old_Assignment />
      </RequireAuth>
    ),
  },
  {
    path: "/auth",
    element: <Auth />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
