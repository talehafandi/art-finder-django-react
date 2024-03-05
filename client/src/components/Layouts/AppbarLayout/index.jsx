import PropTypes from "prop-types";
import { Outlet } from "react-router-dom";

import { Box } from "@mui/material";
import AppBar from "../../Appbar";
import { AppProvider } from "../../../context/appContext";
import AuthDialog from "../../../pages/Auth";

const BaseLayout = ({ children }) => {
  return (
    <Box
      sx={{
        flex: 1,
        height: "100%",
      }}
    >
      <AppProvider>
        <AppBar></AppBar>
        {children || <Outlet />}
        <AuthDialog />
      </AppProvider>
    </Box>
  );
};

BaseLayout.propTypes = {
  children: PropTypes.node,
};

export default BaseLayout;
