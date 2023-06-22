import React, { createContext, useState } from "react";

export const TourContext = createContext();

export const TourProvider = ({ children }) => {
	const [tourDetail, setTourDetail] = useState(null);

	return (
		<TourContext.Provider value={{ tourDetail, setTourDetail }}>
			{children}
		</TourContext.Provider>
	);
};