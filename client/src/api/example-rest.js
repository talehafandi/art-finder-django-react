// src/components/MyComponent.js

import React from "react";
import { useDispatch } from "react-redux"; // Import useDispatch
import { makeApiCallAndUpdateStore } from "./index"; // Import your custom function

const MyComponent = () => {
  const dispatch = useDispatch();

  const handleApiCall = async () => {
    try {
      // Make an API call and update the store
      const apiResponse = await makeApiCallAndUpdateStore(
        "/posts",
        "GET",
        null,
        dispatch
      );
      console.log("API response:", apiResponse);
    } catch (error) {
      console.error("Error in API call:", error);
    }
  };

  return (
    <div>
      <button onClick={handleApiCall}>Make API Call</button>
      {/* Other component content */}
    </div>
  );
};

export default MyComponent;
