import React from "react";

import "./index.css";
import favouriteIcon from "../../assets/favorite-heart.svg";
import mapIcon from "../../assets/map.svg";
import venueImage from "../../assets/venue-image.png";

const WishlistCard = (props) => {
  return (
    <div className="wishlist-card-container">
      {
        // TODO: replace src with props.src for dynamically setting the src
      }
      <img src={venueImage} className="event-venue-card-image" />
      <div className="wishlist-card-content">
        <div className="wishlist-button-wrapper">
          <img
            src={favouriteIcon}
            alt="Wishlist Button"
            className="wishlisted-filled"
          />
        </div>

        <div className="wishlist-card-details">
          <span className="event-venue-name">
            <span>GOMA</span>
          </span>
          <span className="short-description">
            <span>
              Lorem ipsum dolor sit amet consectetur. Est turpis in massa a
              blandit. Proin.
            </span>
          </span>
          <div className="location">
            <img src={mapIcon} />
            <span
              className="location-name
              "
            >
              <span>Glasgow</span>
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WishlistCard;
