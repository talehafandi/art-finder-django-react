import React from "react";

import "./index.css";
import TextField from "@mui/material/TextField";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import CollectionsIcon from "@mui/icons-material/Collections";
import PhotoCameraIcon from "@mui/icons-material/PhotoCamera";
import Search from "../../components/Search";
import EventVenueCard from "../../components/EventVenueCard";
import MapUi from "../../components/Map";

const Explore = (props) => {
  return (
    <div className="container">
      <div className="container-left">
        <div className="exploresearchcategories">
          <div className="exploresearch">
            <span className="text">
              <span>Explore</span>
            </span>
            <div className="search">
              <Search />
            </div>
          </div>
          <div className="explorecategoriesmenu">
            <div className="category-menu" alt="museum">
              <div className="category-icon">
                <AccountBalanceIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Museums</span>
              </span>
            </div>
            <div className="category-menu" alt="galleries">
              <div className="category-icon">
                <CollectionsIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Galleries</span>
              </span>
            </div>
            <div className="category-menu" alt="photography">
              <div className="category-icon">
                <PhotoCameraIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Photography</span>
              </span>
            </div>
            <div className="category-menu" alt="sculptures">
              <div className="category-icon">
                <CollectionsIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Sculptures</span>
              </span>
            </div>
            <div className="category-menu" alt="crafts">
              <div className="category-icon">
                <CollectionsIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Crafts</span>
              </span>
            </div>
          </div>
        </div>
        <div className="list-container">
          <EventVenueCard />
        </div>
      </div>
      <div className="container-right">
        <div className="gradient-top"></div>
        <MapUi className="map-ui" />
        <div className="gradient-bottom"></div>
      </div>
    </div>
  );
};

export default Explore;
