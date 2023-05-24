import "@coreui/coreui/dist/css/coreui.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { FirstSection } from "./first-section/first-section";
import "./header.css";
import React, { useState, useEffect } from "react";
import {Hero} from "./hero/hero";

export function Header(params) {
  const [isScrolled, setIsScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollTop = window.pageYOffset;

      if (scrollTop > 0) {
        setIsScrolled(true);
      } else {
        setIsScrolled(false);
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);

  return (
    <div>
      <header>
        <div className="header">
          <div className={`containerr ${isScrolled ? "scrolled" : ""}`}>
            <div className={`wrapper ${isScrolled ? "scrolled" : ""}`} >
            <div className="nav-logo">
              <h1 className="logo">TourRest</h1>
            </div>
            <div className="nav-nobullet">
              <ul className="nobullet">
                <li className="smooth-menu">
                  <a href="#home">Home</a>
                </li>
                <li className="smooth-menu">
                  <a href="#gallery">Destination</a>
                </li>
                <li className="smooth-menu">
                  <a href="#pack">Packages </a>
                </li>
                <li className="smooth-menu">
                  <a href="#spo">Special Offers</a>
                </li>
                <li className="smooth-menu">
                  <a href="#blog">Blog</a>
                </li>
                <li className="smooth-menu">
                  <a href="#subs">Subscription</a>
                </li>
                <li>
                  <button className="order-online">book now</button>
                </li>
              </ul>
            </div>

            </div>
          </div>
          <Hero/>
        </div>
      </header>
    </div>
  );
}
