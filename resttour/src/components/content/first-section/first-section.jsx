import "@coreui/coreui/dist/css/coreui.min.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "./first-section.css";
export function FirstSection(params) {
  return (
    <div>
      <section class="travel">
        <div class="block-container">
          <div class="row">
            <div class="col-md-12">
              <div class="single-travel-boxes">
                <div id="desc-tabs" class="desc-tabs">
                  <ul class="nav nav-tabs" role="tablist">
                    <li role="presentation" class="active">
                      <a
                        href="#tours"
                        aria-controls="tours"
                        role="tab"
                        data-toggle="tab"
                      >
                        <i class="fa fa-tree"></i>
                        tours
                      </a>
                    </li>
                    <li role="presentation">
                      <a
                        href="#hotels"
                        aria-controls="hotels"
                        role="tab"
                        data-toggle="tab"
                      >
                        <i class="fa fa-building"></i>
                        hotels
                      </a>
                    </li>
                    <li role="presentation">
                      <a
                        href="#flights"
                        aria-controls="flights"
                        role="tab"
                        data-toggle="tab"
                      >
                        <i class="fa fa-plane"></i>
                        flights
                      </a>
                    </li>
                  </ul>
                  <div class="tab-content">
                    <div
                      role="tabpanel"
                      class="tab-pane active fade in"
                      id="tours"
                    >
                      <div class="tab-para">
                        <div class="row">
                          <div class="col-lg-4 col-md-4 col-sm-12">
                            <div class="single-tab-select-box">
                              <h2>destination</h2>
                              <div class="select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your destination country
                                  </option>
                                  <option value="turkey">turkey</option>
                                  <option value="russia">russia</option>
                                  <option value="egept">egypt</option>
                                </select>
                              </div>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your destination location
                                  </option>
                                  <option value="istambul">istambul</option>
                                  <option value="mosko">mosko</option>
                                  <option value="cairo">cairo</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>check in</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="check_in"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="12 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>check out</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="check_out"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="22 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>duration</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">5</option>
                                  <option value="10">10</option>
                                  <option value="15">15</option>
                                  <option value="20">20</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>members</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">1</option>
                                  <option value="2">2</option>
                                  <option value="4">4</option>
                                  <option value="8">8</option>
                                </select>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-sm-5">
                            <div class="travel-budget">
                              <div class="row">
                                <div class="col-md-3 col-sm-4">
                                  <h3>budget : </h3>
                                </div>
                                <div class="co-md-9 col-sm-8">
                                  <div class="travel-filter">
                                    <div class="info_widget">
                                      <div class="price_filter">
                                        <div id="slider-range"></div>
                                        <div class="price_slider_amount">
                                          <input
                                            type="text"
                                            id="amount"
                                            name="price"
                                            placeholder="Add Your Price"
                                          />
                                        </div>
                                      </div>
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                          <div class="clo-sm-7">
                            <div class="about-btn travel-mrt-0 pull-right">
                              <button class="about-view travel-btn">
                                search
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    {/* <div role="tabpanel" class="tab-pane fade in" id="hotels">
                      <div class="tab-para">
                        <div class="row">
                          <div class="col-lg-4 col-md-4 col-sm-12">
                            <div class="single-tab-select-box">
                              <h2>destination</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your destination country
                                  </option>
                                  <option value="turkey">turkey</option>
                                  <option value="russia">russia</option>
                                  <option value="egept">egypt</option>
                                </select>
                              </div>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your destination location
                                  </option>
                                  <option value="istambul">istambul</option>
                                  <option value="mosko">mosko</option>
                                  <option value="cairo">cairo</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>check in</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="check_in"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="12 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>

                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>check out</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="check_out"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="22 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>

                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>duration</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">5</option>

                                  <option value="10">10</option>

                                  <option value="15">15</option>
                                  <option value="20">20</option>
                                </select>
                              </div>
                            </div>
                          </div>

                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>members</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">1</option>

                                  <option value="2">2</option>

                                  <option value="4">4</option>
                                  <option value="8">8</option>
                                </select>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div class="row">
                          <div class="col-sm-5"></div>
                          <div class="clo-sm-7">
                            <div class="about-btn travel-mrt-0 pull-right">
                              <button class="about-view travel-btn">
                                search
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>

                    <div role="tabpanel" class="tab-pane fade in" id="flights">
                      <div class="tab-para">
                        <div class="trip-circle">
                          <div class="single-trip-circle">
                            <input type="radio" id="radio01" name="radio" />
                            <label for="radio01">
                              <span class="round-boarder">
                                <span class="round-boarder1"></span>
                              </span>
                              round trip
                            </label>
                          </div>
                          <div class="single-trip-circle">
                            <input type="radio" id="radio02" name="radio" />
                            <label for="radio02">
                              <span class="round-boarder">
                                <span class="round-boarder1"></span>
                              </span>
                              on way
                            </label>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-lg-4 col-md-4 col-sm-12">
                            <div class="single-tab-select-box">
                              <h2>from</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your location
                                  </option>
                                  <option value="turkey">turkey</option>
                                  <option value="russia">russia</option>
                                  <option value="egept">egypt</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>departure</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="departure"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="12 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>return</h2>
                              <div class="travel-check-icon">
                                <form action="#">
                                  <input
                                    type="text"
                                    name="return"
                                    class="form-control"
                                    data-toggle="datepicker"
                                    placeholder="22 -01 - 2017 "
                                  />
                                </form>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>adults</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">5</option>
                                  <option value="10">10</option>
                                  <option value="15">15</option>
                                  <option value="20">20</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-2 col-md-1 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>childs</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">1</option>
                                  <option value="2">2</option>
                                  <option value="4">4</option>
                                  <option value="8">8</option>
                                </select>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="row">
                          <div class="col-lg-4 col-md-4 col-sm-12">
                            <div class="single-tab-select-box">
                              <h2>to</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">
                                    enter your destination location
                                  </option>
                                  <option value="istambul">istambul</option>
                                  <option value="mosko">mosko</option>
                                  <option value="cairo">cairo</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="col-lg-3 col-md-3 col-sm-4">
                            <div class="single-tab-select-box">
                              <h2>class</h2>
                              <div class="travel-select-icon">
                                <select class="form-control ">
                                  <option value="default">enter class</option>
                                  <option value="A">A</option>
                                  <option value="B">B</option>
                                  <option value="C">C</option>
                                </select>
                              </div>
                            </div>
                          </div>
                          <div class="clo-sm-5">
                            <div class="about-btn pull-right">
                              <button class="about-view travel-btn">
                                search
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div> */}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
