import { ThemeProvider } from "./theme/themeProvider";
import { CssBaseline } from "@mui/material";

import "./App.css";

function App() {
  const content = useRoutes(router);

  //Todo: Context Providers

  return (
    <ThemeProvider>
      <CssBaseline />
      {content}
    </ThemeProvider>
  );
}

export default App;
