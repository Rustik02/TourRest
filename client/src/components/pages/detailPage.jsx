import React from "react";
import { TourContext, TourProvider } from "../context/tourContext";
import { useContext } from "react";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Detail } from "../detail/Detail";

export function DetailPage() {
	const { movie, changeMovie } = useContext(TourContext);
	const [tourData, setTourData] = useState(null);

	const { id } = useParams();
	const { name } = useParams();

	async function fetchTour() {
		try {
			let response = await fetch(
				`http://127.0.0.1:8000/api/v1/tours/?tour-id=${id}`
			);
			let result = await response.json();
			setTourData(result[0]);
		} catch (error) {}
	}

	useEffect(() => {
		fetchTour();
	}, []);

	if (tourData === null) {
		return <div>Loading...</div>;
	} else {
		return <Detail movie={tourData} />;
	}
}
