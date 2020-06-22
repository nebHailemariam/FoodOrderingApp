import React from "react";
import logo from "../../images/logo.png";

class NavBar extends React.Component {
  render() {
    return (
      <div>
        <div class="navbar navbar-expand-lg py-3 navbar-dark bg-dark shadow-sm">
          <div class="container">
            <a href="#" class="navbar-brand">
              <img
                src={logo}
                width="45"
                alt=""
                class="d-inline-block align-middle mr-2"
              ></img>
              <span class="text-uppercase font-weight-bold">uEat</span>
            </a>

            <button
              type="button"
              data-toggle="collapse"
              data-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
              class="navbar-toggler"
            >
              <span class="navbar-toggler-icon"></span>
            </button>

            <div
              id="navbarSupportedContent"
              class="collapse navbar-collapse"
              style={{ padding: "-100%" }}
            >
              <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                  <a href="#" class="nav-link">
                    Home <span class="sr-only">(current)</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a href="#" class="nav-link">
                    About
                  </a>
                </li>
                <li class="nav-item">
                  <a href="#" class="nav-link">
                    Services
                  </a>
                </li>
                <li class="nav-item">
                  <a href="#" class="nav-link">
                    Contact
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default NavBar;
