import React, {useEffect, useState} from "react";
import "./home.css";
import splash from "../../assets/splash.mp4";
import { GrLocation } from "react-icons/gr";
import { HiFilter } from "react-icons/hi";
import { FiFacebook } from "react-icons/fi";
import { AiOutlineInstagram } from "react-icons/ai";
import { FaTripadvisor } from "react-icons/fa";
import { BsListTask } from "react-icons/bs";
import { TbApps } from "react-icons/tb";
import Aos from 'aos'
import 'aos/dist/aos.css'


const Home = () => {

  const [destination, setDestination] = useState('')
  const [date, setDate] = useState('')



  const handleName = (e) => {
    let name= e.target.value
    setDestination(name)
    console.log(destination);
  }
  const handleDate = (e) => {
    let name= e.target.value
    setDate(name)
    console.log(date);
  }

  

  useEffect(() => {
    Aos.init({duration: 2000})
  }, [])
  return (
    <section className="home">
      <div className="overlay"></div>
      <video src={splash} muted autoPlay loop type="video/mp4"></video>

      <div className="homeContent container">
        <div className="textDiv">
          <span data-aos="fade-up" className="smallText">Our Packages</span>
          <h1 data-aos="fade-up" className="homeTitle">Search your Holiday</h1>
        </div>
        <div data-aos="fade-up" className="cardDiv grid">
          <div className="destinationInput">
            <label htmlFor="city">Search your destination:</label>
            <div className="input flex">
              <input type="text" placeholder="Enter name here...." onChange={handleName} />
              <GrLocation className="icon" />
            </div>
          </div>
          <div className="dateInput">
            <label htmlFor="date">Select your date:</label>
            <div className="input flex">
              <input type="date" placeholder="Enter date here...." onChange={handleDate}/>
            </div>
          </div>
          <div className="priceInput">
            <div className="label_total flex">
              <label htmlFor="price">Max price:</label>
              <h3 className="total">$5000</h3>
            </div>
            <div className="input flex">
              <input type="range" max="5000" min="1000" />
            </div>
          </div>

          <div className="searchOptions flex">
            <HiFilter />
            <span>MORE FILTRES</span>
          </div>
        </div>

        <div data-aos="fade-up" className="homeFooterIcons flex">
          <div className="rightIcons">
            <FiFacebook className="icon" />
            <AiOutlineInstagram className="icon" />
            <FaTripadvisor className="icon" />
          </div>
          <div className="leftIcons">
            <BsListTask className="icon" />
            <TbApps className="icon" />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Home;
