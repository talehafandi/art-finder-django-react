import React from "react";
import "./userbox.css";
import expandDown from "../../assets/expand_down.svg";
import { useAppContext } from "../../context/appContext";
import { PrimaryButton } from "../Buttons";
import { useSelector } from "react-redux";
import {
  getCurrentUser,
  getIsUserSignedIn,
} from "../../redux/reducers/userSlice";
import TouchRipple from "@mui/material/ButtonBase/TouchRipple";
import { useDispatch } from "react-redux"; // Import useDispatch
import { updateSignedInUser } from "../../redux/reducers/userSlice";
import { Button } from "@mui/material";

const Userbox = () => {
  const dispatch = useDispatch();
  const handleSignOut = () => {
    console.log("Signing out user...");
    dispatch(
      updateSignedInUser({
        user: {
          first_name: "",
          last_name: "",
          username: "",
          email: "",
          avatar_url: "",
        },
        token: "",
      })
    );
  };

  const { authPopupVisibility } = useAppContext();
  const currentUser = useSelector(getCurrentUser);
  const isUserSignedIn = useSelector(getIsUserSignedIn);

  const rippleRef = React.useRef(null);
  const onRippleStart = (e) => {
    rippleRef.current.start(e);
  };
  const onRippleStop = (e) => {
    rippleRef.current.stop(e);
  };

  return (
    <>
      {isUserSignedIn && (
        <div
          className="userbox-userbox"
          type="button"
          onMouseDown={onRippleStart}
          onMouseUp={onRippleStop}
          onClick={handleSignOut}
        >
          <img
            src={currentUser.avatar}
            alt="profile-picture"
            className="profile-picture"
          />
          <div className="userbox-group3">
            <span className="userbox-text">
              <span>{currentUser.name}</span>
            </span>
            <span className="userbox-text2">
              <span>{currentUser.email}</span>
            </span>
          </div>
          <img
            src={expandDown}
            alt="Expanddown7064"
            className="userbox-expanddown"
          />
          <TouchRipple ref={rippleRef} center={false} />
          {/* <div className="profile-drop-down" onClick={handleSignOut}>
            <Button sx={{ background: "white" }}>Sign Out</Button>
          </div> */}
        </div>
      )}
      {!isUserSignedIn && (
        <PrimaryButton onClick={() => authPopupVisibility(true)}>
          Sign in
        </PrimaryButton>
      )}
    </>
  );
};

export default Userbox;
