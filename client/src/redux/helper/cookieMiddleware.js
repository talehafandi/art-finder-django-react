import Cookies from "js-cookie";
import { updateSignedInUser } from "../reducers/userSlice";

const cookieMiddleware = () => (next) => (action) => {
  if (action.type === updateSignedInUser.type) {
    const { firstName, lastName, email, username, avatar, token } =
      action.payload;

    // Store user data in cookies
    Cookies.set("artfinder-user", {
      firstName,
      lastName,
      email,
      username,
      avatar,
      token,
    });
  }

  return next(action);
};

export default cookieMiddleware;
