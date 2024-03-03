import React from "react";
import "./index.css";
import { Typography } from "@mui/joy";
import { NavLink as RouterLink } from "react-router-dom";
import { Avatar, Button } from "@mui/material";
import avatar from "../../assets/avatar.png";
import Userbox from "./userbox";

export const AppBar = () => {
  return (
    <div className="app-bar">
      <div className="logo-wrapper">
        <div className="logo">
          <Typography
            sx={{
              fontFamily: "Italiana",
              fontWeight: 200,
              fontSize: "38px",
              lineHeight: "62px",
              color: "white",
              marginTop: "auto",
              paddingLeft: "4%",
            }}
            align="left"
          >
            ArtFinder
          </Typography>
        </div>
      </div>
      <div className="menu-wrapper">
        <Button
          component={RouterLink}
          to="/explore"
          className="menu-item"
          activeClassname="active"
        >
          Explore
        </Button>
        <Button
          component={RouterLink}
          to=""
          className="menu-item"
          activeClassname="active"
        >
          My Plans
        </Button>
        <Button
          component={RouterLink}
          to=""
          className="menu-item"
          activeClassname="active"
        >
          My Wishlist
        </Button>
      </div>
      <Userbox />
    </div>
  );
};
