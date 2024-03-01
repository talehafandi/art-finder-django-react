import { Suspense, lazy } from "react";
import { Navigate } from "react-router-dom";
import { RouteObject } from "react-router";

//Import layouts
import BaseLayout from "./components/Layouts/BaseLayout";
import AppbarLayout from "./components/Layouts/AppbarLayout";

//Import pages
import { Explore } from "./pages/Explore";

const routes = [
  {
    path: "/auth",
    element: <BaseLayout />,
    // children: [
    //   {
    //     path: "signin",
    //     element:
    //   },
    // ],
  },
  {
    path: "/explore",
    element: <AppbarLayout />,
    children: [
      {
        path: "",
        element: <Explore />,
      },
    ],
  },
];
