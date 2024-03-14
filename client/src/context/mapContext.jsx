import React, { createContext, useState, useContext, useEffect } from "react";

// Create the context
const MapContext = createContext();

// Custom hook to use the context
export const useMapContext = () => useContext(MapContext);

// Provider component
export const MapProvider = ({ children }) => {
  const [allMarkers, setAllMarkers] = useState([]);
  const [markersToDisplay, setMarkersToDisplay] = useState([
    {
      lat: 55.873402644172984,
      lng: -4.288952736251727,
    },
  ]);
  const [userLocation, setUserLocation] = useState({
    lat: 55.873402644172984,
    lng: 4.288952736251727,
  });

  const pushToMarkersToDisplay = (position) =>
    setMarkersToDisplay((prevMarkers) => [...prevMarkers.position]);

  const updateMarkersToDisplay = (markers) =>
    setMarkersToDisplay(() => markers);

  function getUserLocationAndDisplayOnMap() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else {
      window.alert("Geolocation is not supported by this browser.");
    }
  }

  function showPosition(position) {
    console.log("Position: ", position);
    setUserLocation({
      lat: position.coords.latitude,
      lng: position.coords.longitude,
    });
    updateMarkersToDisplay([
      {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
      },
    ]);
  }

  function showMyLocation() {
    getUserLocationAndDisplayOnMap();
  }

  return (
    <MapContext.Provider
      value={{
        allMarkers,
        setAllMarkers,
        markersToDisplay,
        userLocation,
        setUserLocation,
        pushToMarkersToDisplay,
        updateMarkersToDisplay,
        getUserLocationAndDisplayOnMap,
        showMyLocation,
      }}
    >
      {children}
    </MapContext.Provider>
  );
};
