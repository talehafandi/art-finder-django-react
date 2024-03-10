import axios from "axios";
import { useDispatch } from "react-redux"; // Import useDispatch
import { updateSignedInUser } from "../redux/reducers/userSlice";

const BASE_URL = import.meta.env.VITE_API_BASE_URL;
const APP_ENDPOINT = import.meta.env.VITE_API_ENDPOINT;

const API_URL = BASE_URL + APP_ENDPOINT;

// Function to make an API call and update the store
export const makeApiCall = async (endpoint, method, data) => {
  console.log("API url: ", API_URL);
  try {
    const response = await axios({
      method,
      url: `${API_URL}${endpoint}`,
      data,
    });

    return response.data; // Return the API response
  } catch (error) {
    console.error("Error making API call:", error);
    // TODO: Handle error (e.g., show a notification, dispatch an error action, etc.)
  }
};

const restApi = {
  signIn: (username, password) =>
    makeApiCall(
      "/login", // Change the order of arguments
      "POST", // Change the order of arguments
      { username, password }
    ),
  getDataOnExplore: () => makeApiCall("/", "GET", null, null), // Change the order of arguments and pass null for parameters not used
  getDataOnWishlist: () => makeApiCall("/", "GET", null, null), // Change the order of arguments and pass null for parameters not used
};

export default restApi;
