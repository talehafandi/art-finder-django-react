import "./index.css";
import React from "react";
import expandDown from "../../assets/expand_down.svg";
import WishlistCard from "../../components/WishlistCard";
import NearbyVenuesEventsCard from "../../components/NearbyVenuesEventsCard";
import PlanCard from "../../components/PlanCard";
import { Button } from "@mui/material";
import AddItineraryIcon from "../../components/Icons/AddItineraryIcon";

const MyPlans = (props) => {
  const plans = [{}, {}, {}, {}];
  const itineraries = [{}, {}, {}, {}];

  const renderPlans = () => {
    return plans.map((item) => <PlanCard />);
  };

  const renderItineraries = () => {
    return itineraries.map((item) => <WishlistCard />);
  };

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
        <div className="my-plan">{renderPlans()}</div>
        <div className="my-itinerary-wrapper">
          <span className="itinerary-header">
            <span>My Itineraries</span>
            <Button
              variant="outlined"
              startIcon={<AddItineraryIcon />}
              sx={{ padding: "0px 20px" }}
            >
              Add to itinerary
            </Button>
          </span>
        </div>
        <div className="my-itinerary">{renderItineraries()}</div>
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
