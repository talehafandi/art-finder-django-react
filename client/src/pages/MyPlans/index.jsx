import "./index.css";
import React from "react";
import expandDown from "../../assets/expand_down.svg";
import WishlistCard from "../../components/WishlistCard";
import NearbyVenuesEventsCard from "../../components/NearbyVenuesEventsCard";
import PlanCard from "../../components/PlanCard";

const MyPlans = (props) => {
  return (
    <div className="plan-container">
      <div className="plan-wrapper">
        <div className="my-plan-wrapper">
          <span className="plan-header">
            <span>My Plans</span>
          </span>
          <div className="pills">
            <div className="order-by-type">
              <div className="pill pill-active">
                <span>All</span>
              </div>
              <div className="pill">
                <span>Upcoming Events</span>
              </div>
              <div className="pill">
                <span>Past Events</span>
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
        <div className="my-plan">
          <PlanCard />
          <PlanCard />
        </div>
        <div className="my-itinerary-wrapper">
          <span className="itinerary-header">
            <span>My Itineraries</span>
          </span>
        </div>
        <div className="my-itinerary">
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

export default MyPlans;
