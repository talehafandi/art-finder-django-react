import nearbyEventImage from "../../assets/nearby-event-card-image.png";
import calendarWhiteIcon from "../../assets/calendar-white.svg";
import mapIcon from "../../assets/map.svg";

import "./index.css";

export default function NearbyVenuesEventsCard(props) {
  return (
    <>
      <div className="nearby-events-venues-card-wrapper">
        <img src={nearbyEventImage} className="nearby-event-image" />
        <div className="card-gradient"></div>
        <div className="nearby-events-card-content">
          <div className="nearby-event-name-description">
            <span className="venue-event-name">Boozy Brushes</span>
            <p className="venue-event-short-description">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua
            </p>
          </div>
          <div className="date-wrapper">
            <img src={calendarWhiteIcon} alt="calendar icon" />
            <span className="date">Wed, 14 Feb 23’</span>
          </div>
          <div className="location-wrapper">
            <img src={mapIcon} alt="map icon" />
            <span className="location">G27 AL, Glasgow</span>
          </div>
        </div>
      </div>
    </>
  );
}
