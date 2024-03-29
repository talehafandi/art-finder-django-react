// import { Suspense, lazy } from "react";
import { Navigate } from "react-router-dom";

//Import layouts
import BaseLayout from "./components/Layouts/BaseLayout";
import AppbarLayout from "./components/Layouts/AppbarLayout";

//Import pages
import AuthDialog from "./pages/Auth";
import Explore from "./pages/Explore";
import MyWishlist from "./pages/MyWishlist";
import NearbyVenuesEventsCard from "./components/NearbyVenuesEventsCard";
import MyPlans from "./pages/MyPlans";
import PlanCard from "./components/PlanCard";

//TODO: Implement Authentication
// Fake authentication function
const fakeAuth = {
  isAuthenticated: false,
  authenticate(cb) {
    this.isAuthenticated = true;
    setTimeout(cb, 100); // fake async
    //Todo: If not authenticated, redirect to Sign in/Sign up
  },
  signout(cb) {
    this.isAuthenticated = false;
    setTimeout(cb, 100);
  },
};

// Protected Route Component
const ProtectedRoute = ({ element, ...rest }) => {
  return fakeAuth.isAuthenticated ? (
    element
  ) : (
    <Navigate to="/auth/signin" replace />
  );
};

const routes = [
  {
    path: "",
    element: <AppbarLayout />,
    children: [
      {
        path: "",
        element: <Explore />,
      },
      {
        path: "signin",
        element: <AuthDialog />,
      },
      {
        path: "wishlist",
        element: <MyWishlist />,
      },
      {
        path: "plans",
        element: <MyPlans />,
      },
    ],
  },
  {
    path: "test",
    element: <BaseLayout />,
    children: [
      {
        path: "",
        element: <PlanCard />,
      },
    ],
  },
];

export default routes;
