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
import { getExploreData, updateExploreData } from "../../redux/reducers/exploreSlice";
import { useMapContext } from "../../context/mapContext";
import { useParams } from 'react-router-dom';
import { useSearchParams } from 'react-router-dom';


const Explore = (props) => {
  const {
    setAllMarkers,
    markersToDisplay,
    setUserLocation,
    pushToMarkersToDisplay,
    updateMarkersToDisplay,
    showMyLocation,
  } = useMapContext();

  const [loading, setLoading] = useState(false);
  // const exploreData = useSelector(getExploreData)
  const [searchParams, setSearchParams] = useSearchParams();
  const searchParam = searchParams.get('cat')
  const dispatch = useDispatch();
  useEffect(() => {
    //API call for fetching data on Explore page
    //TODO: Fetch explore data from store and assign it to the 'list' variable below
    const fetchData = async () => {
      setLoading(true);
      //Make call
      if (!searchParam){
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
      }
      else {
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
  }, []);

  const list = [
    {
      cardTitle: "Art Workshop at Gallery X",
      date: "2024-03-15T12:00:00Z",
      address: "123 Main Street, Cityville, USA",
      position: { lat: 40.7128, lng: -74.006 },
      description:
        "Join us for an exciting art workshop at Gallery X. Explore various techniques and unleash your creativity! This workshop will cover a wide range of topics, including painting, sculpture, and mixed media. Whether you're a beginner or an experienced artist, there's something for everyone to enjoy. Don't miss this opportunity to connect with fellow art enthusiasts and expand your artistic horizons.",
      keywords: ["Gallery", "Craft"],
      type: "event",
    },
    {
      cardTitle: "Photography Exhibition: Capturing Moments",
      date: "2024-04-10T10:00:00Z",
      address: "456 Elm Street, Townsville, USA",
      position: { lat: 34.0522, lng: -118.2437 },
      description:
        "Experience the world through the lens of talented photographers. Our exhibition showcases captivating moments frozen in time. From breathtaking landscapes to intimate portraits, each photograph tells a unique story. Join us as we explore the beauty and complexity of the world around us through the art of photography.",
      keywords: ["Photography", "Gallery"],
      type: "event",
    },
    {
      cardTitle: "Sculpture Symposium: Art in the Park",
      date: "2024-05-20T09:00:00Z",
      address: "789 Oak Avenue, Villagetown, USA",
      position: { lat: 51.5074, lng: -0.1278 },
      description:
        "Witness master sculptors bring stone to life at our annual Sculpture Symposium. Enjoy live demonstrations and interactive workshops. Learn about different sculpting techniques and discover the stories behind each unique piece. Whether you're an art enthusiast or simply curious about the creative process, this event promises to inspire and captivate audiences of all ages.",
      keywords: ["Sculpture", "Craft"],
      type: "event",
    },
  ];
  const renderList = () => {
    return list.map((item) => <EventVenueCard cardDetails={item} />);
  };

  const handleExploreData = (cat) => {
    const searchParam = searchParams.get('cat')

    if (searchParam == cat) {
      restApi.listDataOnExplore()
      setSearchParams({})
    }
    else {
      restApi.getDataOnExplore(cat)
      setSearchParams({ cat })
    }
  }

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
            <div className="category-menu" alt="museum" id='MU' onClick={(e) => handleExploreData(e.currentTarget.id)}>
              <div className="category-icon">
                <AccountBalanceIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Museums</span>
              </span>
            </div>
            <div className="category-menu" alt="galleries" id='GA' onClick={(e) => handleExploreData(e.currentTarget.id)}>
              <div className="category-icon">
                <CollectionsIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Galleries</span>
              </span>
            </div>
            <div className="category-menu" alt="photography" id='PH' onClick={(e) => handleExploreData(e.currentTarget.id)}>
              <div className="category-icon">
                <PhotoCameraIcon fontSize="large" />
              </div>
              <span className="category-text">
                <span>Photography</span>
              </span>
            </div>
            <div className="category-menu" alt="sculptures" id='SU' onClick={(e) => handleExploreData(e.currentTarget.id)}>
              <div className="category-icon">
                <SculptureIcon sx={{ fontSize: 40 }} />
              </div>
              <span className="category-text">
                <span>Sculptures</span>
              </span>
            </div>
            <div className="category-menu" alt="crafts" id='CR' onClick={(e) => handleExploreData(e.currentTarget.id)}>
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
