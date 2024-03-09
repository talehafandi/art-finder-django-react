import React from "react";

import "./index.css";
import planSampleImage from "../../assets/plan-sample-image.png";
import calendarIcon from "../../assets/calendar.svg";
import mapIcon from "../../assets/map.svg";

const PlanCard = (props) => {
  return (
    <div className="place-container">
      <div className="textcontent">
        <div className="plandescription">
          <span className="place-event-card-title">Artsera</span>
          <span className="place-event-card-description">
            Lorem ipsum dolor sit amet consectetur. Viverra cras massa nibh
            cursus dui gravida tempor aliquet massa pharetra.
          </span>
        </div>
        <div className="datevenue">
          <div className="date">
            <div className="date-wrapper">
              <img src={calendarIcon} alt="calendar icon" />
              <span className="date">Wed, 14 Feb 23’</span>
            </div>
          </div>
          <div className="location">
            <div className="location-wrapper">
              <img src={mapIcon} alt="map icon" />
              <span className="location">G27 AL, Glasgow</span>
            </div>
          </div>
        </div>
      </div>
      <img src={planSampleImage} className="planimage" />
    </div>
  );
};

export default PlanCard;
