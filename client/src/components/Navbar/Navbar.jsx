import React, { useState, useContext } from "react";
import "./navbar.css";
import { MdTravelExplore } from "react-icons/md";
import { AiFillCloseCircle } from "react-icons/ai";
import { TbGridDots } from "react-icons/tb";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const Navbar = () => {
  const { logoutUser, user } = useContext(AuthContext);
  const [active, setActive] = useState("navBar");
  const showNav = () => {
    setActive("navBar activeNavbar");
  };
  const removeNavbar = () => {
    setActive("navBar");
  };
  const [isDropdownVisible, setDropdownVisible] = useState(false);
  const toggleDropdown = () => {
    setDropdownVisible(!isDropdownVisible);
  };
  return (
    <section className="navBarSection">
      <header className="header flex">
        <div className="logoDiv">
          <Link to="#" className="logo flex">
            <h1>
              <MdTravelExplore className="icon" />
              TourRest
            </h1>
          </Link>
        </div>

        <div className={active}>
          <ul className="navList flex">
            <li className="navItem">
              <Link to="/" className="navLink">
                Home
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                Packages
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                Shop
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                About
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                Pages
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                News
              </Link>
            </li>

            <li className="navItem">
              <Link to="#" className="navLink">
                Contact
              </Link>
            </li>

            
            {user ?(
              <>
              {user.is_admin == true ? (
                <div>
                  <div className="profile" onClick={toggleDropdown}>
                  <Link to='#'>
                  </Link>
                  </div>
                  <div className="profile" onClick={toggleDropdown}>
                  <Link to='/profile'>
                  <img className="imga" src={user.image} />
                  </Link>
                  </div>
                </div>
            ) : (
                <div className="profile" onClick={toggleDropdown}>
                <Link to='/profile'>
                <div className="imga" style={{backgroundImage:`url(http://127.0.0.1:8000${user.image})`}} />
                </Link>
              </div>
            )}
              </>
            ) : (
              <button className="btn">
              <Link to="/login">SignUp/In</Link>
            </button>
            )}
          </ul>

          <div onClick={removeNavbar} className="closeNavbar">
            <AiFillCloseCircle className="icon" />
          </div>
        </div>

        <div className="toggleNavbar" onClick={showNav}>
          <TbGridDots className="icon" />
        </div>
      </header>
    </section>
  );
};

export default Navbar;
