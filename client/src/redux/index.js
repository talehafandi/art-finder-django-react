import { configureStore, combineReducers } from "@reduxjs/toolkit";
import userReducer from "./reducers/userSlice";
import cookieMiddleware from "./helper/cookieMiddleware";
import { persistStore, persistReducer } from "redux-persist";
import storage from "redux-persist/lib/storage"; // defaults to localStorage for web

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(
  persistConfig,
  combineReducers({
    user: userReducer,
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
