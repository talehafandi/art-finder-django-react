import { APIProvider, Map, Marker } from "@vis.gl/react-google-maps";

function MapUi() {
  const position = { lat: 61.2176, lng: -149.8997 };
  const apikey = import.meta.env.VITE_MAPS_API_KEY;
  return (
    <APIProvider apiKey={apikey}>
      <Map center={position} zoom={10}>
        <Marker position={position} />
      </Map>
    </APIProvider>
  );
}

export default MapUi;
