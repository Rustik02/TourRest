import React, { useEffect, useState, useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import "./register.css";

const Registration = () => {
  const { loginUser, registerUser } = useContext(AuthContext);

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const { user } = useContext(AuthContext);
  const [container, setContainer] = useState("");
  const [loginel, setLoginel] = useState("");
  const [registerel, setRegisterel] = useState("");
  useEffect(() => {
    setContainer(document.getElementById("containerr"));
    setLoginel(document.getElementsByClassName("login")[0]);
    setRegisterel(document.getElementsByClassName("page front")[0]);
  });

  function register() {
    container.className = "active";
    loginel.style.background = "none";
    registerel.style.visibility = "hidden";
  }
  function login() {
    container.className = "close";
    loginel.style.background = "#FAFAFA";
    registerel.style.visibility = "visible";
  }
  return (
    <div className="bodyy">
      <div id="containerr">
        <div className="login">
          <div className="content">
            <h1 className="h1">Log In</h1>
            <div className="form">
              <input type="email" name="email" placeholder="email" onChange={(e)=>{setUsername(String(e.target.value))}} value={username} />
              <input type="password" name="password" placeholder="password" onChange={(e)=>{setPassword(String(e.target.value))}} value={password} />
              <div className="spanContent">
                <span id="span" className="remember">
                  Remember me
                </span>
                <span id="span" className="forget">
                  Forgot password?
                </span>
              </div>
              <span id="span" className="clearfix"></span>
              <div onClick={()=>{loginUser(username, password)}} className="button">
                Log In
              </div>
            </div>
            <div className="svgContent">
              <span className="loginwith">Or Connect with</span>
              <a href="https://www.facebook.com/emin.qasimovdia">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  id="svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  className="feather feather-facebook"
                >
                  <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
                </svg>
              </a>
              <a href="https://www.twitter.com/webkoder">
                <svg
                  className="feather feather-twitter sc-dnqmqq jxshSx"
                  id="svg"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
                </svg>
              </a>
              <a href="https://www.github.com/eminqasimov">
                <svg
                  className="feather feather-github sc-dnqmqq jxshSx"
                  id="svg"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                </svg>
              </a>
              <a href="#">
                {" "}
                <svg
                  className="feather feather-linkedin sc-dnqmqq jxshSx"
                  id="svg"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  aria-hidden="true"
                >
                  <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                  <rect x="2" y="9" width="4" height="12"></rect>
                  <circle cx="4" cy="4" r="2"></circle>
                </svg>
              </a>
            </div>
          </div>
        </div>
        <div className="page front">
          <div className="content">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              id="svg"
              width="96"
              height="96"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              className="feather feather-user-plus"
            >
              <path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
              <circle cx="8.5" cy="7" r="4" />
              <line x1="20" y1="8" x2="20" y2="14" />
              <line x1="23" y1="11" x2="17" y2="11" />
            </svg>
            <h1 className="h1">Hello, friend!</h1>
            <p className="p">
              Enter your personal details and start journey with us
            </p>
            <button
              className="button"
              type=""
              id="register"
              onClick={() => {
                register();
              }}
            >
              Register{" "}
              <svg
                xmlns="http://www.w3.org/2000/svg"
                id="svga"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                className="feather feather-arrow-right-circle"
              >
                <circle cx="12" cy="12" r="10" />
                <polyline points="12 16 16 12 12 8" />
                <line x1="8" y1="12" x2="16" y2="12" />
              </svg>
            </button>
          </div>
        </div>
        <div className="page back">
          <div className="content">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              id="svg"
              width="96"
              height="96"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              className="feather feather-log-in"
            >
              <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
              <polyline points="10 17 15 12 10 7" />
              <line x1="15" y1="12" x2="3" y2="12" />
            </svg>
            <h1 className="h1">Welcome Back!</h1>
            <p className="p">
              To keep connected with us please login with your personal info
            </p>
            <button
              className="button"
              type=""
              id="login"
              onClick={() => {
                login();
              }}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                id="svga"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                className="feather feather-arrow-left-circle"
              >
                <circle cx="12" cy="12" r="10" />
                <polyline points="12 8 8 12 12 16" />
                <line x1="16" y1="12" x2="8" y2="12" />
              </svg>{" "}
              Log In
            </button>
          </div>
        </div>
        <div className="register">
          <div className="content">
            <h1 className="h1">Sign Up</h1>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              id="svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              className="feather feather-facebook"
            >
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
            </svg>
            <svg
              className="feather feather-twitter sc-dnqmqq jxshSx"
              id="svg"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              aria-hidden="true"
            >
              <path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path>
            </svg>
            <svg
              className="feather feather-github sc-dnqmqq jxshSx"
              id="svg"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              aria-hidden="true"
            >
              <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
            </svg>
            <svg
              className="feather feather-linkedin sc-dnqmqq jxshSx"
              id="svg"
              xmlns="http://www.w3.org/2000/svg"
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
              aria-hidden="true"
            >
              <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
              <rect x="2" y="9" width="4" height="12"></rect>
              <circle cx="4" cy="4" r="2"></circle>
            </svg>

            <span id="span" className="loginwith">
              Or
            </span>

            <form className="form" onSubmit={registerUser}>
              <input type="text" name="username" placeholder="username" required="" />
              <input type="email" name="email" placeholder="email" required="" />
              <input type="phone" name="phone" placeholder="phone number" required="" />
              <input type="password" name="password" placeholder="password" required="" />
              <span id="span" className="remember">
                I accept terms
              </span>
              <span id="span" className="clearfix"></span>
              <button type="submit" className="button">
                Register
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Registration;
