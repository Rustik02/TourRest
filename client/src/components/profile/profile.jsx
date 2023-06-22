import React, { useContext, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import "./profile.css";

const Profile = () => {
  const { UpdateUser, registerUser } = useContext(AuthContext);
  const { user, logoutUser } = useContext(AuthContext);
  const [isActive, setIsActive] = useState(false);
  function btnHandler() {
    setIsActive(true);
  }

  function closeHandler() {
    setIsActive(false);
  }
  console.log(user);
  return (
    <div className="bodies">
      <div className="wrapper">
        <div
          className={`profile-card js-profile-card ${isActive ? "active" : ""}`}
        >
          <div className="profile-card__img">
            <img
              className="imgs"
              src={`http://127.0.0.1:8000${user.image}`}
              alt="profile card"
            />
          </div>

          <div className="profile-card__cnt js-profile-cnt">
           <div className="profile-card__name">{user.username}</div>
            <div className="profile-card-loc">
              <span className="profile-card-loc__icon">
                <svg className="icons">
                  <use xlinkHref="#icon-location"></use>
                </svg>
              </span>

              <span className="profile-card-loc__txt">{user.address}</span>
            </div>

            <div className="profile-card-inf">
              <div className="profile-card-inf__item">
                <div className="profile-card-inf__title">{user.phone}</div>
                <div className="profile-card-inf__txt">Phone</div>
              </div>

              <div className="profile-card-inf__item">
                <div className="profile-card-inf__title">{user.email}</div>
                <div className="profile-card-inf__txt">Email</div>
              </div>

              <div className="profile-card-inf__item">
                <div className="profile-card-inf__title">{user.date_joined}</div>
                <div className="profile-card-inf__txt">Joined data</div>
              </div>
            </div>

            <div className="profile-card-social">
              <h1>About Me</h1>
              <div className="about">{user.description}</div>
            </div>

            <div className="profile-card-ctr">
              <button
                onClick={() => {
                  btnHandler();
                }}
                className="profile-card__button button--blue js-message-btn"
              >
                Edit Profile
              </button>
              <button className="profile-card__button button--orange">
                <Link className="backLink" to="/">
                  Back
                </Link>
              </button>
              <button className="profile-card__button button--orange" onClick={()=> {
                logoutUser();
              }}>
                  Log out
              </button>
            </div>
          </div>

          <div className="profile-card-message js-message">
            <form className="profile-card-form" onSubmit={UpdateUser}>
              <div className="profile-card-form__container">
                <input type="text" name="username" placeholder="name" />
                <input type="email" name="email" placeholder="email" />
                <input type="phone" name="phone" placeholder="phone number" />
                <input type="password" name="password" placeholder="password" />
                <textarea name="description" placeholder="Say something..."></textarea>
              </div>

              <div className="profile-card-form__bottom">
                <button
                type="submit"
                  onClick={() => {
                    closeHandler();
                  }}
                  className="profile-card__button button--blue js-message-close"
                >
                  Send
                </button>

                <button
                  onClick={() => {
                    closeHandler();
                  }}
                  className="profile-card__button button--gray js-message-close"
                >
                  Cancel
                </button>
              </div>
            </form>

            <div className="profile-card__overlay js-message-close"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
