import * as React from "react";
import { Auth } from "../../components/Auth";
import { useAppContext } from "../../context/appContext";

export default function AuthDialog() {
  const [open, setOpen] = React.useState(true);
  const { signinPopupVisibility } = useAppContext();

  //!Opening auth dialog will be triggered by either clicking on the sign in/up buttons, profile drop down (if user not logged in)
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  if (signinPopupVisibility == true)
    return (
      <>
        <Auth />
      </>
    );
  else return <></>;
}
