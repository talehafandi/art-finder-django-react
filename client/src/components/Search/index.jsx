import * as React from "react";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import SearchIcon from "@mui/icons-material/Search";
import DirectionsIcon from "@mui/icons-material/Directions";
import { useMapContext } from "../../context/mapContext";
import restApi from "../../api";
import { useDispatch } from "react-redux";
import { updateExploreData } from "../../redux/reducers/exploreSlice";

const Search = () => {
  const { showMyLocation } = useMapContext();
  const [searchField, setSearchField] = React.useState("");
  const [loading, setLoading] = React.useState(false);

  const dispatch = useDispatch();

  const onChangeSearchField = (event) => {
    setSearchField(event.target.value);
  };

  const search = () => {
    //TODO: Search API
    console.log("Search input: ", searchField);
    const searchData = async () => {
      setLoading(true);
      if (searchField.length > 0)
        await restApi.searchByName(searchField).then((response) => {
          console.log("search response: ", response);
          dispatch(updateExploreData(response));
        });
    };
    searchData();
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      event.stopPropagation();
      event.preventDefault();
      search();
    }
  };

  const handleSearchInputOnFocus = (event) => {
    const searchWrapper = document.getElementById("search-wrapper");
    searchWrapper.style.backgroundColor = "#d0bcfa";
  };

  const handleSearchInputOnBlur = (event) => {
    const searchWrapper = document.getElementById("search-wrapper");
    searchWrapper.style.backgroundColor = "white";
  };

  return (
    <Paper
      component="form"
      sx={{
        p: "2px 4px",
        display: "flex",
        alignItems: "center",
        width: 400,
        border: "1px solid black",
        borderRadius: "50px",
      }}
      id="search-wrapper"
    >
      <InputBase
        sx={{ ml: 1, flex: 1 }}
        placeholder="Search..."
        inputProps={{ "aria-label": "search google maps" }}
        onKeyDown={handleKeyDown}
        onChange={onChangeSearchField}
        value={searchField}
        onFocus={handleSearchInputOnFocus}
        onBlur={handleSearchInputOnBlur}
      />
      <IconButton
        type="button"
        sx={{ p: "10px" }}
        aria-label="search"
        onClick={() => search()}
      >
        <SearchIcon />
      </IconButton>
      <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
      <IconButton
        color="primary"
        sx={{ p: "10px" }}
        aria-label="directions"
        onClick={() => showMyLocation()}
      >
        <DirectionsIcon />
      </IconButton>
    </Paper>
  );
};

export default Search;
