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

const venueKeywords = {
  MU: "Museum",
  GA: "Gallery",
};

const eventKeywords = {
  AR: "Art",
  MU: "Photography",
  SU: "Sculptures",
  CR: "Crafts",
};

const EventVenueCard = ({ cardDetails }) => {
  const { updateMarkersToDisplay } = useMapContext();

  const handleClickOnCard = (event, cardDetails) => {
    event.stopPropagation();
    console.log("clicked on card...", cardDetails);
    console.log({
      lat: parseFloat(cardDetails.lat),
      lng: parseFloat(cardDetails.long),
    });
    updateMarkersToDisplay([
      {
        lat: parseFloat(cardDetails.lat),
        lng: parseFloat(cardDetails.long),
      },
    ]);
  };

  const handleBookSeat = (event) => {
    event.stopPropagation();
    console.log("clicked on booking button...");
  };

  const handleAddToWishlist = (event) => {
    event.stopPropagation();
    console.log("clicked on wishlist button...");
  };

  const isWishlisted = () => {};

  return (
    <div
      className="place clickable-div"
      onClick={(event) => handleClickOnCard(event, cardDetails)}
    >
      <div className="card-title-wrapper">
        <span className="card-title">
          <span>{cardDetails.name || cardDetails.title}</span>
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
          <span className="location">
            {cardDetails.address || cardDetails.venue}
          </span>
        </div>
      </div>
      <span className="event-venue-description">{cardDetails.description}</span>
      <div className="keyword-book-view-on-map">
        <div className="keyword-wrapper">
          <div className="keyword">
            <span className="keyword-text">
              {cardDetails.venue_category && (
                <span>{venueKeywords[cardDetails.venue_category]}</span>
              )}
              {cardDetails.event_category && (
                <span>{eventKeywords[cardDetails.event_category]}</span>
              )}
            </span>
          </div>
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
