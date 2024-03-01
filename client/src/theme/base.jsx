import React from "react";
import { DefaultTheme } from "./schemes/default";

export function themeCreator(theme) {
  return themes[theme];
}

const themes = {
  DefaultTheme,
};
