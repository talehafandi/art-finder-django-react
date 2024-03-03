import React from "react";

import "./index.css";

import favouriteIcon from "../../assets/favorite-heart.svg";
import calendarIcon from "../../assets/calendar.svg";
import mapIcon from "../../assets/map.svg";
import { PrimaryButton } from "../Buttons";

//TODO: Update 'Book a seat' button
// TODO: Update wishlist button to a MUI fab button
// TODO:

const EventVenueCard = (props) => {
  return (
    <div className="place">
      <div className="card-title-wrapper">
        <span className="card-title">
          <span>Artsera</span>
        </span>
        <img src={favouriteIcon} alt="wishlisted" className="wishlist-icon" />
      </div>
      <div className="date-location">
        <div className="date-wrapper">
          <img src={calendarIcon} alt="calendar icon" />
          <span className="date">Wed, 14 Feb 23’</span>
        </div>
        <div className="location-wrapper">
          <img src={mapIcon} alt="map icon" />
          <span className="location">G27 AL, Glasgow</span>
        </div>
      </div>
      <span className="event-venue-description">
        Lorem ipsum dolor sit amet consectetur. Cras fringilla non dictum vel
        tempor. Arcu enim dignissim tortor habitasse. Arcu malesuada quam duis
        viverra quis pellentesque tristique. Sed id mattis est et molestie
        tristique duis. Pulvinar aliquet elementum sagittis nec. Lacus sociis
        metus cras eu proin eget rhoncus. Velit rhoncus nisl placerat
        consectetur luctus venenatis sit maecenas. Ac ornare tellus et enim
        pharetra. In vulputate arcu egestas enim velit suspendisse nisl. Amet.
      </span>
      <div className="keyword-book-view-on-map">
        <div className="keyword-wrapper">
          <span className="keyword-text">
            <span>Crafts</span>
          </span>
        </div>
        <div className="bookseatviewonmap">
          {/* Todo: Replace the button below with a MUI button */}
          <PrimaryButton
            fullWidth
            size="small"
            sx={{ marginBottom: "5%", width: "125px" }}
            className="book-a-seat-btn"
          >
            Book a seat
          </PrimaryButton>
          <span className="click-to-view-map">
            <span>Click to view on map...</span>
          </span>
        </div>
      </div>
    </div>
  );
};

export default EventVenueCard;
