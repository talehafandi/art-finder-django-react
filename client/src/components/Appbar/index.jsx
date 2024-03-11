import React, { useEffect } from "react";
import "./index.css";
import { Typography } from "@mui/joy";
import { NavLink } from "react-router-dom";
import Userbox from "./userbox";
import Button from "@mui/material/Button";

const AppBar = () => {
  useEffect(() => {
    window.onscroll = function () {
      myFunction();
    };

    var header = document.getElementById("appbar");
    var sticky = header.offsetTop;

    function myFunction() {
      if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
        header.style.top = "0";
      } else {
        header.classList.remove("sticky");
      }
    }
  });

  return (
    <div className="app-bar" id="appbar">
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
        <Button component={NavLink} to="" className="menu-item">
          Explore
        </Button>
        <Button component={NavLink} to="plans" className="menu-item">
          My Plans
        </Button>
        <Button component={NavLink} to="wishlist" className="menu-item">
          My Wishlist
        </Button>
      </div>
      <Userbox />
    </div>
  );
};

export default AppBar;
