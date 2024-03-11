import { createSlice } from "@reduxjs/toolkit";

export const exploreSlice = createSlice({
  name: "explore",
  initialState: {
    data: [],
  },
  reducers: {
    updateExploreData: (state, action) => {
      state.data = action.payload.data;
    },
    clearExploreData: (state) => {
      state.data = [];
    },
  },
  selectors: {
    getExploreData: (state) => {
      return {
        data: state.data,
      };
    },
  },
});

export const { updateExploreData, clearExploreData } = exploreSlice.actions;
export const { getExploreData } = exploreSlice.selectors;
export default exploreSlice.reducer;
