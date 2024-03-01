import PropTypes from "prop-types";
import { Outlet } from "react-router-dom";

import { Box } from "@mui/material";
import { AppBar } from "../../Appbar";

const BaseLayout = ({ children }) => {
  return (
    <Box
      sx={{
        flex: 1,
        height: "100%",
      }}
    >
      <AppBar></AppBar>
      {children || <Outlet />}
    </Box>
  );
};

BaseLayout.propTypes = {
  children: PropTypes.node,
};

export default BaseLayout;
