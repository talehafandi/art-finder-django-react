import React, { useEffect, useState } from "react";

import "./index.css";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";
import CollectionsIcon from "@mui/icons-material/Collections";
import PhotoCameraIcon from "@mui/icons-material/PhotoCamera";
import ContentCutIcon from "@mui/icons-material/ContentCut";
import Search from "../../components/Search";
import EventVenueCard from "../../components/EventVenueCard";
import MapUi from "../../components/Map";
import SculptureIcon from "../../components/Icons/SculptureIcon";
import restApi from "../../api";
import { useDispatch, useSelector } from "react-redux";
import {
  getExploreData,
  updateExploreData,
} from "../../redux/reducers/exploreSlice";
import { updateWishlistData } from "../../redux/reducers/wishlistSlice";
import { useMapContext } from "../../context/mapContext";
import { useParams } from "react-router-dom";
import { useSearchParams } from "react-router-dom";

const Explore = (props) => {
  const { markersToDisplay } = useMapContext();

  const [loading, setLoading] = useState(false);
  const exploreData = useSelector(getExploreData).data || [];
  const [searchParams, setSearchParams] = useSearchParams();
  const searchParam = searchParams.get("cat");
  const dispatch = useDispatch();
  useEffect(() => {
    //API call for fetching data on Explore page
    //TODO: Fetch explore data from store and assign it to the 'list' variable below
    const fetchData = async () => {
      setLoading(true);
      //Make call
      if (!searchParam) {
        await restApi
          .listDataOnExplore()
          .then((response) => {
            //Update state on store (See exploreSlice reducer for more insights)
            dispatch(updateExploreData(response));
            setLoading(false);
          })
          .catch((error) => {
            setLoading(false);
          });
      } else {
        await restApi
          .getDataOnExplore(searchParam)
          .then((response) => {
            //Update state on store (See exploreSlice reducer for more insights)
            dispatch(updateExploreData(response));
            setLoading(false);
          })
          .catch((error) => {
            setLoading(false);
          });
      }
    };

    fetchData();
  }, [searchParam]);

  useEffect(() => {
    const fetchWishlist = async () => {
      await restApi
        .getDataOnWishlist()
        .then((response) => {
          dispatch(updateWishlistData(response));
        })
        .catch((error) => {
          console.log(error);
        });
    };
    fetchWishlist();
  });

  const renderList = () => {
    if (exploreData.length > 0)
      return exploreData.map((item) => <EventVenueCard cardDetails={item} />);
    else
      return (
        <>
          <div class="no-results-container">
            <div class="no-results-icon">😞</div>
            <div class="no-results-message">No results found!</div>
          </div>
        </>
      );
  };

  const handleExploreData = (cat) => {
    const searchParam = searchParams.get("cat");

    if (searchParam == cat) {
      restApi.listDataOnExplore();
      setSearchParams({});
    } else {
      restApi.getDataOnExplore(cat);
      setSearchParams({ cat });
    }
  };

  const setMenuActiveClassname = (category) => {
    if (searchParam == category)
      return "category-menu clickable-div active-cat-menu";
    else return "category-menu clickable-div";
  };

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
            <div
              className={setMenuActiveClassname("MU")}
              alt="museum"
              id="MU"
              onClick={(e) => handleExploreData(e.currentTarget.id)}
            >
              <div className="category-icon">
                <AccountBalanceIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Museums</span>
              </span>
            </div>
            <div
              className={setMenuActiveClassname("GA")}
              alt="galleries"
              id="GA"
              onClick={(e) => handleExploreData(e.currentTarget.id)}
            >
              <div className="category-icon">
                <CollectionsIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Galleries</span>
              </span>
            </div>
            <div
              className={setMenuActiveClassname("PH")}
              alt="photography"
              id="PH"
              onClick={(e) => handleExploreData(e.currentTarget.id)}
            >
              <div className="category-icon">
                <PhotoCameraIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Photography</span>
              </span>
            </div>
            <div
              className={setMenuActiveClassname("SU")}
              alt="sculptures"
              id="SU"
              onClick={(e) => handleExploreData(e.currentTarget.id)}
            >
              <div className="category-icon">
                <SculptureIcon sx={{ fontSize: 40 }} />
              </div>
              <span className="category-text">
                <span>Sculptures</span>
              </span>
            </div>
            <div
              className={setMenuActiveClassname("CR")}
              alt="crafts"
              id="CR"
              onClick={(e) => handleExploreData(e.currentTarget.id)}
            >
              <div className="category-icon">
                <ContentCutIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Crafts</span>
              </span>
            </div>
          </div>
        </div>
        <div className="list-container">{renderList()}</div>
      </div>
      <div className="container-right">
        <div className="gradient-top"></div>
        <MapUi className="map-ui" markers={markersToDisplay} />
        <div className="gradient-bottom"></div>
      </div>
    </div>
  );
};

export default Explore;
