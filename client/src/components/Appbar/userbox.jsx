import React from "react";
import "./userbox.css";
import avatar from "../../assets/avatar.png";
import expandDown from "../../assets/expand_down.svg";
import { useAppContext } from "../../context/appContext";
import { PrimaryButton } from "../Buttons";
import { connect } from "react-redux";
import { useSelector } from "react-redux";
import {
  getCurrentUser,
  getIsUserSignedIn,
} from "../../redux/reducers/userSlice";
import TouchRipple from "@mui/material/ButtonBase/TouchRipple";

const Userbox = () => {
  const { authPopupVisibility } = useAppContext();
  const currentUser = useSelector(getCurrentUser);
  const isUserSignedIn = useSelector(getIsUserSignedIn);
  // console.log("Current user: ", currentUser);
  // console.log("is user signed in: ", isUserSignedIn);

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
        >
          <img
            src={avatar}
            alt="profile-picture"
            className="userbox-ellipse2"
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
