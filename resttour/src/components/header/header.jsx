import "@coreui/coreui/dist/css/coreui.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { FirstSection } from "./first-section/first-section";
import "./header.css";
import React, { useState, useEffect } from "react";

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
          <div className={`container ${isScrolled ? "scrolled" : ""}`}>
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
          <section>
            <div className="row">
                <h2>Explore the Beauty of the Beautiful World</h2>
                <div className="about-btn">
                  <button className="order-online1">explore now</button>
              </div>
            </div>
          </section>
        </div>
      </header>
    </div>
  );
}
