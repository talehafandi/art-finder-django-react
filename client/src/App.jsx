import { useRoutes } from "react-router-dom";
import routes from "./router";
import ThemeProvider from "./theme/themeProvider";
import { CssBaseline } from "@mui/material";

import "./App.css";

function App() {
  const content = useRoutes(routes);

  //Todo: Context Providers

  return (
    <ThemeProvider>
      <CssBaseline />
      {content}
    </ThemeProvider>
  );
}

export default App;
