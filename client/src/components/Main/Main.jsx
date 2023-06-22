import React, { useEffect, useState } from "react";
import "./main.css";
import { HiOutlineLocationMarker } from "react-icons/hi";
import { HiOutlineClipboardCheck } from "react-icons/hi";
import { useNavigate } from "react-router-dom";
import Aos from "aos";

import "aos/dist/aos.css";
import { Link } from "react-router-dom";

const Main = () => {
  let navigate = useNavigate();
  const [details, setDetails] = useState([]);
  const Detail = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/v1/tours/");
    if (response.ok) {
      const data = await response.json();
      setDetails(data);
      console.log(data);
    } else {
      setDetails([]);
    }
  };
  // const Detail = async() => {
  //   let response = await fetch("http://127.0.0.1:8000/api/v1/tours/");
  //   try {
  //   let data = await response.json();
  //   setDetails(data);
  //   console.log(data);
  //   }catch {
  //     setDetails([]);
  //   }
  // }
  useEffect(() => {
    Detail();
    console.log(details);
    Aos.init({ duration: 2000 });
  }, []);

  //   fetch("http://127.0.0.1:8000/api/v1/tours/", )
  //   .then(results => results.json())
  //   .then(data => {
  //     setDetails(data)
  //   })
  //   const fetchData = async () => {
  //     try {
  //       const response = await axios.get("http://127.0.0.1:8000/api/v1/tours/");
  //       const data = response;
  //       setDetails(data);
  //       // Дополнительные действия после получения данных
  //     } catch (error) {
  //       console.log(error);
  //     }
  //   };
  //   Aos.init({ duration: 2000 });
  // }, []);

  return (
    <section className="main container section">
      <div className="secTitle">
        <h3 data-aos="fade-right" className="title">
          Most visited destinations
        </h3>
      </div>
      <div className="secContent grid">
        {details &&
          details.map((e) => {
            return (
              <div key={e.id} data-aos="fade-up" className="singleDestination">
                <div className="imageDiv">
                  <img src={e.image} alt={e.title} />
                </div>

                <div className="cardInfo">
                  <h4 className="desTitle">{e.title}</h4>
                  <span className="continent flex">
                    <HiOutlineLocationMarker className="icon" />
                    <span className="name">{e.country.name}</span>
                  </span>

                  <div className="fees flex">
                    <div className="grade">
                      <span>
                        {e.grade.name}
                        <small>+1</small>
                      </span>
                    </div>
                    <div className="price">
                      <h5>{e.price}</h5>
                    </div>
                  </div>

                  <div className="desc">
                    <p>{e.description}</p>
                  </div>

                  <div className="btn flex" onClick={()=>{navigate(`/detail/${e.id}`)}}>
                    DETAILS <HiOutlineClipboardCheck className="icon" />
                  </div>
                </div>
              </div>
            );
          })}
      </div>
    </section>
  );
};
export default Main;
