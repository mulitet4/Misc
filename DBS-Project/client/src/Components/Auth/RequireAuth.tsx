// RequireAuth.js
import React from "react";
import { Navigate } from "react-router-dom";
// import { authToken } from "./Auth"; // Assuming this is a valid way to check auth
import { useCookies } from "react-cookie";
function RequireAuth({ children }) {
  const [cookies, setCookie, removeCookie] = useCookies();
  return cookies.authToken ? children : <Navigate to="/auth" replace />;
}

export default RequireAuth;
