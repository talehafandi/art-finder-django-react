import React, { useState } from "react";
import { Auth } from "../../components/Auth";
import { useAppContext } from "../../context/appContext";
import "./index.css";

export default function AuthDialog() {
  const { signinPopupVisibility } = useAppContext();
  console.log("popup visibility", signinPopupVisibility);

  return (
    <>
      {signinPopupVisibility && (
        <div className="popup-container">
          <Auth />
        </div>
      )}
    </>
  );
}
