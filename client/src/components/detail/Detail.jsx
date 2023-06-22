import React, { useEffect, useState, useContext } from "react";
import "./detail.css";
import { Link } from "react-router-dom";
import { useLocation, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export const Detail = () => {
  const [detail, setDetails] = useState(null);
  const location = useLocation();
  let navigate = useNavigate();
  const id = Number(location.pathname.split("/")[2]);
  console.log(id);
  const { user } = useContext(AuthContext);

  async function getDetails() {
    try {
      let response = await fetch(
        `http://127.0.0.1:8000/api/v1/tourdetails/${id}`
      );
      let result = await response.json();
      setDetails(result);
    } catch (error) {}
  }
   async function booking ( username, phone){
    try{
		let response = await fetch("http://127.0.0.1:8000/api/v1/booking/", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
        tour_id: id,
				name: username,
				phone: phone,
			}),
		});
		let data = await response.json();
  }catch(error){}
	};

  useEffect(() => {
    getDetails();
  }, []);

  if (detail != null) {
    return (
      <div className="body">
        <div className="contaiiner">
          <div className="mySwiper">
            <div className="mainn-wrapper swiper-wrapper">
              <div className="mainn" id="beach">
                <div className="center">
                  <div className="right-side__img">
                    <img className="bottle-bg" src={detail.image1} alt="" />
                  </div>
                  <div className="right-side__img">
                    <img className="bottle-bg" src={detail.image2} alt="" />
                  </div>
                  <div className="right-side__img">
                    <img className="bottle-bg" src={detail.image3} alt="" />
                  </div>
                  <div className="right-side__img">
                    <img className="bottle-bg" src={detail.image4} alt="" />
                  </div>
                  <div className="right-side__img">
                    <img className="bottle-bg" src={detail.image5} alt="" />
                  </div>
                </div>
                <div className="left-side">
                  <div className="mainn-wrapper">
                    <h3 className="mainn-header">{detail.tour.country.name}</h3>
                    <h1 className="mainn-title">{detail.tour.title}</h1>
                    <h2 className="mainn-subtitle">${detail.tour.price}</h2>
                    <h2 className="mainn-subtitle">Duration: {detail.duration}</h2>
                    <h2 className="mainn-subtitle">Difficulty level: {detail.difficulty_level.name}</h2>
                    <h2 className="mainn-subtitle">Season times: {detail.seasons.map((e, ind) => {
                      if (ind != 0)
                        return (','+e.name)
                      else return (e.name)
                    })}</h2>
                    <h2 className="mainn-subtitle">Dates: {detail.start_date} - {detail.end_date}</h2>
                    <h2 className="mainn-subtitle">Group size: {detail.group_size}</h2>
                  </div>
                  <div className="mainn-content">
                    <div className="mainn-content__title">
                    Itinerary: {detail.itinerary}
                    </div>
                    <div className="mainn-content__subtitle">
                    Highlights: {detail.highlights}
                    </div>
                    <div className="mainn-content__subtitle">
                    Price_includes: {detail.price_includes}
                    </div>
                    <button
                      className="more-menu"
                      onClick={() => {
                        if (!user) {
                          navigate("/login");
                        } else {
                          booking(String(user.username), String(user.phone));
                        }
                      }}
                    >
                      BOOK NOW
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  } else {
    return <>....?</>;
  }
};
