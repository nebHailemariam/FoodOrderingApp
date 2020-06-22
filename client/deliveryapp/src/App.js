import React from "react";
import { Route } from "react-router-dom";
import ClientRegistration from "./views/security/registration/client_registration";

function App() {
  return (
    <div>
      <Route
        path="/client/registration/"
        component={ClientRegistration}
      ></Route>
    </div>
  );
}
export default App;
