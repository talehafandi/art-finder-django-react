import axios from "axios";
import { useDispatch } from "react-redux"; // Import useDispatch

// Define your API base URL (replace with your actual API endpoint)
const BASE_URL = "https://api.example.com";

// Function to make an API call and update the store
export const makeApiCallAndUpdateStore = async (
  endpoint,
  method,
  data,
  dispatch
) => {
  try {
    const response = await axios({
      method,
      url: `${BASE_URL}${endpoint}`,
      data,
    });

    // Assuming you have a Redux action to update the store (replace with your actual action)
    dispatch({ type: "UPDATE_STORE", payload: response.data });

    return response.data; // Return the API response if needed
  } catch (error) {
    console.error("Error making API call:", error);
    // Handle error (e.g., show a notification, dispatch an error action, etc.)
  }
};

const restApi = {
  getDataOnExplore: makeApiCallAndUpdateStore("GET", "./", {}),
  getDataOnWishlist: makeApiCallAndUpdateStore("GET", "./", {}),
};

export default restApi;
