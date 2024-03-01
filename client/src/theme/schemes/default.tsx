import { alpha, createTheme, lighten, darken } from "@mui/material";
// import "@mui/lab/themeAugmentation";

const themeColors = {
  primary: "#F77F00", //Orange
  secondary: "#6320EE",
  success: "",
  warning: "",
  error: "",
  info: "",
  white: "",
  primaryAlt: "",
  black: "#2C2C2C",
};

const colors = {
  layout: {
    general: {
      bodyBg: "#FFFFFF",
    },
  },
  alpha: {
    black: {
      5: alpha(themeColors.black, 0.02),
      10: alpha(themeColors.black, 0.1),
      30: alpha(themeColors.black, 0.3),
      50: alpha(themeColors.black, 0.5),
      70: alpha(themeColors.black, 0.7),
      100: themeColors.black,
    },
  },
};

export const DefaultTheme = createTheme({
  palette: {
    primary: {
      light: lighten(themeColors.primary, 0.3),
      main: themeColors.primary,
      dark: darken(themeColors.primary, 0.2),
    },
    secondary: {
      light: lighten(themeColors.secondary, 0.25),
      main: themeColors.secondary,
      dark: darken(themeColors.secondary, 0.2),
    },
  },
  //@ts-ignore
  colors: {
    gradients: {
      popover:
        "linear-gradient(180deg, rgba(255, 131, 0, 0.4) 34%, rgba(0, 0, 0, 0.4) 100%)",
      placesAndEventsCard:
        "linear-gradient(180deg, rgba(255, 255, 255, 0) 0%, rgba(99, 32, 238, 0.288) 38.5%",
      itineraryCard:
        "linear-gradient(180deg, rgba(255, 255, 255, 0) 0%, rgba(14, 14, 14, 0.8) 78%)",
    },
    shadows: {
      cards: "0px 4px 4px rgba(0, 0, 0, 0.1)",
    },
  },
  breakpoints: {
    values: {
      xs: 0,
      sm: 600,
      md: 960,
      lg: 1280,
      xl: 1840,
    },
  },
  typography: {
    fontFamily: '"Montserrat", "Helvetica", "Arial", sans-serif',
    h1: {
      fontWeight: 700,
      fontSize: 35,
    },
    h2: {
      fontWeight: 700,
      fontSize: 30,
    },
    h3: {
      fontWeight: 700,
      fontSize: 25,
      lineHeight: 1.4,
      color: colors.alpha.black[100],
    },
    h4: {
      fontWeight: 700,
      fontSize: 16,
      color: colors.alpha.black[100],
    },
    h5: {
      fontWeight: 700,
      fontSize: 14,
      color: colors.alpha.black[100],
    },
    h6: {
      fontSize: 15,
    },
    body1: {
      fontSize: 14,
      color: colors.alpha.black[70],
    },
    body2: {
      fontSize: 14,
      color: colors.alpha.black[60],
    },
    button: {
      fontWeight: 600,
    },
    caption: {
      fontSize: 13,
      textTransform: "uppercase",
      color: colors.alpha.black[50],
    },
    subtitle1: {
      fontSize: 14,
      color: colors.alpha.black[70],
    },
    subtitle2: {
      fontWeight: 400,
      fontSize: 15,
      color: colors.alpha.black[70],
    },
    overline: {
      fontSize: 13,
      fontWeight: 700,
      textTransform: "uppercase",
    },
  },
});
