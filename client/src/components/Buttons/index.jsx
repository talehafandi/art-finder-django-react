import Button from "@mui/material/Button";
import { lighten } from "@mui/material";
import { styled } from "@mui/material/styles";

export const PrimaryButton = styled(Button)(
  ({ theme }) => `
       background: ${theme.palette.primary.main};
       color: ${theme.palette.common.white};
       height: 44px !important;
       &:hover {
          background: ${theme.palette.primary.dark};
       }
       white-space: nowrap;
      `
);

export const PrimaryAltButton = styled(Button)(
  ({ theme }) => `
         background: ${theme.palette.common.white};
         color: ${theme.palette.common.black};
         height: 44px !important;
         white-space: nowrap;
         &:hover {
            background: ${lighten(theme.palette.primary.main, 0.85)};
         }
        `
);

export const SecondaryOutlinedButton = styled(Button)(
  ({ theme }) => `
           background: ${theme.palette.common.white};
           color: ${theme.palette.common.black};
           border: 1px solid ${theme.palette.common.black};
           height: 44px !important;
           white-space: nowrap;
           &:hover {
              background: ${lighten(theme.palette.primary.main, 0.85)};
              border: 1px solid ${theme.palette.primary.main}
           }
          `
);
