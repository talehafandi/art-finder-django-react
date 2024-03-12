import React, { useState } from "react";
import { Auth } from "../../components/Auth";
import { useAppContext } from "../../context/appContext";
import "./index.css";
import { useSelector } from "react-redux";
import { getIsUserSignedIn } from "../../redux/reducers/userSlice";

export default function AuthDialog() {
  const { signinPopupVisibility } = useAppContext();
  console.log("popup visibility", signinPopupVisibility);
  const isUserSignedIn = useSelector(getIsUserSignedIn);

  return (
    <>
      {signinPopupVisibility && !isUserSignedIn && (
        <div className="popup-container">
          <Auth />
        </div>
      )}
    </>
  );
}
