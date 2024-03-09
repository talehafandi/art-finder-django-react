import React, { useState } from "react";
import { themeCreator } from "./base";
import { StylesProvider } from "@mui/styles";
import { ThemeProvider } from "@mui/material";

const ThemeContext = React.createContext((themeName) => {});

export const ThemeProviderWrapper = (props) => {
  const curThemeName = localStorage.getItem("appTheme") || "DefaultTheme";
  const [themeName, _setThemeName] = useState(curThemeName);
  const theme = themeCreator(themeName);
  const setThemeName = (themeName) => {
    localStorage.setItem("appTheme", themeName);
    _setThemeName(themeName);
  };

  return (
    <StylesProvider injectFirst>
      <ThemeContext.Provider value={setThemeName}>
        <ThemeProvider theme={theme}>{props.children}</ThemeProvider>
      </ThemeContext.Provider>
    </StylesProvider>
  );
};

export default ThemeProviderWrapper;
