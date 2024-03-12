import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    firstName: "",
    lastName: "",
    email: "",
    username: "",
    avatar: "",
    token: "",
    isUserSignedIn: false,
  },
  reducers: {
    updateSignedInUser: (state, action) => {
      state.firstName = action.payload.user.first_name;
      state.lastName = action.payload.user.last_name;
      state.username = action.payload.user.username;
      state.email = action.payload.user.email;
      state.avatar = action.payload.user.avatar_url;
      state.token = action.payload.token;

      if (
        action.payload.token != "" &&
        action.payload.token != null &&
        action.payload.token != undefined &&
        username != ""
      )
        state.isUserSignedIn = true;
      else state.isUserSignedIn = false;
    },
    remove: (state) => (state = {}),
  },
  // extraReducers: (builder) => {
  //   builder.addCase(updateUser.pending, (state, action) => {
  //     state.pending = true;
  //     state.error = false;
  //   }),
  //     builder.addCase(updateUser.fulfilled, (state, action) => {
  //       state.pending = true;
  //       state.userInfo = action.payload;
  //     }),
  //     builder.addCase(updateUser.rejected, (state, action) => {
  //       state.pending = false;
  //       state.error = true;
  //     });
  // },
  selectors: {
    getCurrentUser: (state) => {
      return {
        name: state.firstName + "" + state.lastName,
        email: state.email,
        avatar: state.avatar,
      };
    },
    getIsUserSignedIn: (state) => state.isUserSignedIn,
  },
});

export const { updateSignedInUser, remove } = userSlice.actions;
export const { getCurrentUser, getIsUserSignedIn } = userSlice.selectors;
export default userSlice.reducer;
