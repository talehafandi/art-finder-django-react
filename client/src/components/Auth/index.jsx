import React, { useState } from "react";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";
import "./index.css";
import googleIcon from "../../assets/google-icon.png";
import signInBg from "../../assets/sign-in-bg.png";
import {
  PrimaryAltButton,
  PrimaryButton,
  SecondaryOutlinedButton,
} from "../Buttons";
import { useAppContext } from "../../context/appContext";
import { Checkbox } from "@mui/material";

import restApi from "../../api";

export const Auth = () => {
  const { authPopupVisibility } = useAppContext();
  const [authView, setAuthView] = useState("signin");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
  };

  const toggleAuthView = () => {
    if (authView == "signin") setAuthView("signup");
    else setAuthView("signin");
  };

  const handleSignIn = () => {
    console.log("email:", email);
    console.log("Password:", password);
    restApi.signIn(email, password);
    //TODO: Make API call...
  };

  return (
    <div className="sign-in-wrapper">
      <div className="left-side">
        <img className="auth-image" src={signInBg}></img>
        <div className="overlap-wrapper">
          <div className="overlap">
            <Typography
              variant="h5"
              gutterBottom
              sx={{
                fontSize: "40px",
                fontWeight: "500",
                lineHeight: "49px",
                top: "160px",
                color: "#FFFFFF",
                width: "80%",
                paddingLeft: "10%",
              }}
            >
              {authView == "signin" && "Are you new here?"}
              {authView == "signup" && "Already have an account?"}
            </Typography>
            <div className="sign-up">
              <PrimaryAltButton
                sx={{ width: "150px", marginTop: "20px" }}
                onClick={() => toggleAuthView()}
              >
                {authView == "signin" && "SIGN UP"}
                {authView == "signup" && "SIGN IN"}
              </PrimaryAltButton>
              {/* <Button variant="contained" color="primary">
              SIGN UP
            </Button> */}
            </div>
          </div>
          <div className="logo-text">
            <Typography
              sx={{
                fontFamily: "Italiana",
                fontStyle: "normal",
                fontWeight: 200,
                fontSize: "55px",
                lineHeight: "65px",
                color: "white",
                marginTop: "auto",
                paddingLeft: "15%",
              }}
              align="left"
            >
              ArtFinder
            </Typography>
          </div>
        </div>
      </div>

      <div className="right-side">
        <div
          className="close-btn-wrapper"
          onClick={() => authPopupVisibility(false)}
        >
          <svg
            width="15"
            height="20"
            viewBox="0 0 15 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M13.3828 5.88281C13.8711 5.39453 13.8711 4.60156 13.3828 4.11328C12.8945 3.625 12.1016 3.625 11.6133 4.11328L7.5 8.23047L3.38281 4.11719C2.89453 3.62891 2.10156 3.62891 1.61328 4.11719C1.125 4.60547 1.125 5.39844 1.61328 5.88672L5.73047 10L1.61719 14.1172C1.12891 14.6055 1.12891 15.3984 1.61719 15.8867C2.10547 16.375 2.89844 16.375 3.38672 15.8867L7.5 11.7695L11.6172 15.8828C12.1055 16.3711 12.8984 16.3711 13.3867 15.8828C13.875 15.3945 13.875 14.6016 13.3867 14.1133L9.26953 10L13.3828 5.88281Z"
              fill="#2C2C2C"
            />
          </svg>
        </div>
        <div className="sign-in-form-wrapper">
          <div className="sign-in-text">
            {authView == "signin" && "Sign In"}
            {authView == "signup" && "Sign Up"}
          </div>
          {authView == "signin" && (
            <div className="sign-in-form">
              <TextField
                className="text-field-instance"
                id="email"
                label="Email"
                variant="standard"
                size="medium"
                value={email}
                sx={{ marginBottom: "10%" }}
                onChange={handleEmailChange}
              />
              <TextField
                className="design-component-instance-node"
                label="Password"
                id="password"
                type="password"
                size="medium"
                value={password}
                variant="standard"
                sx={{ marginBottom: "10%" }}
                onChange={handlePasswordChange}
              />
            </div>
          )}
          {authView == "signup" && (
            <div className="sign-in-form">
              <div className="name-wrapper">
                <TextField
                  className="text-field-instance"
                  id="first-name"
                  label="First Name"
                  variant="standard"
                  size="medium"
                  sx={{ marginBottom: "10%" }}
                  fullWidth
                  value={firstName}
                  onChange={handleFirstNameChange}
                />
                <TextField
                  className="text-field-instance"
                  id="last-name"
                  label="Last Name"
                  variant="standard"
                  size="medium"
                  sx={{ marginBottom: "10%" }}
                  fullWidth
                  value={lastName}
                  onChange={handleLastNameChange}
                />
              </div>
              <TextField
                className="text-field-instance"
                id="email"
                label="Email"
                variant="standard"
                size="medium"
                value={email}
                sx={{ marginBottom: "10%" }}
                onChange={handleEmailChange}
              />
              <TextField
                className="design-component-instance-node"
                label="Password"
                id="password"
                size="medium"
                value={password}
                type="password"
                variant="standard"
                sx={{ marginBottom: "10%" }}
                onChange={handlePasswordChange}
              />
              <div className="tac-check">
                <Checkbox size="small" />
                <span>
                  I have read and I accept the{" "}
                  <a
                    href="http://"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="tac-link"
                  >
                    T&Cs
                  </a>
                </span>
              </div>
            </div>
          )}
        </div>

        <div className="auth-options">
          {authView == "signin" && (
            <PrimaryButton
              fullWidth
              sx={{ marginBottom: "5%" }}
              onClick={handleSignIn}
            >
              SIGN IN
            </PrimaryButton>
          )}
          {authView == "signup" && (
            <PrimaryButton fullWidth sx={{ marginBottom: "5%" }}>
              SIGN UP
            </PrimaryButton>
          )}
          <div className="text-wrapper">Or</div>

          {authView == "signin" && (
            <>
              <SecondaryOutlinedButton
                startIcon={<img src={googleIcon}></img>}
                fullWidth
                sx={{ marginBottom: "5%" }}
              >
                SIGN IN WITH GOOGLE
              </SecondaryOutlinedButton>
              <SecondaryOutlinedButton
                variant="outlined"
                fullWidth
                sx={{ marginBottom: "5%" }}
              >
                REGISTER AS AN ORGANISER
              </SecondaryOutlinedButton>
            </>
          )}
          {authView == "signup" && (
            <SecondaryOutlinedButton
              startIcon={<img src={googleIcon}></img>}
              fullWidth
              sx={{ marginBottom: "5%" }}
            >
              SIGN UP WITH GOOGLE
            </SecondaryOutlinedButton>
          )}
        </div>
      </div>
    </div>
  );
};
