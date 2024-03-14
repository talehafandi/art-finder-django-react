import * as React from "react";
import SvgIcon from "@mui/material/SvgIcon";

export default function SculptureIcon(props) {
  return (
    <SvgIcon {...props}>
      <svg
        width="41"
        height="56"
        viewBox="0 0 41 56"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g fill={props.color || "#3F3F3F"}>
          <path
            fillRule="evenodd"
            clipRule="evenodd"
            d="M18.1485 0.0167831C35.0931 -0.592421 36.3265 13.8447 27.4635 22.5799C27.4274 29.2645 35.4035 30.3033 40.6142 31.5508C40.7055 31.8226 40.7969 32.0945 40.8882 32.3663C39.978 34.9893 36.7128 35.5344 35.1348 37.5313C32.9904 40.2452 31.5211 43.2365 30.2033 46.7741C30.2946 46.9553 30.3859 47.1365 30.4772 47.3178L37.6005 47.5896C37.6761 50.1721 37.8789 53.7406 37.0526 55.4731C30.2961 55.5288 8.61257 56.9234 4.17585 54.9294L4.44983 47.3178L11.5731 47.0459V46.7741C8.24353 40.4249 6.08517 37.1856 0.888184 32.91L1.16216 31.5508C5.20298 30.1915 12.3002 29.2314 14.0389 25.5702L14.5868 22.8517C10.532 19.5997 6.48435 9.42071 11.0252 3.55076C12.6706 1.42385 15.4838 1.20529 18.1485 0.0167831ZM18.4224 2.46338C16.3304 3.36265 13.8657 3.70762 12.669 5.45368C8.60983 11.3764 15.6326 24.8248 21.4361 22.8517C30.9372 21.8693 36.4833 1.79111 18.4224 2.46338ZM16.7786 24.4828C16.3591 30.1415 9.85887 31.7506 4.99777 32.91L5.54572 33.1818C12.932 41.0289 29.5378 40.6103 36.7786 32.91C30.4057 31.5731 27.3145 29.7188 24.7238 24.4828C22.0033 25.7637 19.5616 25.3815 16.7786 24.4828ZM10.7512 39.1624C11.9953 41.6362 13.2717 43.6661 14.0389 46.7741H27.7375C28.4054 43.6799 29.74 41.572 31.0252 39.1624C24.7356 42.25 17.0463 42.2141 10.7512 39.1624ZM6.64161 49.7644V53.0265H35.1348V49.7644H6.64161Z"
          />
        </g>
      </svg>
    </SvgIcon>
  );
}
