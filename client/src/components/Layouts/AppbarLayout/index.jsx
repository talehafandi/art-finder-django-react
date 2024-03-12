import PropTypes from "prop-types";
import { Outlet } from "react-router-dom";

import { Box } from "@mui/material";
import AppBar from "../../Appbar";
import { AppProvider } from "../../../context/appContext";
import AuthDialog from "../../../pages/Auth";
import { MapProvider } from "../../../context/mapContext";

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
        <MapProvider>{children || <Outlet />}</MapProvider>
        <AuthDialog />
      </AppProvider>
    </Box>
  );
};

BaseLayout.propTypes = {
  children: PropTypes.node,
};

export default BaseLayout;
