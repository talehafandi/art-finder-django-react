import React from "react";

import "./index.css";

import favouriteIcon from "../../assets/favorite-heart.svg";
import calendarIcon from "../../assets/calendar.svg";
import mapIcon from "../../assets/map.svg";
import { PrimaryButton } from "../Buttons";
import { formatDate } from "../../utils";
import { useMapContext } from "../../context/mapContext";

//TODO: Update 'Book a seat' button
// TODO: Update wishlist button to a MUI fab button
// TODO:

const EventVenueCard = ({ cardDetails }) => {
  const { updateMarkersToDisplay } = useMapContext();

  const handleClickOnCard = (event, position) => {
    event.stopPropagation();
    console.log("clicked on card...", position);
    updateMarkersToDisplay([position]);
  };

  const handleBookSeat = (event) => {
    event.stopPropagation();
    console.log("clicked on booking button...");
  };

  const handleAddToWishlist = (event) => {
    event.stopPropagation();
    console.log("clicked on wishlist button...");
  };

  return (
    <div
      className="place"
      onClick={(event) => handleClickOnCard(event, cardDetails.position)}
    >
      <div className="card-title-wrapper">
        <span className="card-title">
          <span>{cardDetails.cardTitle}</span>
        </span>
        <img
          src={favouriteIcon}
          alt="wishlisted"
          className="wishlist-icon"
          onClick={handleAddToWishlist}
        />
      </div>
      <div className="date-location">
        <div className="date-wrapper">
          <img src={calendarIcon} alt="calendar icon" />
          <span className="date">{formatDate(cardDetails.date)}</span>
        </div>
        <div className="location-wrapper">
          <img src={mapIcon} alt="map icon" />
          <span className="location">{cardDetails.address}</span>
        </div>
      </div>
      <span className="event-venue-description">{cardDetails.description}</span>
      <div className="keyword-book-view-on-map">
        <div className="keyword-wrapper">
          {cardDetails.keywords.map((keyword) => (
            <>
              <div className="keyword">
                <span className="keyword-text">
                  <span>{keyword}</span>
                </span>
              </div>
            </>
          ))}
        </div>

        <div className="bookseatviewonmap">
          {/* Todo: Replace the button below with a MUI button */}
          <PrimaryButton
            fullWidth
            size="small"
            sx={{
              width: "125px",
              height: "32px !important",
            }}
            className="book-a-seat-btn"
            onClick={handleBookSeat}
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
