import { createSlice } from "@reduxjs/toolkit";

export const wishlistSlice = createSlice({
  name: "wishlist",
  initialState: {
    data: [],
  },
  reducers: {
    updateWishlistData: (state, action) => {
      state.data = action.payload.data;
    },
    clearWishlistData: (state) => {
      state.data = [];
    },
  },
  selectors: {
    getWishlistData: (state) => {
      return {
        data: state.data,
      };
    },
  },
});

export const { updateWishlistData, clearWishlistData } = wishlistSlice.actions;
export const { getWishlistData } = wishlistSlice.selectors;
export default wishlistSlice.reducer;
