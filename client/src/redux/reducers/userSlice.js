import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const updateUser = createAsyncThunk("users/update", async (user) => {
  const res = await axios.post(
    "http://localhost:8800/api/users/1/update", //TODO: update actual API url
    user
  );
  return res.data;
});

export const userSlice = createSlice({
  name: "user",
  initialState: {
    name: "Mahesh Adhikari",
    email: "spiralmonkey225@gmail.com",
    isUserSignedIn: false,
  },
  reducers: {
    update: (state, action) => {
      state.name = action.payload.name;
      state.email = action.payload.name;
    },
    remove: (state) => (state = {}),
  },
  extraReducers: (builder) => {
    builder.addCase(updateUser.pending, (state, action) => {
      state.pending = true;
      state.error = false;
    }),
      builder.addCase(updateUser.fulfilled, (state, action) => {
        state.pending = true;
        state.userInfo = action.payload;
      }),
      builder.addCase(updateUser.rejected, (state, action) => {
        state.pending = false;
        state.error = true;
      });
  },
  selectors: {
    getCurrentUser: (state) => {
      return {
        name: state.name,
        email: state.email,
      };
    },
    getIsUserSignedIn: (state) => state.isUserSignedIn,
  },
});

export const { update, remove } = userSlice.actions;
export const { getCurrentUser, getIsUserSignedIn } = userSlice.selectors;
export default userSlice.reducer;
