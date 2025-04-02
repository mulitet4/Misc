import { Auth } from "../Auth/Auth";
// import { authToken } from "../Auth/Auth";
import { useCookies } from "react-cookie";
import List from "./List";
export default function Manager() {
  const handleLogout = () => {
    removeCookie("authToken");
    removeCookie("Email");
    window.location.reload();
  };
  const [cookies, setCookie, removeCookie] = useCookies();
  return (
    <>
      {cookies.authToken ? (
        <>
          {/* <button onClick={() => handleLogout()}>Log Out</button>
          <div>{cookies.authToken}</div>
          <div>{cookies.Email}</div> */}
          <List />
        </>
      ) : (
        <Auth />
      )}
    </>
  );
}
