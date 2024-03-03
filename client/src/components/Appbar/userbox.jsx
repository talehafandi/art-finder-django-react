import React from "react";
import "./userbox.css";
import avatar from "../../assets/avatar.png";
import expandDown from "../../assets/expand_down.svg";

const Userbox = (props) => {
  return (
    <div className="userbox-userbox">
      <img src={avatar} alt="profile-picture" className="userbox-ellipse2" />
      <div className="userbox-group3">
        <span className="userbox-text">
          <span>Mahesh Adhikari</span>
        </span>
        <span className="userbox-text2">
          <span>spiralmonkey@gmail.com</span>
        </span>
      </div>
      <img
        src={expandDown}
        alt="Expanddown7064"
        className="userbox-expanddown"
      />
    </div>
  );
};

export default Userbox;
