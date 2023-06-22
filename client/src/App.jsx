import "./App.css";
import React, { Profiler } from "react";
import Navbar from "./components/Navbar/Navbar";
import Main from "./components/Main/Main";
import Home from "./components/Home/Home";
import Footer from "./components/Footer/Footer";
import Registration from "./components/Registration/Registration";
import { HomePage } from "./components/pages/home";
import {
  BrowserRouter as Router,
  Route,
  Routes,
} from "react-router-dom";
import { AuthProvider } from "./components/context/AuthContext";
import { ProfilePage } from "./components/pages/profilePage";
import { DetailPage } from "./components/pages/detailPage";
import { Detail } from "./components/detail/Detail";
import { TourProvider } from "./components/context/tourContext";
function App() {
  return (
    <>
      <TourProvider>
        <Router>
          <AuthProvider>
            <Routes>
              <Route path="/" element={<HomePage />} exact></Route>
              <Route path="/login" element={<Registration />}></Route>
              <Route path="/profile" element={<ProfilePage />}></Route>
              <Route path="/:name/:id" element={<DetailPage />}></Route>
              <Route path="/:name/:id" element={<Detail />}></Route>
              <Route path="/:details/*" element={<Detail />}></Route>
              {/* <Route path='/login' element={<LoginPage/>}></Route> */}
            </Routes>
          </AuthProvider>
        </Router>
      </TourProvider>
      {/* <Registration/> */}
    </>
  );
}

export default App;
