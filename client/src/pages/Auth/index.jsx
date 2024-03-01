import * as React from "react";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import { Auth } from "../../components/Auth";

export default function AuthDialog() {
  const [open, setOpen] = React.useState(true);

  //!Opening auth dialog will be triggered by either clicking on the sign in/up buttons, profile drop down (if user not logged in)
  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  return (
    <>
      <Auth />
    </>
    // <React.Fragment>
    //   {/* <Button variant="outlined" onClick={handleClickOpen}>
    //     Open form dialog
    //   </Button> */}
    //   <Dialog
    //     open={open}
    //     onClose={handleClose}
    //     PaperProps={{
    //       component: "form",
    //       onSubmit: (event) => {
    //         event.preventDefault();
    //         const formData = new FormData(event.currentTarget);
    //         const formJson = Object.fromEntries(formData.entries());
    //         const email = formJson.email;
    //         console.log(email);
    //         handleClose();
    //       },
    //     }}
    //   >
    //     <DialogContent>
    //       <Auth />
    //     </DialogContent>
    //     <DialogActions>
    //       <Button onClick={handleClose}>Cancel</Button>
    //     </DialogActions>
    //   </Dialog>
    // </React.Fragment>
  );
}
