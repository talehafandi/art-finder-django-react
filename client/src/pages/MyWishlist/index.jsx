import "./index.css";
import React from "react";
import expandDown from "../../assets/expand_down.svg";
import WishlistCard from "../../components/WishlistCard";
import NearbyVenuesEventsCard from "../../components/NearbyVenuesEventsCard";

const MyWishlist = (props) => {
  return (
    <div className="wishlist-container">
      <div className="wishlist-wrapper">
        <div className="my-wishlist-wrapper">
          <span className="wishlist-header">
            <span>My Wishlist</span>
          </span>
          <div className="pills">
            <div className="order-by-type">
              <div className="pill pill-active">
                <span>All</span>
              </div>
              <div className="pill">
                <span>Places</span>
              </div>
              <div className="pill">
                <span>Events</span>
              </div>
            </div>
            <div className="orderby">
              <div className="frame4">
                <span className="text-3">
                  <span>Order By</span>
                </span>
                <img
                  src={expandDown}
                  alt="Expand down"
                  className="expanddown"
                />
              </div>
            </div>
          </div>
        </div>
        <div className="my-wishlist">
          <WishlistCard />
          <WishlistCard />
          <WishlistCard />
          <WishlistCard />
        </div>
      </div>
      <div className="places-events-nearby-wrapper">
        <span className="places-events-nearby-heading">
          Places and Events nearby
        </span>
        <div className="places-events-nearby-container">
          <NearbyVenuesEventsCard />
        </div>
      </div>
    </div>
  );
};

export default MyWishlist;
