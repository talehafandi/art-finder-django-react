import { configureStore, combineReducers } from "@reduxjs/toolkit";
import userReducer from "./reducers/userSlice";
import exploreReducer from "./reducers/exploreSlice";
import cookieMiddleware from "./helper/cookieMiddleware";
import { persistStore, persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage"; // defaults to localStorage for web
import wishlistSlice from "./reducers/wishlistSlice";

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(
  persistConfig,
  combineReducers({
    user: userReducer,
    explore: exploreReducer,
    wishlist: wishlistSlice,
  })
);

const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(cookieMiddleware),
});

// Wrap the store creation with persistStore
const persistor = persistStore(store);

export { store, persistor };
