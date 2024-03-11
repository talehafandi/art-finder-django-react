import { APIProvider, Map, Marker } from "@vis.gl/react-google-maps";
import { useMapContext } from "../../context/mapContext";
import { useEffect } from "react";

const MapUi = () => {
  const { markersToDisplay } = useMapContext();

  useEffect(() => {
    console.log("Markers to display: ", markersToDisplay);
  }, [markersToDisplay]);
  // const position = { lat: 61.2176, lng: -149.8997 };
  const apikey = import.meta.env.VITE_MAPS_API_KEY;

  const renderMarkers = () => {
    return markersToDisplay.map((markerData) => (
      <Marker position={markerData} />
    ));
  };
  return (
    <APIProvider apiKey={apikey}>
      <Map center={markersToDisplay[0]} zoom={15}>
        {renderMarkers()}
        {/* <Marker position={position} /> */}
      </Map>
    </APIProvider>
  );
};

export default MapUi;
