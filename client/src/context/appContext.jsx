import React, { createContext, useState, useContext } from "react";

// Create the context
const AppContext = createContext();

// Custom hook to use the context
export const useAppContext = () => useContext(AppContext);

// Provider component
export const AppProvider = ({ children }) => {
  const [signinPopupVisibility, setSigninPopupVisibility] = useState(true);

  const authPopupVisibility = (visibility) =>
    setSigninPopupVisibility((prevVisibility) => visibility);

  return (
    <AppContext.Provider value={{ signinPopupVisibility, authPopupVisibility }}>
      {children}
    </AppContext.Provider>
  );
};
